import logging
from contextlib import contextmanager

import pytest

import pogo_migrate.config
import pogo_migrate.testing


@contextmanager
def caplog_session(request: pytest.FixtureRequest):  # noqa: ANN201
    request.node.add_report_section = lambda *args: None  # noqa: ARG005
    logging_plugin = request.config.pluginmanager.getplugin("logging-plugin")
    for _ in logging_plugin.pytest_runtest_setup(request.node):
        yield pytest.LogCaptureFixture(request.node, _ispytest=True)


@pytest.fixture()
def pogo_config() -> pogo_migrate.config.Config:
    return pogo_migrate.config.load_config()


@pytest.fixture(scope="session")
async def pogo_engine(request: pytest.FixtureRequest):  # noqa: PT004, ANN201
    with caplog_session(request) as caplog, caplog.at_level(logging.ERROR):
        await pogo_migrate.testing.apply()

    yield

    # Rollback all migrations
    with caplog_session(request) as caplog, caplog.at_level(logging.ERROR):
        await pogo_migrate.testing.rollback()


@pytest.fixture(scope="session")
async def pogo_engine_verbose():  # noqa: PT004, ANN201
    await pogo_migrate.testing.apply()

    yield

    # Rollback all migrations
    await pogo_migrate.testing.rollback()

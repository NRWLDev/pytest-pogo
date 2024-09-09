import logging
import sys
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


@pytest.fixture
def pogo_config() -> pogo_migrate.config.Config:
    return pogo_migrate.config.load_config()


def extract_verbosity() -> int:
    verbose = set(sys.argv) & {"-v", "-vv", "-vvv"}
    # If short verbosity is passed strip the `-` to get count of `v`s for verbosity setting.
    verbose = len(verbose.pop()) - 1 if verbose else 0

    # If full verbose flag is passed in, get count of flags
    verbose = sys.argv.count("--verbose") if "--verbose" in sys.argv else verbose

    return {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
    }.get(verbose, logging.DEBUG)


@pytest.fixture(scope="session")
async def pogo_engine(request: pytest.FixtureRequest):  # noqa: ANN201
    level = extract_verbosity()
    with caplog_session(request) as caplog, caplog.at_level(level):
        await pogo_migrate.testing.apply()

    yield

    # Rollback all migrations
    with caplog_session(request) as caplog, caplog.at_level(level):
        await pogo_migrate.testing.rollback()

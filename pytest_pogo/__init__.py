import asyncio

import pytest

import pogo_migrate.config
import pogo_migrate.testing


@pytest.fixture()
def pogo_config() -> pogo_migrate.config.Config:
    return pogo_migrate.config.load_config()


@pytest.fixture(scope="session")
def pogo_engine():  # noqa: PT004, ANN201
    asyncio.run(pogo_migrate.testing.apply())

    yield

    # Rollback all migrations
    asyncio.run(pogo_migrate.testing.rollback())

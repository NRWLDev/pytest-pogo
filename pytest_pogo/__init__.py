import asyncio

import pytest

import pogo_migrate.testing


@pytest.fixture(scope="session")
def pogo_engine():  # noqa: PT004, ANN201
    asyncio.run(pogo_migrate.testing.apply())

    yield

    # Rollback all migrations
    asyncio.run(pogo_migrate.testing.rollback())

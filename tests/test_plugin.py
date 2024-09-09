import os
from pathlib import Path

import asyncpg
import pytest

import pogo_migrate.config
import pytest_pogo  # noqa: F401


@pytest.fixture
def postgres_dsn():
    return os.environ["POSTGRES_DSN"]


def test_config_fixture(pogo_config):
    assert pogo_config == pogo_migrate.config.Config(
        migrations=Path.cwd() / "tests/migrations",
        database_config="{POSTGRES_DSN}",
        root_directory=Path.cwd(),
    )


@pytest.mark.usefixtures("pogo_engine")
async def test_engine_applies_migrations(pogo_config):
    db = await asyncpg.connect(pogo_config.database_dsn)
    stmt = """
    SELECT tablename
    FROM pg_tables
    WHERE  schemaname = 'public'
    ORDER BY tablename
    """
    results = await db.fetch(stmt)

    assert [r["tablename"] for r in results] == ["_pogo_migration", "_pogo_version", "table_one", "table_two"]

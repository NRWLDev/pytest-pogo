import os

import asyncpg
import pytest

import pytest_pogo


@pytest.fixture()
def postgres_dsn():
    return os.environ["POSTGRES_DSN"]


@pytest.mark.usefixtures("pogo_engine")
async def test_engine_applies_migrations(postgres_dsn):
    db = await asyncpg.connect(postgres_dsn)
    stmt = """
    SELECT tablename
    FROM pg_tables
    WHERE  schemaname = 'public'
    ORDER BY tablename
    """
    results = await db.fetch(stmt)

    assert [r["tablename"] for r in results] == ["_pogo_migration", "_pogo_version", "table_one", "table_two"]

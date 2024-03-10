"""
initial migration
"""

__depends__ = []


async def apply(db):
    await db.execute("CREATE TABLE table_one()")


async def rollback(db):
    await db.execute("DROP TABLE table_one")

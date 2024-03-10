"""
second migration
"""

__depends__ = ["20240310_01_vlvda-initial-migration"]


async def apply(db):
    await db.execute("CREATE TABLE table_two()")


async def rollback(db):
    await db.execute("DROP TABLE table_two")

import asyncio
import sqlite3

import aiosqlite

#
# def try_make_db() -> None:
#     with sqlite3.connect('sqlite_db') as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """CREATE TABLE IF NOT EXISTS  delivieries  (
#             id TEXT PRIMARY KEY,
#             status TEXT)
#         """
#         )
#         conn.commit()
#


async def try_make_db():
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS  delivieries  (
                id TEXT PRIMARY KEY,
                status TEXT)
            """)
        await db.commit()


async def insert_values(id,status):
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        try:
            await db.execute("""INSERT INTO delivieries VALUES 
                       ('{0}', '{1}')
                   """.format(id,status))

            await db.commit()
        except sqlite3.IntegrityError:
            await db.execute("""UPDATE delivieries SET status ='{1}' WHERE ID = '{0}'
                               """.format(id, status))

            await db.commit()
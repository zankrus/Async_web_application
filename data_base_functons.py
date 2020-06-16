"""File with DB functions."""
import sqlite3
from typing import Any

import aiosqlite


async def try_make_db() -> None:
    """Async creating of DB."""
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS  delivieries  (
                id TEXT PRIMARY KEY,
                status TEXT)
            """)
        await db.commit()


async def insert_values(id: str, status: str) -> Any:
    """ASYNC inserting or updating DB."""
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        try:
            await db.execute("""INSERT OR REPLACE INTO
            delivieries (id , status) VALUES ('{0}', '{1}')
                   """.format(id, status))
            print('Запись добавлена в БД')
            await db.commit()
        except sqlite3.IntegrityError:
            return False


async def select_db() -> list:
    """Selecting from DB."""
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        summary = []
        cursor = await db.execute('SELECT * FROM delivieries')
        rows = await cursor.fetchall()
        for row in rows:
            ident = {'id': row[0]}
            status = {'status': row[1]}
            summary.append((ident, status))
        return summary

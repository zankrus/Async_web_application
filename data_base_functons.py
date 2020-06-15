import asyncio
import sqlite3
import aiosqlite
import requests

from service import id_randomizer


async def try_make_db():
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS  delivieries  (
                id TEXT PRIMARY KEY,
                status TEXT)
            """)
        await db.commit()


async def insert_values(id, status):
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        try:
            await db.execute("""INSERT INTO delivieries (id , status) VALUES 
                       ('{0}', '{1}')
                   """.format(id, status))
            print('Запись добавлена в БД')
            await db.commit()
        except sqlite3.IntegrityError:
            await db.execute("""UPDATE delivieries SET status ='{1}' WHERE ID = '{0}'
                               """.format(id, status))
            print('Запись обновлена в БД')
            await db.commit()


async def select_db():
    async with aiosqlite.connect('sqlite_db_deliviery') as db:
        summary = []
        cursor = await db.execute('SELECT * FROM delivieries')
        rows = await cursor.fetchall()
        for row in rows:
            ident = {'id': row[0]}
            status = {'status': row[1]}
            summary.append((ident, status))
        return summary



"""Файл для работы с БД"""
import psycopg2



def db_connector(function):
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="221052",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()
    def wrapper():
        print('Создаем подключение к БД')
        function(connection, cursor)
        print('Закрываем соединение')
    return wrapper


@db_connector
def data_base_creating(connection, cursor) -> None:
    """Функция создает таблицу ROBENS."""
    cursor.execute('''CREATE TABLE IF NOT EXISTS ROBENS2
         (ID SERIAL  PRIMARY KEY NOT NULL ,
         SENDER VARCHAR NOT NULL,
         RECIPIENT VARCHAR NOT NULL,
         STATUS VARCHAR NOT NULL,
         WEIGHT INTEGER NOT NULL,
         CREATION_TIME VARCHAR NOT NULL,
         APPROVE_CODE VARCHAR NOT NULL);''')

    connection.commit()

data_base_creating()

def insert_goods(a: dict) -> None:
    """Функция вставляет значения в таблицу GOODS или обновляет их, если они уже вставлены."""
    a = a
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO GOODS (ID,NAME,PACKAGE_HEIGHT,PACKAGE_WIDTH) VALUES (%s, %s, %s, %s);",
            (a['id'], a['name'], a['height'], a['width'])
        )

        con.commit()
    except psycopg2.errors.UniqueViolation:
        cur.execute("ROLLBACK")
        con.commit()
        cur.execute(
            "UPDATE GOODS SET NAME = %s ,PACKAGE_HEIGHT = %s, PACKAGE_WIDTH = %s WHERE ID = %s",
            (a['name'], a['height'], a['width'], a['id'])
        )
        con.commit()

#
# def insert_shops_goods(a: dict) -> None:
#     """Функция вставляет значения в таблицу SHOPS_GOODS, или обновляет их."""
#     b = select()
#     a = a
#     cur = con.cursor()
#     if (a['id'], a['location']) in b:
#         cur.execute(
#             "UPDATE SHOPS_GOODS SET AMOUTH = %s  WHERE LOCATION = %s AND ID_GOOD = %s",
#             (a['amount'], a['location'], a['id'])
#         )
#         con.commit()
#     else:
#         cur.execute(
#             "INSERT INTO SHOPS_GOODS (ID,ID_GOOD,LOCATION,AMOUTH) VALUES (default,%s, %s, %s)",
#             (a['id'], a['location'], a['amount'])
#         )
#         con.commit()
#
#
# def select() -> list:
#     """Вспомоготельная функция , нужная для проверки  вставленных значений в SHOPS_GOODS."""
#     cur = con.cursor()
#     cur.execute("SELECT  ID_GOOD,LOCATION from SHOPS_GOODS")
#     rows = cur.fetchall()
#     flag = []
#
#     for row in rows:
#         flag.append((row[0], row[1]))
#
#     return flag

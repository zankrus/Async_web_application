import psycopg2


if __name__ == '__main__':


    with psycopg2.connect(
        database="postgres",
        user="postgres",
        password="221052",
        host="127.0.0.1",
        port="5432"
    ) as connection:
        with connection.cursor() as cursor:
            data_base_creating(cursor)
            connection.commit()

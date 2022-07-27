import sqlite3 as sl


def create_products_db():
    con = sl.connect('mybot.db')

    with con:
        con.execute("""
            CREATE TABLE PRODUCTS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                products_name TEXT,
                flavor TEXT,
                package_type TEXT,
                id_insales INTEGER,
                dm_sku TEXT,
                price INTEGER
            );
        """)

    sql = 'INSERT INTO PRODUCTS (products_name, flavor, package_type, id_insales, price) values(?, ?, ?, ?, ?)'
    data = [
        ('Digital Meal Original Ваниль', 'ваниль', 'пакет', 77277687, 1425),
        ('Digital Meal Original Ваниль', 'ваниль', 'пакет', 105796382, 4900),
        ('Digital Meal Original Ваниль', 'ваниль', 'пакет', 105917378, 10500),
        ('Digital Meal Original Ваниль', 'ваниль', 'банка', 379431066, 3710),
        ('Digital Meal Original Ваниль', 'ваниль', 'банка', 243602670, 6600),
        ('Digital Meal Original Ваниль', 'ваниль', 'банка', 243606417, 9850),
        ('Digital Meal Original Ваниль', 'ваниль', 'бутылка', 346764601, 1710),
        ('Digital Meal Original Ваниль', 'ваниль', 'бутылка', 391306253, 7950),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'пакет', 265726303, 1475),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'пакет', 265727388, 5600),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'пакет', 265728072, 10800),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'банка', 450053113, 3990),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'банка', 265728560, 7350),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'банка', 265728752, 10250),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'бутылка', 346761481, 1770),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'бутылка', 391307638, 8550),
        ('Digital Meal "Starter Kit"', 'микс', ' бутылка', 338585388, 1890),
        ('Digital Meal Original Банан ', 'банан', 'банка', 504765716, 3710),
        ('Digital Meal Original Банан ', 'банан', 'банка', 504768608, 6600),
        ('Digital Meal Original Банан ', 'банан', 'банка', 510689914, 1900)
    ]

    con = sl.connect('mybot.db')
    with con:
        con.executemany(sql, data)

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
                price INTEGER
            );
        """)

    sql = 'INSERT INTO PRODUCTS (products_name, flavor, package_type, id_insales, price) values(?, ?, ?, ?, ?)'
    data = [
        ('Digital Meal Original Ваниль', 'ваниль', 'Пакет/5 порций', 77277687, 1425),
        ('Digital Meal Original Ваниль', 'ваниль', '4 пакета/20 порций', 105796382, 4900),
        ('Digital Meal Original Ваниль', 'ваниль', '10 пакетов/50 порций', 105917378, 10500),
        ('Digital Meal Original Ваниль', 'ваниль', '1,4кг/14 порций', 379431066, 3710),
        ('Digital Meal Original Ваниль', 'ваниль', '3кг/30 порций', 243602670, 6600),
        ('Digital Meal Original Ваниль', 'ваниль', '5кг/50 порций', 243606417, 9850),
        ('Digital Meal Original Ваниль', 'ваниль', 'Бутылки 6шт', 346764601, 1710),
        ('Digital Meal Original Ваниль', 'ваниль', 'Бутылки 30шт', 391306253, 7950),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'Пакет/5 порций', 265726303, 1475),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', '4 пакета/20 порций', 265727388, 5600),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', '10 пакетов/50 порций', 265728072, 10800),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', '1,4кг/14 порций', 450053113, 3990),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', '3кг/30 порций', 265728560, 7350),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', '5кг/50 порций', 265728752, 10250),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'Бутылки 6шт', 346761481, 1770),
        ('Digital Meal "Завтрак с Кофе"', 'кофе', 'Бутылки 30шт', 391307638, 8550),
        ('Digital Meal "Starter Kit"', 'микс', ' бутылка', 338585388, 1890),
        ('Digital Meal Original Банан ', 'банан', 'Пакет/5 порций', 1111111110, 1425),
        ('Digital Meal Original Банан ', 'банан', '4 пакета/20 порций', 3333333330, 4900),
        ('Digital Meal Original Банан ', 'банан', '10 пакетов/50 порций', 222222220, 10500),
        ('Digital Meal Original Банан ', 'банан', '1,4кг/14 порций', 504765716, 3710),
        ('Digital Meal Original Банан ', 'банан', '3кг/30 порций', 504768608, 6600),
        ('Digital Meal Original Банан ', 'банан', '5кг/50 порций', 510689914, 1900),
        ('Digital Meal Original Банан ', 'банан', 'Бутылки 6шт', 44444444, 1710),
        ('Digital Meal Original Банан ', 'банан', 'Бутылки 30шт', 55555555, 7950)
    ]

    con = sl.connect('mybot.db')
    with con:
        con.executemany(sql, data)

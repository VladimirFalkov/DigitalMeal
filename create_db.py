from handlers import get_id_insales, get_retail_price
from products_db import create_products_db
# from choice_product_form import first_order_form


def load_id_and_price_to_data(first_order_form):
    id_insales = get_id_insales(
        first_order_form['flavor'],
        first_order_form['package_type']
        )
    price = get_retail_price(
        first_order_form['flavor'],
        first_order_form['package_type']
        )
    print(price, id_insales)
    return id_insales, price

    load_id_and_price_to_data(first_order_form)
    create_products_db()

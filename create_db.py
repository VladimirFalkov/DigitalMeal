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


def confirm_order(first_order_form, username):
    # print(first_order_form)
    id_insales = load_id_to_data(
        first_order_form['flavor'], first_order_form['variant_of_good']
        )
    print(first_order_form['email'], type(first_order_form['email']))
    print(first_order_form['name'], type(first_order_form['name']))
    print(first_order_form['quantity'], type(first_order_form['quantity']))
    print(id_insales, type(id_insales))
    place_order_by_API()
    print(id_insales)

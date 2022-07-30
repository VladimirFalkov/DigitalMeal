from telegram import ParseMode, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from utils import choose_flavor_keyboard, confirm_order_keyboard
from handlers import get_id_insales, get_retail_price
from order import place_order_by_API


def start_choice_goods(update, context):
    update.message.reply_text(
        'Выберите вкус', reply_markup=choose_flavor_keyboard()
    )
    return 'flavor'


def choose_flavor(update, context):
    context.user_data['first_order_form']['flavor'] = update.message.text
    reply_keyboard = [['Пакет', 'Банка', "Бутылка"]]
    update.message.reply_text(
            'Выберите вид упаковки',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
                )
    )
    return 'package_type'


def choose_package(update, context):
    context.user_data['first_order_form']['package_type'] = update.message.text
    if context.user_data['first_order_form']['package_type'] == 'Пакет':
        reply_keyboard = [
            ['Пакет/5 порций', '4 пакета/20 порций', "10 пакетов/50 порций"]
            ]
        update.message.reply_text(
                'Выберите количество пакетов/порций',
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard, one_time_keyboard=True
                    )
        )
        return 'variant_of_good'
    if context.user_data['first_order_form']['package_type'] == 'Банка':
        reply_keyboard = [
            ['1,4кг/14 порций', ' 3кг/30 порций', "5кг/50 порций"]
            ]
        update.message.reply_text(
                'Выберите количество порций',
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard, one_time_keyboard=True
                    )
        )
        return 'variant_of_good'
    else:
        reply_keyboard = [
            ['Бутылки 6шт', 'Бутылки 30шт', "Starter Kit 6 бутылок"]
            ]
        update.message.reply_text(
                'Выберите количество бутылок',
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard, one_time_keyboard=True
                    )
        )
        return 'variant_of_good'


def choose_variant_of_good(update, context):
    context.user_data['first_order_form'][
        'variant_of_good'] = update.message.text
    update.message.reply_text(
        "Введите количество упаковок"
    )
    return 'quantity'


def leave_comment(update, context):
    context.user_data['first_order_form']['quantity'] = int(
        update.message.text
        )
    update.message.reply_text(
        "Если необходимо оставьте комментарий"
    )
    return 'comment'


def choose_quantity(update, context):
    context.user_data['first_order_form']['comment'] = update.message.text
    order_info = order_format_form(
        context.user_data['first_order_form'],
        update.effective_user.first_name
        )
    update.message.reply_text(
        order_info, reply_markup=confirm_order_keyboard(),
        parse_mode=ParseMode.HTML
        )
    return ConversationHandler.END


def load_id_to_data(flavor, package_type):
    id_insales = int(get_id_insales(flavor, package_type))
    return id_insales


def load_price_to_data(flavor, package_type):
    price = int(get_retail_price(flavor, package_type))
    return price


def order_format_form(first_order_form, username):
    # first_order_form = context.user_data['first_order_form']
    id_insales = load_id_to_data(
        first_order_form['flavor'], first_order_form['variant_of_good']
        )
    price = load_price_to_data(
        first_order_form['flavor'], first_order_form['variant_of_good']
        )
    delivery_cost = 390
    order_info = f"""<b>{username}, давайте проверим, итак:</b>
<b>Получатель</b>:  {first_order_form['name']}
<b>Ваш email</b>: {first_order_form['email']}
<b>Ваш телефон</b>: {first_order_form['phone']}
<b>Город достаки</b>: {first_order_form['city']}
<b>Доставка по адрес</b>: {first_order_form['address']}
<b>Ваш выбор</b>: {first_order_form['variant_of_good']} 
<b>Cо вкусом</b>: {first_order_form['flavor']}
<b>Цена выбранных товаров</b>: {price * first_order_form['quantity']}
<b>Цена доставки</b>: {delivery_cost}
<b>ИТОГО с доставкой</b>:{price * first_order_form['quantity'] + delivery_cost}
    """
    print(id_insales)
    # print(first_order_form)
    return order_info


def confirm_order(first_order_form, username):
    place_order_by_API()

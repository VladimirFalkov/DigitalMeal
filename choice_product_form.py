from telegram import ParseMode, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from utils import choose_flavor_keyboard, main_keyboard


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
        return 'quantity'
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
        return 'quantity'
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
        return 'quantity'


def choose_quantity(update, context):
    context.user_data['first_order_form']['quantity'] = update.message.text
    order_info = order_format_form(
        context.user_data['first_order_form'],
        update.effective_user.first_name
        )
    update.message.reply_text(
        order_info, reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )
    return ConversationHandler.END


def order_format_form(first_order_form, username):
    order_info = f"""<b>{username}, давайте проверим, итак:</b>
<b>Заказ на имя</b>:  {first_order_form['name']}
<b>Ваш email</b>: {first_order_form['email']}
<b>Ваш телефон</b>: {first_order_form['phone']}
<b>Ваш адрес</b>: {first_order_form['address']}
<b>Ваш город</b>: {first_order_form['city']}
<b>Ваш выбор</b>: {first_order_form['quantity']} со вкусом {first_order_form['flavor']}
    """
    return order_info

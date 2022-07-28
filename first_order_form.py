from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from choice_product_form import start_choice_goods


def first_order_form_start(update, context):
    update.message.reply_text(
        "Кто будет получать заказ?",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"


def first_order_form_name(update, context):
    customer_name = update.message.text
    context.user_data['first_order_form'] = {'name': customer_name}
    context.user_data['first_order_form']['name'] = update.message.text
    update.message.reply_text(
        "Введите ваш email"
        )
    return 'email'


def first_order_form_email(update, context):
    context.user_data['first_order_form']['email'] = update.message.text
    update.message.reply_text(
        "Введите ваш телефон"
        )
    return 'phone'


def first_order_form_phone(update, context):
    context.user_data['first_order_form']['phone'] = update.message.text
    update.message.reply_text(
        "Введите ваш адрес"
        )
    return 'address'


def first_order_form_address(update, context):
    context.user_data['first_order_form']['address'] = update.message.text
    update.message.reply_text(
        "Введите ваш город"
        )
    return 'city'


def first_order_form_city(update, context):
    context.user_data['first_order_form']['city'] = update.message.text
    start_choice_goods(update, context)
    return ConversationHandler.END

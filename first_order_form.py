from telegram import ParseMode, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard, choose_flavor_keyboard


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


def start_choice_goods(update, context):
    context.user_data['first_order_form']['phone'] = update.message.text
    update.message.reply_text(
        'Выберите вкус', reply_markup=choose_flavor_keyboard()
    )
    return 'flavor'


def first_order_form_phone(update, context):
    context.user_data['first_order_form']['phone'] = update.message.text
    # надо изменить 'phone'] на соовтветсвующее значение
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
    user_text = format_first_order_form(
        context.user_data['first_order_form'],
        update.effective_user.first_name
        )
    update.message.reply_text(
        user_text, reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )
    return ConversationHandler.END


def format_first_order_form(first_order_form, username):
    user_text = f"""<b>{username}, давайте проверим заказ, итак:</b>
<b>Заказ на имя</b>:  {first_order_form['name']}
<b>Ваш email</b>: {first_order_form['email']}
<b>Ваш телефон</b>: {first_order_form['phone']}
<b>Ваш адрес</b>: {first_order_form['address']}
<b>Ваш город</b>: {first_order_form['city']}
    """
    return user_text

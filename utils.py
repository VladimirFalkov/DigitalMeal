from telegram import ReplyKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Сделать Заказ', 'Рассчитать калорийность']
    ])


def start_shop_keyboard():
    return ReplyKeyboardMarkup([
        ['Заказать впервые', 'Повторный заказ']
    ])


def choose_flavor_keyboard():
    return ReplyKeyboardMarkup([
        ['Ваниль', 'Банан', 'Кофе']
    ])


def confirm_order_keyboard():
    return ReplyKeyboardMarkup([
        ['Подтвердить заказ', 'Сделать Заказ']
    ])

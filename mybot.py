import logging
import settings
from form import (
    form_start, form_age, form_gender, form_weight,
    form_activity, form_dontknow
)
from first_order_form import (
    first_order_form_start, first_order_form_name,
    first_order_form_email, first_order_form_phone,
    first_order_form_address, first_order_form_city,
    start_choice_goods
)
from handlers import greet_user, take_order
from telegram.ext import (
    Updater, CommandHandler, MessageHandler,
    Filters, ConversationHandler)

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    first_order_form = ConversationHandler(
        entry_points=[
            MessageHandler(
                Filters.regex('^(Заказать впервые)$'), first_order_form_start
                )

        ],
        states={
            'name': [MessageHandler(Filters.text, first_order_form_name)],
            'email': [MessageHandler(Filters.text, first_order_form_email)],
            'phone': [MessageHandler(Filters.text, start_choice_goods)],
            # заменить функцию на в выборе продукта first_order_form_phone
            'address': [MessageHandler(
                Filters.text, first_order_form_address
                )],
            'city': [MessageHandler(Filters.text, first_order_form_city)]
        },
        fallbacks=[
            MessageHandler(
                Filters.text | Filters.video | Filters.photo |
                Filters.document | Filters.location, form_dontknow
                )
        ]
        )
    dp.add_handler(first_order_form)
    form = ConversationHandler(
        entry_points=[
            MessageHandler(
                Filters.regex('^(Рассчитать калорийность)$'), form_start
                )

        ],
        states={
            'age': [MessageHandler(Filters.text, form_age)],
            'gender': [MessageHandler(
                Filters.regex('^(Жен|Муж)$'), form_gender
                )],
            'weight': [MessageHandler(Filters.text, form_weight)],
            'activity': [MessageHandler(
                Filters.regex(
                    '^(Низкий|Средний|Высокий)$'
                    ), form_activity
                )]
        },
        fallbacks=[
            MessageHandler(
                Filters.text | Filters.video | Filters.photo |
                Filters.document | Filters.location, form_dontknow
                )
        ]
        )
    dp.add_handler(form)
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(
        MessageHandler(Filters.regex('^(Сделать Заказ)$'), take_order)
        )

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

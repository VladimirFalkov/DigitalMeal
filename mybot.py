import logging
import settings
from form import (
    form_start, form_age, form_gender, form_weight,
    form_activity, form_dontknow
)
from first_order_form import (
    first_order_form_start, first_order_form_name,
    first_order_form_email, first_order_form_phone,
    first_order_form_address, first_order_form_city
    
)
from choice_product_form import (
    choose_flavor, choose_package,
    choose_variant_of_good, choose_quantity,
    leave_comment,
    load_id_and_price_to_data
)
from handlers import greet_user, take_order
from telegram.ext import (
    Updater, CommandHandler, MessageHandler,
    Filters, ConversationHandler)

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    choice_product_form = ConversationHandler(
        entry_points=[
            MessageHandler(
                Filters.regex('^(Ваниль|Банан|Завтрак с Кофе)$'), choose_flavor
                )
        ],
        states={
            'package_type': [MessageHandler(
                Filters.regex('^(Пакет|Банка|Бутылка)$'),
                choose_package
                )],
            'variant_of_good': [MessageHandler(
                Filters.regex('^(Пакет/5 порций|4 пакета/20 порций|10 пакетов/50 порций|1,4кг/14 порций|3кг/30 порций|5 кг/50 порций|Бутылки 6шт|Бутылки 30шт|Starter Kit 6 бутылок)$'),
                choose_variant_of_good
                )],
            'quantity': [MessageHandler(
                Filters.text, leave_comment
                )],
            'comment': [MessageHandler(
                Filters.text, choose_quantity, load_id_and_price_to_data
                )],
        },
        fallbacks=[
            MessageHandler(
                Filters.text | Filters.video | Filters.photo |
                Filters.document | Filters.location, form_dontknow
                )
        ]
        )
    dp.add_handler(choice_product_form)
    first_order_form = ConversationHandler(
        entry_points=[
            MessageHandler(
                Filters.regex('^(Заказать впервые)$'), first_order_form_start
                )

        ],
        states={
            'name': [MessageHandler(Filters.text, first_order_form_name)],
            'email': [MessageHandler(Filters.text, first_order_form_email)],
            'phone': [MessageHandler(Filters.text, first_order_form_phone)],
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

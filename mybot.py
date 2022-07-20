import logging
import settings
from form import (
    form_start, form_age, form_gender, form_weight,
    form_activity, form_dontknow

)
from handlers import greet_user
from telegram.ext import (
    Updater, CommandHandler, MessageHandler,
    Filters, ConversationHandler)

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
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

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()

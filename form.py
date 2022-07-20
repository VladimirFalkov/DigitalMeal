from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from handlers import (
    calc_energy, weight_user, count_age, activity_level, calories_at_rest
    )
from utils import main_keyboard


def form_start(update, context):
    update.message.reply_text(
        "Сколько Вам лет?",
        reply_markup=ReplyKeyboardRemove()
    )
    return "age"


def form_age(update, context):
    user_age = update.message.text
    if len(user_age.split()) > 2:
        update.message.reply_text("Введите ваш возраст")
        return 'age'
    else:
        context.user_data['form'] = {'age': user_age}
        context.user_data['form']['user_age_group'] = count_age(int(user_age))
        reply_keyboard = [['Жен', 'Муж']]
        update.message.reply_text(
            'Ваш пол?',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
                )
        )
        return 'gender'


def form_gender(update, context):
    context.user_data['form']['gender'] = update.message.text
    update.message.reply_text(
        "Введите ваш вес"
        )
    return 'weight'


def form_weight(update, context):
    context.user_data['form']['weight'] = update.message.text
    context.user_data['form']['weight_rnd'] = weight_user(update.message.text)
    reply_keyboard = [['Низкий', 'Средний', "Высокий"]]
    update.message.reply_text(
            'Ваш уровень ежедневной физической активности?',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
                )
    )
    return 'activity'


def form_activity(update, context):
    context.user_data['form']['activity'] = update.message.text
    context.user_data['form']['user_act_level'] = (
        activity_level(update.message.text)
        )
    user_text = format_form(
        context.user_data['form'],
        update.effective_user.first_name
        )
    update.message.reply_text(
        user_text, reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML
        )
    return ConversationHandler.END


def format_form(form, username):
    user_rest_cal = calories_at_rest(
        form['gender'], form['user_age_group'], form['weight_rnd']
        )
    user_text = f"""<b>Ваше имя</b>: {username}
<b>Ваш возраст</b>: {form['age']}
<b>Ваш пол</b>: {form['gender']}
<b>Ваш вес</b>: {form['weight']}
<b>Ваш уровень ежедневной физической активности</b>: {form['activity']}
<b>Вы расходуете</b>: {round(calc_energy(
    form['user_act_level'], user_rest_cal), 0
    )} <b>ккал в день</b>
    """
    return user_text


def form_dontknow(update, context):
    update.message.reply_text('Я вас не понимаю! Введите ответ на вопрос выше')

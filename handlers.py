from utils import main_keyboard, start_shop_keyboard
import sqlite3 as sl


def greet_user(update, context):
    print("Вызван /Start")
    username = update.effective_user.first_name
    update.message.reply_text(
        f'Здравствуйте {username}!',
        reply_markup=main_keyboard()
        )


def weight_user(weight, base=5):
    weight_user = base * round(int(weight) / base)
    return weight_user


def count_age(age):
    if 18 <= int(age) <= 29:
        age_range = '18-29'
    if 30 <= int(age) <= 39:
        age_range = '30-39'
    if 40 <= int(age) <= 59:
        age_range = '40-59'
    if 60 <= int(age) <= 85:
        age_range = '60+'
    return age_range


def activity_level(activity):
    if activity == 'Низкий':
        ratio_activity = 1.4
    if activity == 'Средний':
        ratio_activity = 1.6
    if activity == 'Высокий':
        ratio_activity = 1.9
    return ratio_activity


def calories_at_rest(gender, age, weight):
    con = sl.connect('mybot.db')
    cursor = con.cursor()
    sql = 'SELECT ccal FROM CALORY WHERE gender=? AND age=? AND weight=?'
    cursor.execute(sql, (gender, age, weight))
    result = cursor.fetchone()[0]
    print(result)
    return result


def calc_energy(ratio_activity, calories_at_rest):
    calories_total = ratio_activity * calories_at_rest
    return calories_total


def take_order(update, context):
    username = update.effective_user.first_name
    update.message.reply_text(
        f'Давайте закажем {username}!',
        reply_markup=start_shop_keyboard()
        )

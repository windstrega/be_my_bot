from datetime import datetime
from random import choice
import ephem
from glob import glob

from utils import get_smile, play_random_numbers, main_keyboard

def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Наконец-то ты пришёл {context.user_data['emoji']}!",
        reply_markup=main_keyboard
    )

def planet_info(update, context):
    planetnameinput = update.message.text.split(' ')[1]
    if planetnameinput == "Mars":
        planet = ephem.Mars(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    elif planetnameinput == "Mercury":
        planet = ephem.Mercury(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    elif planetnameinput == "Venus":
        planet = ephem.Venus(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    elif planetnameinput == "Jupiter":
        planet = ephem.Jupiter(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    elif planetnameinput == "Saturn":
        planet = ephem.Saturn(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    elif planetnameinput == "Uranus":
        planet = ephem.Uranus(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    elif planetnameinput == "Neptune":
        planet = ephem.Neptune(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    elif planetnameinput == "Earth":
        planet = ephem.Earth(datetime.today())
        update.message.reply_text(ephem.constellation(planet), reply_markup=main_keyboard())
    else:
        update.message.reply_text("Такой планеты нет", reply_markup=main_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup=main_keyboard())

def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    update.message.reply_text(message, reply_markup=main_keyboard())

def send_cat_picture(update, context):
    cat_photo_list = glob('images/cat*.jp*g')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'), reply_markup=main_keyboard())

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )
from emoji import emojize
from datetime import datetime
import ephem
from glob import glob
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice, randint

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Наконец-то ты пришёл {context.user_data['emoji']}!")



def planet_info(update, context):
    planetnameinput = update.message.text.split(' ')[1]
    if planetnameinput == "Mars":
        planet = ephem.Mars(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif planetnameinput == "Mercury":
        planet = ephem.Mercury(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif planetnameinput == "Venus":
        planet = ephem.Venus(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif planetnameinput == "Jupiter":
        planet = ephem.Jupiter(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif planetnameinput == "Saturn":
        planet = ephem.Saturn(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif planetnameinput == "Uranus":
        planet = ephem.Uranus(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif planetnameinput == "Neptune":
        planet = ephem.Neptune(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    elif planetnameinput == "Earth":
        planet = ephem.Earth(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
    else:
        update.message.reply_text("Такой планеты нет")



def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}")

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, моё {bot_number}, вы выиграли'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, моё {bot_number}, ничья'
    else:
        message = f'Ваше число {user_number}, моё {bot_number}, вы проиграли'
    return message

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
    update.message.reply_text(message)

def send_cat_picture(update, context):
    cat_photo_list = glob('images/cat*.jp*g')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'))
 

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

import json
import telebot
from telebot import types
token = '7114588324:AAHCQJyS7t8FfvVb-mSd-vdc4CSfZSW5IVY'
bot = telebot.TeleBot(token)


active_department = ''

@bot.message_handler(content_types=['text'])


def get_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, text='Добро пожаловать! Это бот для ответсвенного человека, который может добавлять других людей  ')



















































bot.polling(none_stop=True, interval=0)
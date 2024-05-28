import json
import telebot
from telebot import types
token = '7123532905:AAHCw-orSkIET0JSmSqPgNHb3rgtwXhGKtA'
bot = telebot.TeleBot(token)

active_department = ''

@bot.message_handler(content_types=['text'])

def get_message(message):
    if message.text == '/start':

        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'Запуск бота'),
                types.BotCommand('/dance', 'Получить танец'),
                types.BotCommand('/bomb', 'Не нажимать')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )

        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Кислородно-газовый', callback_data='Кислородно-газовый')
        button2 = types.InlineKeyboardButton(text='АСУТП', callback_data='АСУТП')
        button3 = types.InlineKeyboardButton(text='Колесобандажный', callback_data='Колесобандажный')
        button4 = types.InlineKeyboardButton(text='Конверторный', callback_data='Конверторный')
        button5 = types.InlineKeyboardButton(text='УЖДТ', callback_data='УЖДТ')

        keyboard.add(button1, button2, button3, button4, button5)

        bot.send_message(message.from_user.id, text='Добро пожаловать!')
        bot.send_message(message.from_user.id, text='Выберите цех, из которого вы хотите получить данные с датчиков', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global active_department
    if call.data == 'Кислородно-газовый':
        active_department = 'Кислородно-газовый'
        keyboard = types.InlineKeyboardMarkup()
        button1_2 = types.InlineKeyboardButton(text='Посмотреть всю информацию по цеху', callback_data='Посмотреть всю информацию по цеху')
        button1_3 = types.InlineKeyboardButton(text='Посмотреть показания по дате', callback_data='Посмотреть показания по дате')
        keyboard.add(button1_2, button1_3)
        bot.send_message(call.from_user.id, text='Выберите как вы хотите получить информацию', reply_markup=keyboard)
    if call.data == 'Посмотреть всю информацию по цеху':
        file = open('датчик.json', 'r', encoding='utf-8')
        conditions = json.load(file)
        file.close()
        for condition in conditions:
            if condition['department'] == active_department:
                text = '\nНазвание цеха:' + condition['department'] + '\n'
                text += 'Лента:' + condition['lenta'] + '\n'
                text += 'Датчик: ' + condition['datchik'] + '\n'
                text += 'Дата: ' + condition['date'] + '\n'
                text += 'Показатели: ' + str(condition['value']) + '\n'
                bot.send_message(call.from_user.id, text=text)
    elif call.data == 'Посмотреть показания по дате':
        bot.send_message(call.from_user.id, text='Введите дату г-м-д')
        file = open('датчик.json', 'r', encoding='utf-8')
        conditions = json.load(file)
        file.close()
        for condition in conditions:
            if condition['department'] == active_department:
                text = '\nНазвание цеха:' + condition['department'] + '\n'
                text += 'Лента:' + condition['lenta'] + '\n'
                text += 'Датчик: ' + condition['datchik'] + '\n'
                text += 'Дата: ' + condition['date'] + '\n'
                text += 'Показатели: ' + str(condition['value']) + '\n'
                bot.send_message(call.from_user.id, text=text)





bot.polling(none_stop=True, interval=0)
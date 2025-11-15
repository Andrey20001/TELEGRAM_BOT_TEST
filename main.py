import telebot, os, requests, random

bot = telebot.TeleBot("СВОЙ ТОКЕН")

@bot.message_handler(commands=['start'])
def send_mess(message):
    bot.send_message(message.chat.id, "Привет! Я бот который умеет сортировать мусор по контейнерам и показывать еще цвет контейнера! Например - напиши  просто пластик и я скажу цвет контейнера!")


@bot.message_handler(commands=['пластик'])
def send_hello_e(message):
    hello = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "Пластик кладут в ЖЕЛТЫЙ контейнер! Это 1 контейнер!")
    with open('image/k1.png', 'rb') as img:
        bot.send_photo(message.chat.id, img)


@bot.message_handler(commands=['пищевые_отходы'])
def send_hello_e(message):
    hello = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "Пищевые отходы кладут в КОРИЧНЕВЫЙ контейнер! Это 2 контейнер!")
    with open('image/k3.png', 'rb') as img:
        bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['стекло'])
def send_hello_e(message):
    hello = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "Стекло кладут в ЗЕЛЕНЫЙ контейнер! Это 3 контейнер!")
    with open('image/k2.png', 'rb') as img:
        bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['опасные_отходы'])
def send_hello_e(message):
    hello = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "Опасные отходы например батарейки кладут в КРАСНЫЙ контейнер! Это 4 контейнер!")
    with open('image/k4.png', 'rb') as img:
        bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['бумага'])
def send_hello_e(message):
    hello = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "Бумагу кладут в СИНИЙ контейнер! И это последний 5 контейнер!")
    with open('image/k5.png', 'rb') as img:
        bot.send_photo(message.chat.id, img)

bot.polling()

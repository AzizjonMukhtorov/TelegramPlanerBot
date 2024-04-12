import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot('7084012680:AAFmGV4MV0Zq7gugBC5yLSu6ID8obWS12fI')
image = ''
@bot.message_handler(commands=['start'])
def introduction(message):
    global image
    if datetime.now() > datetime(2024, 3, 10):
        image = "photo_2024-03-06_13-25-38.jpg"
        file = open('images/' + image, 'rb')
        bot.send_message(message.chat.id, file)
        bot.send_message(message.chat.id, "Happy Ramadan")
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn_yes = types.KeyboardButton("Да. Хочу узнать цену")
        btn_no = types.KeyboardButton("Нет. Дайте больше информации")
        btn_back = types.KeyboardButton("Назад")
        murkup.row(btn_yes, btn_no)
        murkup.row(btn_back)
        bot.send_message(message.chat.id, "У вас есть информация о нашем продукте?", reply_markup=murkup)
    else:
        image = "photo_2024-03-06_13-25-41.jpg"
        file = open('images/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, "🌙 Проведите Рамадан эффективно вместе с лимитированными планерами Ramadan 2024 от Today Plan")
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn_yes = types.KeyboardButton("Да. Хочу узнать цену")
        btn_no = types.KeyboardButton("Нет. Дайте больше информации")
        btn_back = types.KeyboardButton("Назад")
        murkup.row(btn_yes, btn_no)
        murkup.row(btn_back)
        bot.send_message(message.chat.id, "У вас есть информация о нашем продукте?", reply_markup=murkup)

@bot.message_handler(func = lambda message: message.text == "Да. Хочу узнать цену")
def handle_price(message):
    price(message)

@bot.message_handler(func = lambda message: message.text == "Нет. Дайте больше информации")
def handle_more_information(message):
    more_information(message) 

@bot.message_handler(func = lambda message: message.text == "Какие расцветки имеются?")
def handle_color(message):
    color(message)

@bot.message_handler(func = lambda message: message.text == "Красный цвет")
def handle_color_red(message):
    color_red(message)
   

@bot.message_handler(func = lambda message: message.text == "Синий цвет")
def handle_color_blue(message):
    color_blue(message)

@bot.message_handler(func = lambda message: message.text == "Начать сначала")
def handle_color_blue   (message):
    introduction(message)

@bot.message_handler(func = lambda message: message.text == "Спасибо за информацию")
def hendle_thanks_for(message):
    thanks_for(message)

@bot.message_handler(func = lambda message: message.text == "Что оно содержит?")
def hendle_it_has(message):
    it_has(message)


def price(message):
    global image
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_book = types.KeyboardButton("Заказать сейчас")
    btn_thanks = types.KeyboardButton("Спасибо за информацию")
    btn_back = types.KeyboardButton("Назад")
    markup.row(btn_book, btn_thanks)
    markup.row(btn_back)
    bot.send_message(message.chat.id, "Sorryyyyy.....", reply_markup=markup)

def more_information(message):
    global image
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_have = types.KeyboardButton("Что оно содержит?")
    btn_color = types.KeyboardButton("Какие расцветки имеются?")
    btn_back = types.KeyboardButton("Назад")
    markup.row(btn_have, btn_color)
    markup.row(btn_back)
    image = "09_15_02_todayplan00196 копия s.jpg"
    file = open('./images/' + image, 'rb')
    bot.send_photo(message.chat.id, file)  
    bot.send_message(message.chat.id, """Что такое планер?

Планер Ramadan 2024 - ежедневник, выпущенный специально под самый важный месяц для всех мусульман. 

Ramadan 2024 - ограниченная серия, всего 10000 эксклюзивных планеров. Планер поможет вам оставаться сфокусированными в течение всего месяца. 

Планировщик содержит несколько важных разделов: постановка главных целей на месяц, планирование 30 дней в разрезе календаря, план на каждый день и подведение итогов месяца.
                         """, reply_markup=markup)
        
def color(message):
    global image
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_red = types.KeyboardButton("Красный цвет")
    btn_blue = types.KeyboardButton("Синий цвет")
    btn_back = types.KeyboardButton("Назад")
    markup.row(btn_red, btn_blue)
    markup.row(btn_back)
    image = "images/07_15_02_todayplan00173 копия s.jpg"
    file = open("./" + image, "rb")
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, "Который цвет вы хотите посмотреть? ", reply_markup=markup)

def color_red(message):
    global image
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_book = types.KeyboardButton("Заказать сейчас")
    btn_thanks = types.KeyboardButton("Спасибо за информацию")
    btn_back = types.KeyboardButton("Назад")
    markup.row(btn_book, btn_thanks)
    markup.row(btn_back)
    image = "03_15_02_todayplan00066 копия s.jpg"
    file = open('./images/red_photo/' + image, 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, "Красный цвет")

def color_blue(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_book = types.KeyboardButton("Заказать сейчас")
    btn_thanks = types.KeyboardButton("Спасибо за информацию")
    btn_back = types.KeyboardButton("Назад")
    markup.row(btn_book, btn_thanks)
    markup.row(btn_back)
    image = "blue_photo/04_15_02_todayplan00062 копия s.jpg"
    file = open('./images/' + image, 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, "Синий цвет")

def thanks_for(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_start = types.KeyboardButton("Начать сначала")
    markup.row(btn_start)
    bot.send_message(message.chat.id, "Рады были Вам помочь. Надеюсь Вы подумаете и закажите ☺️", reply_markup=markup)

def it_has(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_color = types.KeyboardButton("Какие расцветки имеются?")
    btn_back = types.KeyboardButton("Назад")
    markup.row(btn_color, btn_back)
    bot.send_message(message.chat.id, """До Рамадана осталось совсем немного,и если вы хотите провести этот Священный месяц с пользой и продуктивно то постарайтесь выполнить эти 5 пунктов ⬇️🤍

1. Составьте план действий.
                     
Планирование - это ключ к продуктивности.
Если вы желаете провести Рамадан максимально успешно, то составьте цели и план действий.
В этом вам поможет невероятный планнер от @today.plan
С аятами из Корана 💔

2. Совершите покаяние.

Аллах Милосердный и Прощающий, потому никогда не сомневайтесь в его щедрости и совершайте покаяния.
Перед наступлением этого прекрасного месяца, будет хорошо начать его с покоем в душе и сердце.

3 Подготовь свое тело.

Старайтесь перед Рамаданом и на протяжении его, насыщать свое тело полезными витаминами и микроэлементами.
Откажитесь от вредной, жареной, жирной и соленой еды. Выпивайте норму воды.

4. Подкрепите свои знания.
Смотрите видео-лекции, читайте статьи и книги, дабы провести Рамадан с наибольшей пользой, и получить больше вознаграждения за держание поста и совершение благих дел.

5. Правильное намерение.
И самое главное, поставьте искреннее намерение провести этот месяц Рамадан продуктивно ради довольства Всевышнего Аллаха!
""", reply_markup=markup)


bot.infinity_polling()

#Happy to help you. Hope you think and book

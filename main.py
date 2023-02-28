import telebot
import os
import random
bot = telebot.TeleBot("6260578840:AAF8IvgYmk2fMYBt3wHBC3Zzg_0v-XLiSKg")
def send_photo(chat_id, photo, markup):
    with open(photo, 'rb') as f:
        bot.send_photo(chat_id, f, reply_markup=markup)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot = telebot.TeleBot("6260578840:AAF8IvgYmk2fMYBt3wHBC3Zzg_0v-XLiSKg")
    btn1 = telebot.types.KeyboardButton('Зашквар 18+')
    btn2 = telebot.types.KeyboardButton('Жизненные ситуации')
    btn3 = telebot.types.KeyboardButton('Семейная жиза')
    btn4 = telebot.types.KeyboardButton('Школьный движ')
    btn6 = telebot.types.KeyboardButton('📖Правила')
    chat_id = message.chat.id
    text = message.text
    if text == '/start':
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        markup.add(btn6)
        bot.send_message(chat_id, 'Еееееее!🥳 Ознакомься с правилами, выбирай понравившийся раздел и скорее начинай!!!', reply_markup=markup)
    elif text == '📖Правила':
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn6)
        bot.send_message(chat_id, 'Коротко: Один игрок озвучивает ситуацию из колоды, '
                                          'другие выдают самый ржачный и подходящий к ней мем. '
                                          'Побеждает автор самой смешной связки. До начала игры '
                                          'каждый игрок берёт из колоды с мемами по 5 карточек. '
                                          'Колода с ситуациями выкладывается на середину стола. Участники '
                                          'определяют судью на первый раунд любым способом. Судья выбирает из '
                                          'колоды ситуаций карточку, которую хочет разыграть в этом раунде, озвучивает '
                                          'и кладёт на середину стола. Игроки подбирают и выкладывают наиболее смешной '
                                          'мем к данной ситуации. За один раунд можно использовать только один мем. '
                                          'Судья выбирает наиболее смешную связку и отдаёт ее автору карточку с ситуацией, '
                                          'таким образом считаются очки. Все берут из колоды по одному новому мему, а игрок '
                                          'слева от судьи становится судьей в следующем раунде.', reply_markup=markup)

    elif text in ('Зашквар 18+', 'Жизненные ситуации', 'Семейная жиза', 'Школьный движ'):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        photo_dir = os.path.join(os.getcwd(), text)
        photos = os.listdir(photo_dir)
        photo = os.path.join(photo_dir, random.choice(photos))
        send_photo(chat_id, photo, markup)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        markup.add(btn1, btn2, btn3, btn4, btn6)
    else:
        bot.send_message(chat_id, 'Неизвестная команда')
bot.polling(none_stop=True)
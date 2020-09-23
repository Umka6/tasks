import telebot

bot = telebot.TeleBot('1148924698:AAEscEKThvc3SLVdqohMdITISRgr5ZqsW_c')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_message(message):
  if message.text == 'Привет':
    bot.send_message(message.chat.id, 'Привет beatiful girl')
  elif message.text.lower() == 'пока':
    bot.send_message(message.chat.id, 'Прощай создатель')
  elif message.text.lower() == 'good day':
      bot.send_message(message.chat.id, 'thank you')
  elif message.text == 'Ты красотка':
      bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMkX0Dgn9tYtPz4V5ate_LWEx7EkJ4AAmEHAAL9eyQAAWaYLBsXaKvGGwQ')
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

#@bot.message_handler(content_types=['text'])
#def send_text(message):
#    if message.text.lower() == 'привет':
#        bot.send_message(message.chat.id, 'Привет, мой создатель')
#    elif message.text.lower() == 'пока':
 #       bot.send_message(message.chat.id, 'Прощай, создатель')
 #   elif message.text.lower() == 'хай':
 #       bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDFV8_wMJ--2k7VjLIWOWB5Q12ne4xAAKBEQACPLPFB0bAzHDYX3P9GwQ')

#@bot.message_handler(content_types=['sticker'])
#def sticker_id(message):
 #   print(message)

bot.polling()
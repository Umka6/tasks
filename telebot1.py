import telebot

bot = telebot.TeleBot('1344039009:AAFD6_y_lejW8Xc4LflBxP-U24dXr--JpbE')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,спасибо что запустил меня')


bot.polling()

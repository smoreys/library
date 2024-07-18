import telebot

bot = telebot.TeleBot('6994566645:AAHFzM37MT_gca9sRXnIBA9A95oLrXKl1wM')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'Nice, but library is empty')

bot.infinity_polling()

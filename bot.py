import telebot
import sities_methods

telegram_bot_key = "5727998641:AAGmixf7PBRDZ3nStxTQJx30PzP8e4BGZiA"
bot = telebot.TeleBot(telegram_bot_key)


@bot.message_handler(content_types=['text'])
def action(message):
    if message.text == '/start':
        sities_methods.create_session(message.from_user.id)
        bot.send_message(message.from_user.id, "Welcome to game, Boiii")

bot.polling()

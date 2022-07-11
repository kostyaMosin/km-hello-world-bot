import telebot
from decouple import config


TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "Hello, how can I help you?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Say, hello!")
    else:
        bot.send_message(message.from_user.id, "I dont understand you! Use /help cmd.")


bot.polling(none_stop=True, interval=0)

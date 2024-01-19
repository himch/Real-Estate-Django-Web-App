import logging
import telebot

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

token = '6853852285:AAGX3xriBMkiUYbszsVWtd196UTWthE5tV4'
service_channel_id = -1002128970552
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def send(message):
    print('1')
    bot.send_message(chat_id=service_channel_id, text='example')
    pass


bot.polling()

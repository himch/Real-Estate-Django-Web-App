import logging
import telebot
from datetime import datetime
from django.utils import timezone


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

token = '6853852285:AAGX3xriBMkiUYbszsVWtd196UTWthE5tV4'
service_channel_id = -1002128970552
bot = telebot.TeleBot(token)


def send_message_to_telegram_service_channel(text):
    bot.send_message(chat_id=service_channel_id, text=text, parse_mode="HTML")


# @bot.message_handler(content_types=['text'])
# def send(message):
#     bot.send_message(chat_id=service_channel_id, text='example')
#     pass


# bot.polling()
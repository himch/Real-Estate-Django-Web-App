import logging
import traceback

import telebot
from datetime import datetime
from django.utils import timezone
from pytils.translit import slugify
from uuid import uuid4


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


def say_my_name():
    stack = traceback.extract_stack()
    text = 'Исполняется функция {}'.format(stack[-2][2])
    # print(text)
    logging.info(text)


def unique_slugify(instance, slug):
    """
    Генератор уникальных SLUG для моделей, в случае существования такого SLUG.
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug

import aiohttp
import traceback
import logging


class Loader:
    url = None

    def __init__(self, url):
        self.url = url

    async def request_content(self):
        say_my_name()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.url) as response:
                    print('Database response.status =', response.status)
                    text = await response.text(encoding="utf-8")
                    return text
            except Exception as e:
                print("Error: " + str(e))
                return None


def say_my_name():
    stack = traceback.extract_stack()
    logging.info('Исполняется функция {}'.format(stack[-2][2]))


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
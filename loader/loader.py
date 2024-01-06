import aiohttp


class Loader:
    url = None

    def __init__(self, url):
        self.url = url

    async def request_content(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                print('Database response.status =', response.status)
                text = await response.text(encoding="utf-8")
                return text



import asyncio
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

from load_alnair_realty import DatabaseDownloader


class TooManyTriesException(BaseException):
    pass


def tries(times):
    def func_wrapper(f):
        async def wrapper(*args, **kwargs):
            for time in range(times):
                print('times:', time + 1)
                # noinspection PyBroadException
                try:
                    return await f(*args, **kwargs)
                except Exception as e:
                    print(str(e))
            raise TooManyTriesException()

        return wrapper

    return func_wrapper



class Parser:
    locales = ('ar', 'ru', 'en')

    def __init__(self):
        self.parsed_data = None

    async def airbnb_parse(self, url):
        async def wait(page, moves=100):
            for i in range(100):
                await page.mouse.wheel(0, 10)
                await page.wait_for_timeout(30)

        @tries(times=3)
        async def get_info_from_main_page():
            sep_locales = {'en': ' in ', 'ar': 'في', 'ru': ','}
            print('start parse airbnb main_page')
            async with async_playwright() as playwright:
                browser = await playwright.chromium.launch()
                page = await browser.new_page()
                await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
                title = dict()
                address_text = dict()
                overview = dict()
                address = dict()
                for locale in self.locales:
                    locale_url = base_url + f'?locale={locale}'
                    print(locale_url)
                    await page.goto(locale_url, timeout=60000)
                    await wait(page, 50)
                    title[locale] = await page.locator('span._1xxgv6l').inner_text()
                    overview_text = await page.locator('//div[@data-section-id="OVERVIEW_DEFAULT_V2"]').inner_text()
                address_text[locale], overview[locale] = overview_text.split('\n')[:2]
                items = address_text[locale].split(sep_locales[locale])
                if len(items) > 1:
                    address[locale] = ' '.join(items[1:])
                else:
                    address[locale] = address_text[locale]
                price_text = await page.locator('span._tyxjp1').first.inner_text()
                await browser.close()

                price_text = price_text.split('&')[0].strip()
                price = price_text[:-1].replace(',', '')
                currency = price_text[-1]
                currencies = {'₽': 'RUB', '$': 'USD', '€': 'EUR'}
                price_a_currency = currencies[currency]

                res = [(f'title_a_{locale}', 'CHAR', title[locale]) for locale in self.locales]

                return [('price_a_currency', 'CHAR', price_a_currency),
                        ('price_a_min', 'REAL', float(price)),
                        ('price_a_max', 'REAL', float(price)),
                        ('listing_districts', 'LIST', json.dumps([address['en'], ])),
                        ('address', 'CHAR', address['en']),
                        ('overview', 'CHAR', overview['en'])] + res

        @tries(times=3)
        async def get_description():
            print('start parse airbnb description')
            async with async_playwright() as playwright:
                browser = await playwright.chromium.launch()
                page = await browser.new_page()
                await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
                description_text = dict()
                for locale in self.locales:
                    locale_url = f"{base_url}?modal=DESCRIPTION&locale={locale}"
                    print(locale_url)
                    await page.goto(locale_url, timeout=60000)
                    await wait(page, 25)
                    description_text[locale]: str = await page.locator(
                        '//div[@data-section-id="DESCRIPTION_MODAL"]').inner_text()
                    description_text[locale] = '\n'.join(description_text[locale].split('\n')[1:])
                await browser.close()
            return [(f'description_a_{locale}', 'CHAR', description_text[locale]) for locale in self.locales]

        @tries(times=3)
        async def get_amenities():
            # locators = {'en': 'div._1seuw5go', 'ar': 'div._17itzz4', 'ru': 'div._1seuw5go'}
            locators = {'en': 'div._njm7bck', 'ar': 'div._1sbso6hm', 'ru': 'div._njm7bck'}
            print('start parse airbnb amenities')
            async with async_playwright() as playwright:
                browser = await playwright.chromium.launch()
                page = await browser.new_page()
                await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
                amenities_list = {locale: [] for locale in self.locales}
                for locale in self.locales:
                    locale_url = f"{base_url}/amenities?locale={locale}"
                    print(locale_url)
                    await page.goto(locale_url, timeout=60000)
                    await wait(page)
                    html = await page.locator(locators[locale]).inner_html()
                    soup = BeautifulSoup(html, "html.parser")
                    amenities_groups = soup.findAll("div", {"class": "_11jhslp"})
                    for group in amenities_groups:
                        group_name = group.findAll("div", {"class": "_87jbxlz"})[0].text
                        if group_name not in ('Not included', 'غير مُدرج', 'Не включено'):
                            lis_amenities = group.findAll('li')
                            for li in lis_amenities:
                                amenity = li.findAll("div", {"class": "twad414"})[0].text
                                if locale == 'en':
                                    svg = str(li.findAll('svg')[0]).replace('"', "'")
                                    amenities_list[locale].append(
                                        {locale: f'{group_name} - {amenity}', 'amenity_svg': svg})
                                else:
                                    amenities_list[locale].append({locale: f'{group_name} - {amenity}'})
                    print(amenities_list)
                await browser.close()
                for i, item in enumerate(amenities_list['en']):
                    item['ru'] = amenities_list['ru'][i]['ru']
                    item['ar'] = amenities_list['ar'][i]['ar']

                amenities = json.dumps(amenities_list['en'])
            return [('listing_amenities', 'CHAR', amenities), ]

        @tries(times=3)
        async def get_photos():
            print('start parse airbnb photos')
            async with async_playwright() as playwright:
                browser = await playwright.chromium.launch()
                page = await browser.new_page()
                await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
                locale_url = f"{base_url}?modal=PHOTO_TOUR_SCROLLABLE&locale=en"
                print(locale_url)
                await page.goto(locale_url, timeout=60000)
                await wait(page)
                html: str = await page.locator('//div[@data-section-id="PHOTO_TOUR_SCROLLABLE_MODAL"]').inner_html()
                await browser.close()
                soup = BeautifulSoup(html, "html.parser")
                images_list = [image['src'] for image in soup.findAll('img') if image.has_attr('src')]
                if images_list:
                    photo = images_list[0]
                    images = json.dumps(images_list[1:])
                return [('listing_album', 'LIST', images),
                        ('photo', 'CHAR', photo)]

        url_parts = url.split('?')
        base_url = url_parts[0]

        result1 = await get_info_from_main_page()
        result2 = await get_description()
        result3 = await get_amenities()
        result4 = await get_photos()
        result = result1 + result2 + result3 + result4

        # tasks = list()
        # tasks.append(asyncio.create_task(get_info_from_main_page()))
        # tasks.append(asyncio.create_task(get_description()))
        # results = await asyncio.gather(*tasks)
        # result = sum(results, [])
        #
        # tasks = list()
        # tasks.append(asyncio.create_task(get_amenities()))
        # tasks.append(asyncio.create_task(get_photos()))
        # results = await asyncio.gather(*tasks)
        # result = sum(results, result)

        now = datetime.now()
        date_time = now.strftime("%Y-%m-%dT%H:%M:%S+04:00")
        """2024-01-07T13:20:59+04:00"""
        result.extend([('url', 'CHAR', base_url),
                       ('complex_id', 'CHAR', base_url.split('/')[-1]),
                       ('updated_at', 'CHAR', date_time)])

        self.parsed_data = result
        # print(*result, sep='\n')
        return result


class AirbnbDownloader(DatabaseDownloader):
    async def insert_record_python(self, record, table_name=DatabaseDownloader.TOP_TABLE_NAME):
        if record:
            k = '"' * 3
            parameters = []
            for field, field_type, item in record:
                if field_type == 'INT':
                    parameters.append(f'{field}={int(item)}')
                elif field_type == 'REAL':
                    parameters.append(f'{field}={float(item)}')
                elif field_type == 'CHAR':
                    if item is None:
                        parameters.append(f'{field}=None')
                    else:
                        parameters.append(f"{field}='''{k + item + k}'''")
                elif field_type == 'LIST':
                    if item is None:
                        parameters.append(f'{field}=None')
                    else:
                        parameters.append(f"{field}='''{k + item + k}'''")
            with open("airbnb_add_record_template.py", "r", encoding='utf-8') as file:
                code = file.read()
                command = 'code.format(' + ', '.join(parameters) + ')'
                code_for_exec = eval(command, globals(), locals())
                with open("airbnb_add_record.py", "w", encoding='utf-8') as f:
                    f.write(code_for_exec.encode('utf-8', 'replace').decode())
                os.system('python airbnb_add_record.py')


@tries(times=3)
async def airbnb_parse(url):
    parser = Parser()
    result = await parser.airbnb_parse(url)
    print(*result, sep='\n')
    print()
    abnb_loader = AirbnbDownloader()
    await abnb_loader.insert_record_python(result)


if __name__ == "__main__":
    # test_url = 'https://www.airbnb.ru/rooms/1025839257800387103?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701086285_it%2FJbRJ34KuI0qDR&enable_auto_translate=false'
    # asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/924282872362443647?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701087118_E8voa32ofmwdeDAd'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/52959323?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701087610_0TJGArZ2qEi/c9E8'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/1025894438402820962?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701087852_RkL1fWkZSDCqksF6'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/1028813054044084583?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701088117_OFUYRInvX4AoX9+M'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/1023727217442279350?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701088383_fpTiQBz9xVgk66lr&translate_ugc=false'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/894042852527152940?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701089251_S9z3INTrMDsUesV9&translate_ugc=true'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/957924904929258926?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701089670_C/wDtUFsIdP4olYa'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/965255156287767882?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701089896_iQpnrVJIouqTCMsc'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/923063187704862404?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701090317_9iTr6L67uVTRQ5B0&translate_ugc=false'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/923052826211233835?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701090562_a9O5OMQLcGwxRLa0&translate_ugc=false'
    asyncio.run(airbnb_parse(test_url))
    test_url = 'https://www.airbnb.ru/rooms/52660644?_set_bev_on_new_domain=1701086284_MzEyZWFhMTQxYTZi&source_impression_id=p3_1701090860_slSQpL+HsLwtqKnl'
    asyncio.run(airbnb_parse(test_url))

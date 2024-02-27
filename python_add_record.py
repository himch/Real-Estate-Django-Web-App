import os
from random import choice
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
import django
django.setup()
from listings.models import Listing
from realtors.models import Realtor
from developers.models import Developer
from loader.get_developer import developer_get_or_add
realtor_list = Realtor.objects.all()
realtors_ids = [realtor.id for realtor in realtor_list]
listings = Listing.objects.filter(complex_id=898)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-27T12:17:41+04:00':
        print('exist with the same updated_at')
        quit()
    print('exist with different updated_at')
else:
    listing = Listing()
listing.is_fully_loaded = False
listing.source = 'alnair'
listing.offer_type = 'sell'
listing.realtor_id = choice(realtors_ids)
print('go')
listing.complex_id = 898
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/6/0f/cd/0fcd556758df27fc4cb8c145e1ecb8d4.png"""
listing.photo = """https://files.alnair.ae/uploads/2023/6/33/db/33dbfa6ddddaaec927559ba45624fed5.png"""
listing.title_a_ru = """Luma21"""
listing.title_a_en = """Luma21"""
listing.title_a_ar = """لوما21"""
listing.description_a_ru = """<p>Luma21 – новый малоэтажный жилой комплекс, который строится в семейно-ориентированном комьюнити Jumeirah Village Circle (JVC), в окружении развитой инфраструктуры, а также рядом с культовыми достопримечательностями Дубая. Проект реализует девелопер из ОАЭ TownX Development. Сдача комплекса в эксплуатацию запланирована на второй квартал 2023 года.</p>"""
listing.description_a_en = """<p>Luma21 is a new low–rise residential complex, which is being built in the family-oriented community Jumeirah Village Circle (JVC), surrounded by developed infrastructure, as well as near the iconic sights of Dubai. The project is being implemented by a developer from the UAE Town Development. The commissioning of the complex is scheduled for the second quarter of 2023.</p>"""
listing.description_a_ar = """<p>سرداب+ارضي+4+سطح+سطح علوي بناية سكنية</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Завершено"""
listing.status_a_en = """Completed"""
listing.status_a_ar = """منتهى"""
listing.construction_start_at = """2021-07-25T12:17:40+04:00"""
listing.construction_progress = 100.0
listing.planned_completion_at = """2023-04-30T12:17:40+04:00"""
listing.predicted_completion_at = """2023-04-30T12:17:40+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Детская игровая площадка", "en": "Kids Play Area", "ar": "منطقة لعب الأطفال"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """TownX"""
listing.developer_a_title_a_en = """TownX"""
listing.developer_a_title_a_ar = """تاون إكس"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/3/b0/80/b0805aa6d83185e3289e7d6b7b6a445f.jpg"""
listing.listing_districts = """["Al Barsha South Fourth", "Jumeirah Village Circle (JVC)"]"""
listing.address = """Dubai, Jumeirah Village Circle, Luma21"""
listing.latitude = 25.05081252
listing.longitude = 55.20503752
listing.listing_album = """["https://files.alnair.ae/uploads/2023/6/2c/17/2c179366b77264dbecd9929b6c77e87a.png", "https://files.alnair.ae/uploads/2023/6/7b/ab/7bab75e99871c75c41f61f993232d716.png", "https://files.alnair.ae/uploads/2023/6/bb/83/bb830713b4d91bdc6b92b13ff5d47b3c.png"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/6/a1/5b/a15b5b8cc4065f7d01d77a8ab679a7b8.png", "https://files.alnair.ae/uploads/2023/6/04/73/047304d25a6b8b30392575d1e1cf9e95.png", "https://files.alnair.ae/uploads/2023/6/ec/94/ec94d25478107f2a145cab45735bcfa2.png", "https://files.alnair.ae/uploads/2023/6/1b/ff/1bff8070d6bcb1ee3164b122e39d1392.png", "https://files.alnair.ae/uploads/2023/6/95/c0/95c093213edf4e5d83dda6bcdd14ccc4.png"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 0
listing.price_a_min = None
listing.price_a_max = None
listing.price_a_currency = """AED"""
listing.listing_br_prices = None
listing.updated_at = """2024-02-27T12:17:41+04:00"""
listing.is_sold_out = 1
listing.listing_payment_plans = None
listing.sales_status_a_ru = """Нет в продаже"""
listing.sales_status_a_en = """Sold Out"""
listing.sales_status_a_ar = """بيعت بالكامل"""
listing.listing_stocks = """[{"title": {"ru": "Получите 80% комиссии в течение 5 дней", "en": "Get 80% of commission within 5 days", "ar": "احصل على 80% من العمولة خلال 5 أيام"}, "description": {"ru": "<p>При бронировании и продаже квартиры  при помощи Alnair самозанятый брокер получает 80% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки) через 5 дней после подписания SPA. Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iRESTв течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<p><a href="https://about.alnair.ae/booking_80">Описание процесса</a></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 80% of the developer's commission (after deducting transaction-related expenses) within 5 days after signing the SPA. To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_80"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_80">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>", "ar": "<p>عند حجز وبيع شقة بمساعدة النير، يحصل الوسيط الذي يعمل لحسابه الخاص على 80% من عمولة المطور (بعد خصم المصاريف المتعلقة بالمعاملة) خلال 5 أيام بعد توقيع عقد البيع والشراء. للقيام بذلك، من الضروري حجز شقة من خلال نموذج الحجز على موقع Alnair وانتظار اتصال مديري الشركة الشريكة iREST خلال ساعة واحدة لتوضيح التفاصيل وإتمام المعاملة.<a href="https%20://about.alnair.ae/booking_80"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www .w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_80">عملية التسجيل</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">الحصول على iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/25/69/25692832ad3d850fa8a7bcdcee24d041.png"}, {"title": {"ru": "Получите  90% от комиссии застройщика", "en": "Get 90% of the developer's commission", "ar": "90% من عمولة المطور"}, "description": {"ru": "<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p><p></p><p></p></p>", "ar": "<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"}]"""
listing.eoi_a_is_eoi_return = None
listing.eoi_a_eoi_items = None
listing.service_charge = None
listing.assignment = None

listing.developer_id = developer_get_or_add(listing.developer_a_title_a_en, listing.developer_a_title_a_ru, listing.developer_a_title_a_ar, listing.developer_a_logo, Realtor, Developer).id
listing.save()

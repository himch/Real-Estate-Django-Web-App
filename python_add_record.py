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
listings = Listing.objects.filter(complex_id=1094)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T22:55:18+04:00':
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
listing.complex_id = 1094
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2024/1/d7/cb/d7cb66fd7055b0effae142b49d983a27.jpg"""
listing.photo = """https://files.alnair.ae/uploads/2024/1/74/73/74730e4f36e54462276586e8764f3e38.jpg"""
listing.title_a_ru = """Riviera Azure"""
listing.title_a_en = """Riviera Azure"""
listing.title_a_ar = """ريفييرا أزور"""
listing.description_a_ru = """<p>Яркий, изысканный и сделанный на заказ отель Riviera Azure - это воплощение жизни на берегу моря высокого класса. Великолепная кристально чистая лагуна, оживленный бульвар и бесконечное множество развлекательных мероприятий - вот лишь некоторые из удобств, предлагаемых вам в Riviera Azure. Спроектированный с использованием солнечных панелей и вертикальной зелени, вдохновленной движением воды по лагуне, этот архитектурный шедевр является высшим выражением роскоши и комфорта.</p><p>Отель Azizi Riviera, расположенный в самом сердце Meydan в MBR City, является единственным в своем роде местом назначения с мегаинтегрированным торговым районом, оживленным 5-звездочным отелем и представительским бизнес-центром. Azizi Riviera воплощает классический образ жизни средиземноморской Ривьеры в современном стиле. Долгие прогулки по бульвару, оформленному во французском стиле, красивые закаты в кристальной лагуне, бесконечные походы по магазинам и застолья в изысканных ресторанах - все, что вам нужно для идеального образа жизни.</p><p></p><p></p><p></p><p></p><p></p>"""
listing.description_a_en = """<p>Striking, exquisite and bespoke, Riviera Azure is a statement of high-end beachfront living. An outstanding crystal lagoon, a vibrant boulevard, and an endless array of recreational activities are just some of the amenities offered to you at Riviera Azure. Designed with solar panels and vertical greenery inspired by the water movement across the lagoon, this architectural masterpiece is the ultimate expression of luxury and comfort.</p><p>Located in the heart of Meydan in MBR City, Azizi Riviera is a one-of-a-kind destination, featuring a mega-integrated retail district, a vibrant 5-star hotel, and an executive business center. Azizi Riviera evokes the classic Mediterranean Riviera lifestyle with a modern and contemporary touch. Long strolls on the French-inspired boulevard, beautiful sunsets at the crystal lagoon, endless shopping experiences, and ﬁne-dining feasts are all that you need for the ultimate lifestyle.</p><p></p><p></p><p></p><p></p><p></p>"""
listing.description_a_ar = """<p>ريفييرا أزور هو مشروع فاخر جديد من المطور عزيزي للتطوير العقاري ، والمعروف بنهجه في تنظيم مساحة معيشة مريحة ومتميزة. والمشروع الجديد هو أفضل دليل على هذا النهج.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Строится"""
listing.status_a_en = """In Progress"""
listing.status_a_ar = """تحت التشيد"""
listing.construction_start_at = """2022-11-08T18:12:48+04:00"""
listing.construction_progress = 40.19
listing.planned_completion_at = """2024-12-31T18:12:48+04:00"""
listing.predicted_completion_at = """2024-12-31T18:12:48+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Прачечная", "en": "Laundry Room", "ar": "غسيل"}, {"ru": "Детская игровая площадка", "en": "Kids Play Area", "ar": "منطقة لعب الأطفال"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}, {"ru": "Общий SPA", "en": "Shared SPA", "ar": "صالون سبا مشترك"}, {"ru": "Детский бассейн", "en": "Children’s pool", "ar": "حمام سباحة للأطفال"}, {"ru": "Домашние животные разрешены", "en": "Pets Allowed", "ar": "مسموح بدخول الحيوانات الأليفة"}]"""
listing.developer_a_title_a_ru = """Azizi"""
listing.developer_a_title_a_en = """Azizi"""
listing.developer_a_title_a_ar = """عزيزي"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/2/61/96/61960833617390084dcf04c2b55fa878.jpg"""
listing.listing_districts = """["Al Merkadh", "Meydan", "Sobha Hartland", "Mohammed Bin Rashid City (MBR)"]"""
listing.address = """Riviera Azure , Meydan , Dubai"""
listing.latitude = 25.17505402
listing.longitude = 55.31358115
listing.listing_album = """["https://files.alnair.ae/uploads/2023/2/f3/d5/f3d5c400728e2a326b5444d3faf1fb21.jpg", "https://files.alnair.ae/uploads/2023/2/3f/76/3f769b7bf5a5c2adf5d2ea016df6a492.jpg", "https://files.alnair.ae/uploads/2024/1/13/42/13420aae8ede8e4d51c8b89f173a794a.jpg", "https://files.alnair.ae/uploads/2024/1/90/04/900452264064f13f57dbb362b7534c8f.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/2/fd/f3/fdf36563635f12f924eb65d5eae19edb.jpg", "https://files.alnair.ae/uploads/2023/2/df/21/df2134790a14907625831280811696f1.jpg", "https://files.alnair.ae/uploads/2023/2/6a/2d/6a2d4a2de7eca2ef98eb565f8b301b25.jpg", "https://files.alnair.ae/uploads/2023/2/33/5e/335e64065b4e14c6897ae7b26039c09b.jpg", "https://files.alnair.ae/uploads/2023/2/c7/b5/c7b5ddf3ef63f1e6e5a04e21a5c07979.jpg"]}}, {"title": {"ru": "Инфраструктура", "en": "Infrastructure", "ar": "بنية تحتية"}, "images": {"image": ["https://files.alnair.ae/uploads/2024/1/6b/0c/6b0ce120c5b68ecb8085e77d02502640.jpg", "https://files.alnair.ae/uploads/2024/1/3a/9b/3a9bb4a58bd9988f0638767750578cb4.jpg", "https://files.alnair.ae/uploads/2024/1/c9/e9/c9e9c1dd731d05b7a2247bb43b6a53d1.jpg", "https://files.alnair.ae/uploads/2024/1/16/e3/16e325ef671f2899ca6116d11f956a51.jpg", "https://files.alnair.ae/uploads/2024/1/b7/de/b7dea59ce84d44b32a36e104090548d3.jpg", "https://files.alnair.ae/uploads/2024/1/34/7b/347b1bbc82f3a5ba2d85939f9fac825d.jpg", "https://files.alnair.ae/uploads/2024/1/0f/26/0f26a1c6590fabf0baaa6473d00b5c2c.jpg"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 26
listing.price_a_min = 2371000
listing.price_a_max = 39301000
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_1", "count": "23", "min_price": "2371000", "max_price": "2652000", "min_price_m2": "37429", "max_price_m2": "38237", "currency": "AED", "min_area": {"m2": "62.11", "ft2": "668.55"}, "max_area": {"m2": "70.85", "ft2": "762.62"}}, {"key": "rooms_3", "count": "3", "min_price": "35546000", "max_price": "39301000", "min_price_m2": "53205", "max_price_m2": "54710", "currency": "AED", "min_area": {"m2": "652.98", "ft2": "7028.61"}, "max_area": {"m2": "718.35", "ft2": "7732.25"}}]"""
listing.updated_at = """2024-02-26T22:55:18+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "44", "title": {"ru": "План оплаты 40/60", "en": "Payment plan 40/60", "ar": "خطة الدفع 40/60"}, "on_booking_percent": "10", "on_booking_fix": null, "on_construction_percent": "30", "on_construction_fix": null, "on_construction_payments_count": "3", "on_handover_percent": "60", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": [{"title": {"ru": "Admin fee", "en": "Admin fee", "ar": "رسوم المشرف"}, "percent": null, "fix": "5250"}, {"title": {"ru": "DLD fee", "en": "DLD fee", "ar": "رسوم DLD"}, "percent": "4", "fix": null}], "additional_percent": "4", "additional_fix": "5250", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
listing.sales_status_a_ru = """В продаже"""
listing.sales_status_a_en = """On Sale"""
listing.sales_status_a_ar = """معروض للبيع"""
listing.listing_stocks = """[{"title": {"ru": "Получите  90% от комиссии застройщика", "en": "Get 90% of the developer's commission", "ar": "90% من عمولة المطور"}, "description": {"ru": "<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p><p></p><p></p></p>", "ar": "<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"}]"""
listing.eoi_a_is_eoi_return = None
listing.eoi_a_eoi_items = None
listing.service_charge = None
listing.assignment = None

listing.developer_id = developer_get_or_add(listing.developer_a_title_a_en, listing.developer_a_title_a_ru, listing.developer_a_title_a_ar, listing.developer_a_logo, Realtor, Developer).id
listing.save()

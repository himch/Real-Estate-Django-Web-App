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
listings = Listing.objects.filter(complex_id=1098)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T22:31:04+04:00':
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
listing.complex_id = 1098
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/3/bc/b8/bcb861af73968e57eb0e53b1ecc572bb.jpg"""
listing.photo = """https://files.alnair.ae/uploads/2023/3/56/54/5654f73984c36b9819079d73a9f1cb0a.jpg"""
listing.title_a_ru = """Gemz"""
listing.title_a_en = """Gemz"""
listing.title_a_ar = """جيمز"""
listing.description_a_ru = """<p>GEMZ - новый проект Danube переосмысливает роскошную жизнь в самом сердце Аль-Фурджана. Этот уникальный проект с потрясающей архитектурой в форме пирамиды является предстоящей достопримечательностью. Построенный в отличном месте, проект предлагает просторные апартаменты, первоклассные удобства, легкий доступ к общественному транспорту и торговым центрам и многое другое</p>"""
listing.description_a_en = """<p>GEMZ - a new project by Danube is redefining luxury living in the heart of Al Furjan. This unique project with a stunning pyramid shaped architecture is the upcoming landmark. Built on the prime location, the project offers spacious apartments, top-of-the line amenities, easy access to public transport and malls, and a lot more<p><a href="https://danubeproperties.ae/gemz-by-danube#!"></a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"""
listing.description_a_ar = """<p>جيمز-مشروع جديد من قبل الدانوب يعيد تعريف الحياة الفاخرة في قلب الفرجان. هذا المشروع الفريد ذو الهندسة المعمارية المذهلة على شكل هرم هو المعلم القادم. تم بناء المشروع في موقع متميز ، ويوفر شققا واسعة ، ووسائل راحة عالية ، وسهولة الوصول إلى وسائل النقل العام ومراكز التسوق ، وغير ذلك الكثير</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Строится"""
listing.status_a_en = """In Progress"""
listing.status_a_ar = """تحت التشيد"""
listing.construction_start_at = """2022-11-01T18:12:48+04:00"""
listing.construction_progress = 38.46
listing.planned_completion_at = """2025-03-31T18:12:48+04:00"""
listing.predicted_completion_at = """2025-03-31T18:12:48+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Детская игровая площадка", "en": "Kids Play Area", "ar": "منطقة لعب الأطفال"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """Danube"""
listing.developer_a_title_a_en = """Danube"""
listing.developer_a_title_a_ar = """نهر الدانوب"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/3/ce/cf/cecfd137a1c39320cc6947dac2f6a78a.jpg"""
listing.listing_districts = """["Jabal Ali First", "Al Furjan"]"""
listing.address = """Gemz ,Al Fujairah, Dubai"""
listing.latitude = 25.018224
listing.longitude = 55.14058391
listing.listing_album = """["https://files.alnair.ae/uploads/2023/3/be/d0/bed0e99be9c91afdbf90fa1aac4ee288.jpg", "https://files.alnair.ae/uploads/2023/3/f9/27/f92775474667eba88846f113aa13c03d.jpg", "https://files.alnair.ae/uploads/2023/3/e0/50/e0505d4e1280101423c842229ff38f0e.jpg", "https://files.alnair.ae/uploads/2023/3/fd/ae/fdaeb65116bac3dc3fee80199e99c0d5.jpg", "https://files.alnair.ae/uploads/2023/3/14/6f/146f4d975d8b1767011f38c48a62871f.jpg", "https://files.alnair.ae/uploads/2023/3/7e/c2/7ec26518ecc858594f885145ddceb276.jpg", "https://files.alnair.ae/uploads/2023/3/ff/69/ff69e8ebb4b1d0fbc0cec8e13e19f6b0.jpg", "https://files.alnair.ae/uploads/2023/3/e3/24/e324dc22b5a73d38d913749021d843f1.jpg", "https://files.alnair.ae/uploads/2023/3/17/fe/17fe035694a2bb15278a057b9ec38342.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/3/51/73/51736f4f84a480eb9a652d3472854678.jpg", "https://files.alnair.ae/uploads/2023/3/1f/b6/1fb6d1a5a6d4150149d72b1fd546e9df.jpg", "https://files.alnair.ae/uploads/2023/3/a5/2d/a52d0d8100f9aacc0e89a92e51aaf681.jpg", "https://files.alnair.ae/uploads/2023/3/63/fe/63fe5237d9f4bed6dcf86ca1f5180d02.jpg", "https://files.alnair.ae/uploads/2023/3/8d/e6/8de6dadb71f3fdb810d7b6a0c9f36e1d.jpg", "https://files.alnair.ae/uploads/2023/3/ed/e2/ede2d4da20b5c6f0ad36f5fdb59fa22c.jpg", "https://files.alnair.ae/uploads/2023/3/42/d7/42d77067ebbfeaf8c756a26b8c400427.jpg", "https://files.alnair.ae/uploads/2023/3/fb/ec/fbecef070d8a7425124e8270d8d3ebd2.jpg", "https://files.alnair.ae/uploads/2023/3/50/68/5068d7c1c436396ef028fc9aee670171.jpg", "https://files.alnair.ae/uploads/2023/3/13/53/1353896a299b8ed6e4289ebd37283672.jpg", "https://files.alnair.ae/uploads/2023/3/e1/63/e163787fb4f855c09f7a996a150d9905.jpg", "https://files.alnair.ae/uploads/2023/3/25/d9/25d96f443eaed96273136074f1894943.jpg", "https://files.alnair.ae/uploads/2023/3/c0/58/c0580be03701594e507ed2c904d1d45d.jpg", "https://files.alnair.ae/uploads/2023/3/64/46/6446b4647b2cf0b3c84c428218a795f1.jpg", "https://files.alnair.ae/uploads/2023/3/e4/ea/e4eadee2976749eeceadedda97868c5b.jpg", "https://files.alnair.ae/uploads/2023/3/9a/e6/9ae6bbf07bc863c3300dd31d01ed92e0.jpg", "https://files.alnair.ae/uploads/2023/3/cd/0d/cd0d8ac81e3962a803298aac0b579eeb.jpg", "https://files.alnair.ae/uploads/2023/3/dd/31/dd319277f82070d8e6af311851521376.jpg"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 3
listing.price_a_min = 993000
listing.price_a_max = 1836000
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_1", "count": "1", "min_price": "993000", "max_price": "993000", "min_price_m2": "12913", "max_price_m2": "12913", "currency": "AED", "min_area": {"m2": "76.90", "ft2": "827.74"}, "max_area": {"m2": "76.90", "ft2": "827.74"}}, {"key": "rooms_3", "count": "2", "min_price": "1831000", "max_price": "1836000", "min_price_m2": "12376", "max_price_m2": "12376", "currency": "AED", "min_area": {"m2": "147.95", "ft2": "1592.52"}, "max_area": {"m2": "148.35", "ft2": "1596.82"}}]"""
listing.updated_at = """2024-02-26T22:31:04+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "21", "title": {"ru": "План оплаты", "en": "Payment plan", "ar": "خطة الدفع 60/40"}, "on_booking_percent": "10", "on_booking_fix": null, "on_construction_percent": "49", "on_construction_fix": null, "on_construction_payments_count": "11", "on_handover_percent": "1", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": "40", "post_handover_fix": null, "on_post_handover_payments_count": "40", "additional": [{"title": {"ru": "Registration Charges", "en": "Registration Charges", "ar": "رسوم التسجيل"}, "percent": null, "fix": "1092"}, {"title": {"ru": "DLD Fee", "en": "DLD Fee", "ar": "DLD Fee"}, "percent": "4", "fix": null}], "additional_percent": "4", "additional_fix": "1092", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": "month", "count": "1", "repeat_count": "40"}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
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

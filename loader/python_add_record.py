import os
from random import choice
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
import django
django.setup()
from listings.models import Listing
from realtors.models import Realtor
realtor_list = Realtor.objects.all()
realtors_ids = [realtor.id for realtor in realtor_list]
listings = Listing.objects.filter(complex_id=119)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-01-30T16:20:42+04:001':
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
listing.complex_id = 119
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/2/56/0d/560d44899ac49584a777d5228fad7719.png"""
listing.photo = """https://files.alnair.ae/uploads/2023/2/4d/12/4d129cf90619b0ada50ff9628312b011.jpg"""
listing.title_a_ru = """Riviera 34"""
listing.title_a_en = """Riviera 34"""
listing.title_a_ar = """ريفييرا 34"""
listing.description_a_ru = """<p>Riviera сочетает в себе
лучшее из французского средиземноморского дизайна и современную архитектуру,
создавая идеальное место для современной общественной жизни.Riviera состоит из 69 жилых зданий средней
этажности, мега-интегрированного торгового района, захватывающих дух видов на
набережную и пышной зелени.</p>"""
listing.description_a_en = """<p>Riviera combines the best of French Mediterranean design perspective and
modern architecture to create the ideal place for modern community living.
Riviera comprises of 69 mid-rise residential buildings, a mega integrated
retail district, breathtaking waterfront views and lush greenery.</p>"""
listing.description_a_ar = """<p>تجمعريفييرابينأفضلمنظورتصميمالبحرالأبيضالمتوسطالفرنسيوالهندسةالمعماريةالحديثةلإنشاءالمكانالمثاليللعيشالمجتمعيالحديث.
تتكونريفييرامن 69 مبنىسكنيمتوسطالارتفاع،ومنطقةبيعبالتجزئةضخمةمتكاملة،وإطلالاتخلابةعلىالواجهةالبحرية،ومساحاتخضراءمورقة.<p>

</p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"""
listing.price_on_request = 0
listing.status_a_ru = """Завершено"""
listing.status_a_en = """Completed"""
listing.status_a_ar = """منتهى"""
listing.construction_start_at = """2017-10-01T12:10:38+04:00"""
listing.construction_progress = 100.0
listing.planned_completion_at = """2023-06-30T12:10:38+04:00"""
listing.predicted_completion_at = """2023-06-30T00:00:00+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """Azizi"""
listing.developer_a_title_a_en = """Azizi"""
listing.developer_a_title_a_ar = """عزيزي"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/2/61/96/61960833617390084dcf04c2b55fa878.jpg"""
listing.listing_districts = """["Al Merkadh", "Meydan", "Mohammed Bin Rashid City (MBR)"]"""
listing.address = """Riviera 34, Meydan, Dubai"""
listing.latitude = 25.17170834
listing.longitude = 55.30511461
listing.listing_album = """["https://files.alnair.ae/uploads/2023/2/98/35/983521d64761fff2a3caeaa5e69b6a3e.jpg", "https://files.alnair.ae/uploads/2023/2/4d/48/4d481864ccba6f77ff4957cfc985137e.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/2/20/6a/206a9357206c72d3f50ead9a7651ae93.jpg", "https://files.alnair.ae/uploads/2023/2/07/5b/075b9172bef90c976e2c19d552d3b39a.jpg", "https://files.alnair.ae/uploads/2023/2/c6/67/c667e164fd8a53a324ef36982506049a.jpg", "https://files.alnair.ae/uploads/2023/2/c0/42/c04231b9e6c4543a092c39ba92d4dfdd.jpg", "https://files.alnair.ae/uploads/2023/2/66/6f/666f6609dc23223a36f4163d5304cd4d.jpg"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 4
listing.price_a_min = 1798000
listing.price_a_max = 3813000
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_studio", "count": "3", "min_price": "1798000", "max_price": "1937000", "min_price_m2": "38935", "max_price_m2": "41276", "currency": "AED", "min_area": {"m2": "43.57", "ft2": "468.98"}, "max_area": {"m2": "49.80", "ft2": "536.04"}}, {"key": "rooms_1", "count": "1", "min_price": "3813000", "max_price": "3813000", "min_price_m2": "21896", "max_price_m2": "21896", "currency": "AED", "min_area": {"m2": "174.10", "ft2": "1873.99"}, "max_area": {"m2": "174.10", "ft2": "1873.99"}}]"""
listing.updated_at = """2024-01-30T16:20:42+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "874", "title": {"ru": "План оплаты", "en": "Payment Plan", "ar": "خطة الدفع"}, "on_booking_percent": "100", "on_booking_fix": null, "on_construction_percent": null, "on_construction_fix": null, "on_construction_payments_count": "0", "on_handover_percent": null, "on_handover_fix": null, "on_handover_payments_count": "0", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": null, "additional_percent": "0", "additional_fix": "0", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
listing.sales_status_a_ru = """В продаже"""
listing.sales_status_a_en = """On Sale"""
listing.sales_status_a_ar = """معروض للبيع"""
listing.listing_stocks = """[{"title": {"ru": "Получите  90% от комиссии застройщика", "en": "Get 90% of the developer's commission", "ar": "90% من عمولة المطور"}, "description": {"ru": "<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p></p>", "ar": "<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"}]"""
listing.eoi_a_is_eoi_return = None
listing.eoi_a_eoi_items = None
listing.service_charge = None
listing.assignment = None
listing.save()
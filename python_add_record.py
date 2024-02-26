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
listings = Listing.objects.filter(complex_id=1515)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T11:03:35+04:00':
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
listing.complex_id = 1515
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/9/aa/af/aaafb1146d8c0cd7438ba788c51ca0bd.png"""
listing.photo = """https://files.alnair.ae/uploads/2023/9/50/09/500982d3d6d94a04fcd65a7484e8a3cb.jpg"""
listing.title_a_ru = """Rove Home Downtown"""
listing.title_a_en = """Rove Home Downtown"""
listing.title_a_ar = """رو? هوم ريزدنس بي إرث"""
listing.description_a_ru = """<p>ROVE Home – идеальное сочетание роскоши и комфорта. Полностью меблированные апартаменты оснащены высококачественной бытовой техникой, включая телевизоры от ведущих производителей и стильные кухни с техникой. Полностью складывающиеся окна на террасе.<p>Всего 384 квартиры. В доме есть всё, что нужно для комфортной жизни: кафе, коворкинг, звукозаписывающая студия, тренажерный зал, бассейны, студия йоги, зоны отдыха, а также множество дополнительных услуг, предоставляемых консьерж-сервисом 24/7.</p><p>Сервис ROVE Connect обеспечивает комфорт, позволяя заказать любые услуги. А благодаря дополнительным услугам A LA CARTE, проживание резидентов станет ещё более роскошным.</p><p></p></p>"""
listing.description_a_en = """<p>ROVE Home - это идеальное сочетание роскоши и комфорта. Полностью меблированные апартаменты оснащены высококачественной бытовой техникой, в том числе Tax от ведущих производителей, и стильными кухнями с бытовой техникой. Полностью складывающиеся окна на террасе.<p>Всего 384 квартиры. В доме есть все необходимое для комфортной жизни: кафе, коворкинг, студия звукозаписи, тренажерный зал, бассейны, студия йоги, зоны отдыха, а также множество дополнительных услуг, предоставляемых круглосуточной консьерж-службой.</p><p>Сервис RAVE Connect обеспечивает комфорт, позволяя заказывать любые услуги. А благодаря дополнительным услугам A LA CARTE проживание резидентов станет еще более роскошным.</p><p></p></p>"""
listing.description_a_ar = """<p>B+G+M+3P+19</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Запланировано"""
listing.status_a_en = """Scheduled"""
listing.status_a_ar = """البناء المقرر"""
listing.construction_start_at = """2023-09-30T18:12:50+04:00"""
listing.construction_progress = 0.2
listing.planned_completion_at = """2026-06-30T00:00:00+04:00"""
listing.predicted_completion_at = """2026-06-30T00:00:00+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Широкополосный Интернет", "en": "Broadband Internet", "ar": "الإنترنت ذات النطاق العريض"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """Irth Development"""
listing.developer_a_title_a_en = """Irth Development"""
listing.developer_a_title_a_ar = """أي ار تي اتش للتطوير ش.ذ.م.م"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2024/2/52/fd/52fdc3e193fe4a694058d27b1ad10d29.jpg"""
listing.listing_districts = """["Downtown Dubai", "Burj Khalifa"]"""
listing.address = """Downtown, Dubai"""
listing.latitude = 25.19008902
listing.longitude = 55.27128334
listing.listing_album = """["https://files.alnair.ae/uploads/2023/9/dc/77/dc77b60d7c9c0e365bb9b7cb45c1340c.jpg", "https://files.alnair.ae/uploads/2023/9/35/a8/35a854b16d6ae8c1c51ff290b9d0c3ae.jpg", "https://files.alnair.ae/uploads/2023/9/42/9f/429fc33b1e29d4c758f08704b70a38f8.jpg", "https://files.alnair.ae/uploads/2023/9/d9/ed/d9ed6cbed70a531228d0fdb80980bf3a.jpg"]"""
listing.listing_albums = None
listing.buildings_count = 1
listing.for_sale_count = 11
listing.price_a_min = 2529888
listing.price_a_max = 3993888
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_1", "count": "1", "min_price": "2529888", "max_price": "2529888", "min_price_m2": "36554", "max_price_m2": "36554", "currency": "AED", "min_area": {"m2": "76.13", "ft2": "819.46"}, "max_area": {"m2": "76.13", "ft2": "819.46"}}, {"key": "rooms_2", "count": "10", "min_price": "3420888", "max_price": "3993888", "min_price_m2": "307", "max_price_m2": "37332", "currency": "AED", "min_area": {"m2": "111.83", "ft2": "1203.73"}, "max_area": {"m2": "124.74", "ft2": "1342.69"}}]"""
listing.updated_at = """2024-02-26T11:03:35+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "522", "title": {"ru": "План оплаты", "en": "Payment Plan", "ar": "خطة الدفع"}, "on_booking_percent": "20", "on_booking_fix": null, "on_construction_percent": "30", "on_construction_fix": null, "on_construction_payments_count": "1", "on_handover_percent": "50", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": {"title": {"ru": "DLD Fee", "en": "DLD Fee", "ar": "DLD Fee"}, "percent": "4", "fix": null}, "additional_percent": "4", "additional_fix": "0", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
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

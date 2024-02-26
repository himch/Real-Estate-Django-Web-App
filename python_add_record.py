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
listings = Listing.objects.filter(complex_id=1114)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T22:28:04+04:00':
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
listing.complex_id = 1114
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/3/2c/98/2c980a9670195fdb257ad136bbb69ea4.png"""
listing.photo = """https://files.alnair.ae/uploads/2023/3/ec/fb/ecfbd289b5e0de89a62ea830e89644c6.jpg"""
listing.title_a_ru = """Seascape"""
listing.title_a_en = """Seascape"""
listing.title_a_ar = """المناظر البحرية"""
listing.description_a_ru = """<p>Seascape at Rashid Yachts &amp; Marina - это новый комплекс от Emaar Properties, предлагающий прибрежные апартаменты и таунхаусы с 1-3 спальнями, расположенные в Мина-Рашид. Насладитесь новой роскошью на берегу моря в четырех многоэтажных зданиях, где эти современные резиденции предлагают изысканные удобства и спокойную обстановку с захватывающей розничной торговлей и аттракционами.</p>"""
listing.description_a_en = """<p>Seascape atRashid Yachts &amp; Marina is a new development byEmaar Properties, offering 1 to 3-bedroom waterfront apartments &amp; townhouses located withinMina Rashid. Experience the redefined seafront luxury in the four multi-storey buildings, where these contemporary residences offer sophisticated amenities, and tranquil surroundings with exciting retail and attraction.</p>"""
listing.description_a_ar = """<p>المناظر البحرية في راشد لليخوت والمارينا هو تطوير جديد من قبل إعمار العقارية ، ويقدم شقق ومنازل من 1 إلى 3 غرف نوم على الواجهة البحرية تقع داخل ميناء راشد. جرب الفخامة المعاد تعريفها على الواجهة البحرية في المباني الأربعة متعددة الطوابق ، حيث توفر هذه المساكن المعاصرة وسائل راحة متطورة ومحيطا هادئا مع متاجر التجزئة والجذب المثيرة.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Запланировано"""
listing.status_a_en = """Scheduled"""
listing.status_a_ar = """البناء المقرر"""
listing.construction_start_at = """2023-04-13T18:12:48+04:00"""
listing.construction_progress = 1.89
listing.planned_completion_at = """2026-11-30T18:12:48+04:00"""
listing.predicted_completion_at = """2026-11-30T18:12:48+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """Emaar"""
listing.developer_a_title_a_en = """Emaar"""
listing.developer_a_title_a_ar = """إمار"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/3/59/74/5974dd50e1f85b5a56cdcef99f37eafe.png"""
listing.listing_districts = """["Madinat Dubai Al Melaheyah", "Mina Rashid"]"""
listing.address = """Rashid Yachts & Marina - Seascape - Dubai"""
listing.latitude = 25.25765398
listing.longitude = 55.27753102
listing.listing_album = """["https://files.alnair.ae/uploads/2023/3/3c/33/3c33d387b877039335f869e1a76a18f1.jpg", "https://files.alnair.ae/uploads/2023/3/67/45/6745e2b6c4fece7cb4ffd697e4a1bc2a.jpg", "https://files.alnair.ae/uploads/2023/3/39/3c/393cf2bdf03c6a64a54a3b897cdbf885.jpg", "https://files.alnair.ae/uploads/2023/3/ef/43/ef43023e98b1e30efbe2d9186a7541c7.jpg", "https://files.alnair.ae/uploads/2023/12/ac/bf/acbf1b2b69a01aadb61194909c4d3c18.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/3/d9/ae/d9ae9ce42ad05930884e61e0ea0d91a3.jpg", "https://files.alnair.ae/uploads/2023/3/ae/c5/aec51f0318e43db56fcac04707692a37.jpg", "https://files.alnair.ae/uploads/2023/3/a6/9d/a69dc81c2c605cb65017fbeefb1588c5.jpg"]}}]"""
listing.buildings_count = 4
listing.for_sale_count = 1
listing.price_a_min = 5228888
listing.price_a_max = 5228888
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_3", "count": "1", "min_price": "5228888", "max_price": "5228888", "min_price_m2": "18874", "max_price_m2": "18874", "currency": "AED", "min_area": {"m2": "277.04", "ft2": "2982.03"}, "max_area": {"m2": "277.04", "ft2": "2982.03"}}]"""
listing.updated_at = """2024-02-26T22:28:04+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "511", "title": {"ru": "План оплаты", "en": "Payment plan", "ar": "خطة الدفع 90/10"}, "on_booking_percent": "10", "on_booking_fix": null, "on_construction_percent": "70", "on_construction_fix": null, "on_construction_payments_count": "7", "on_handover_percent": "20", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": {"title": {"ru": "DLD Fee", "en": "DLD Fee", "ar": "رسوم DLD"}, "percent": "4", "fix": null}, "additional_percent": "4", "additional_fix": "0", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
listing.sales_status_a_ru = """В продаже"""
listing.sales_status_a_en = """On Sale"""
listing.sales_status_a_ar = """معروض للبيع"""
listing.listing_stocks = """[{"title": {"ru": "Получите 80% комиссии в течение 5 дней", "en": "Get 80% of commission within 5 days", "ar": "احصل على 80% من العمولة خلال 5 أيام"}, "description": {"ru": "<p>При бронировании и продаже квартиры  при помощи Alnair самозанятый брокер получает 80% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки) через 5 дней после подписания SPA. Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iRESTв течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<p><a href="https://about.alnair.ae/booking_80">Описание процесса</a></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 80% of the developer's commission (after deducting transaction-related expenses) within 5 days after signing the SPA. To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_80"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_80">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>", "ar": "<p>عند حجز وبيع شقة بمساعدة النير، يحصل الوسيط الذي يعمل لحسابه الخاص على 80% من عمولة المطور (بعد خصم المصاريف المتعلقة بالمعاملة) خلال 5 أيام بعد توقيع عقد البيع والشراء. للقيام بذلك، من الضروري حجز شقة من خلال نموذج الحجز على موقع Alnair وانتظار اتصال مديري الشركة الشريكة iREST خلال ساعة واحدة لتوضيح التفاصيل وإتمام المعاملة.<a href="https%20://about.alnair.ae/booking_80"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www .w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_80">عملية التسجيل</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">الحصول على iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/25/69/25692832ad3d850fa8a7bcdcee24d041.png"}, {"title": {"ru": "Получите  90% от комиссии застройщика", "en": "Get 90% of the developer's commission", "ar": "90% من عمولة المطور"}, "description": {"ru": "<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p><p></p><p></p></p>", "ar": "<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"}]"""
listing.eoi_a_is_eoi_return = None
listing.eoi_a_eoi_items = None
listing.service_charge = None
listing.assignment = None

listing.developer_id = developer_get_or_add(listing.developer_a_title_a_en, listing.developer_a_title_a_ru, listing.developer_a_title_a_ar, listing.developer_a_logo, Realtor, Developer).id
listing.save()

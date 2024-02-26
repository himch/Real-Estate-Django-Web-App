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
listings = Listing.objects.filter(complex_id=622)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T23:06:24+04:00':
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
listing.complex_id = 622
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/3/87/92/8792cff0b6018df2be34b3960db63e3f.jpg"""
listing.photo = """https://files.alnair.ae/uploads/2022/12/7f/6d/7f6d9a025d114b43c201ef0d6627713e.jpg"""
listing.title_a_ru = """Opalz"""
listing.title_a_en = """Opalz"""
listing.title_a_ar = """أوبالز"""
listing.description_a_ru = """<p>Opalz by Danube Properties - безмятежный оазис среди шумного города, где роскошь встречается с будущим. Этот уникальный архитектурный шедевр ориентирован на будущее и предлагает высочайший уровень роскошной жизни. Расположенные в самом престижном районе Дубая, красивые две башни возвышаются в отличном месте Дубайского научного парка с легким доступом к улице Шейха Зайда, предлагая энергоэффективные удобства, инновационные технологии, экологичную архитектуру и эксклюзивный доступ к современным удобствам, которые навсегда изменят ваш образ жизни.</p>"""
listing.description_a_en = """<p>Opalz by Danube Properties  - A serene oasis amidst the bustling city where luxury meets the future. This unique architectural masterpiece is future-ready and offers the highest standard of opulent living. Located in the plushest precinct of Dubai, the beautiful two towers stand tall in the prime location of Dubai Science Park with easy access to Sheikh Zayed Road while offering energy-efficient amenities, innovative technology, green architecture, and exclusive access to modern amenities that’ll change your lifestyle forever.</p>"""
listing.description_a_ar = """<p>أوبال من دانوب العقارية-واحة هادئة وسط المدينة الصاخبة حيث تلتقي الرفاهية بالمستقبل. هذه التحفة المعمارية الفريدة جاهزة للمستقبل وتوفر أعلى مستوى من المعيشة الفخمة. يقع البرجان الجميلان في أفخم منطقة في دبي ، ويقفان شامخين في الموقع الرئيسي لمجمع دبي للعلوم مع سهولة الوصول إلى شارع الشيخ زايد مع توفير وسائل الراحة الموفرة للطاقة والتكنولوجيا المبتكرة والهندسة المعمارية الخضراء والوصول الحصري إلى وسائل الراحة الحديثة التي ستغير نمط حياتك إلى الأبد.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Строится"""
listing.status_a_en = """In Progress"""
listing.status_a_ar = """تحت التشيد"""
listing.construction_start_at = """2023-01-01T18:12:45+04:00"""
listing.construction_progress = 20.38
listing.planned_completion_at = """2025-09-30T00:00:00+04:00"""
listing.predicted_completion_at = """2025-09-30T00:00:00+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Детская игровая площадка", "en": "Kids Play Area", "ar": "منطقة لعب الأطفال"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}, {"ru": "Широкополосный Интернет", "en": "Broadband Internet", "ar": "الإنترنت ذات النطاق العريض"}]"""
listing.developer_a_title_a_ru = """Danube"""
listing.developer_a_title_a_en = """Danube"""
listing.developer_a_title_a_ar = """نهر الدانوب"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/3/ce/cf/cecfd137a1c39320cc6947dac2f6a78a.jpg"""
listing.listing_districts = """["Al Barsha South Second", "Al Barsha", "Dubai Science Park"]"""
listing.address = """Opalz -Al Barsha South- Dubai"""
listing.latitude = 25.0691325
listing.longitude = 55.248893
listing.listing_album = """["https://files.alnair.ae/uploads/2023/3/41/e7/41e73df1e8c3d227bb29f835a3471505.jpg", "https://files.alnair.ae/uploads/2023/3/9e/a3/9ea37f7ac113001c8afa895e6b8d204d.jpg", "https://files.alnair.ae/uploads/2023/3/79/22/7922c4667638fc0a718312b05fba151e.jpg", "https://files.alnair.ae/uploads/2023/3/33/3f/333fe21899e9b052d7d25fa0bec5351d.jpg", "https://files.alnair.ae/uploads/2023/3/5f/34/5f340a14fb397ad3a8bf21236f8eef66.jpg", "https://files.alnair.ae/uploads/2023/3/46/1a/461a401c110d9f712270ab421ba138de.jpg", "https://files.alnair.ae/uploads/2023/3/ce/00/ce009f7b2d1d36b0a5ad257f40a31efd.jpg", "https://files.alnair.ae/uploads/2023/3/29/23/29237ec3f612e035c599ebafe4978792.jpg", "https://files.alnair.ae/uploads/2023/3/eb/fb/ebfbae68fef1535b161501f36040c9a1.jpg", "https://files.alnair.ae/uploads/2023/3/84/76/8476df291af9dc201f438b3af52b2c72.jpg", "https://files.alnair.ae/uploads/2023/3/6f/14/6f14f226927ad9b09f8c9e2ec811b000.jpg", "https://files.alnair.ae/uploads/2023/3/af/c6/afc6a741cbfb50728e89cbca2b7fbab9.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/3/d9/5f/d95f5e836e7e7bf47991a06aa6a7c3be.jpg", "https://files.alnair.ae/uploads/2023/3/77/56/77567eac2d28e99a3b1f69dd5692566d.jpg", "https://files.alnair.ae/uploads/2023/3/34/09/3409192273982e5c312737d2e5984b43.jpg", "https://files.alnair.ae/uploads/2023/3/d2/b0/d2b0fc0371ae3892bfaea68b23284038.jpg", "https://files.alnair.ae/uploads/2023/3/90/69/9069613b1502e4f63ae5033868bc5d6a.jpg", "https://files.alnair.ae/uploads/2023/3/71/dd/71dda45ba89f31accc52c42f14803d14.jpg"]}}]"""
listing.buildings_count = 2
listing.for_sale_count = 6
listing.price_a_min = 1990000
listing.price_a_max = 3072000
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_2", "count": "5", "min_price": "1990000", "max_price": "3072000", "min_price_m2": "9614", "max_price_m2": "13324", "currency": "AED", "min_area": {"m2": "149.36", "ft2": "1607.70"}, "max_area": {"m2": "319.53", "ft2": "3439.39"}}, {"key": "rooms_3", "count": "1", "min_price": "2737000", "max_price": "2737000", "min_price_m2": "11789", "max_price_m2": "11789", "currency": "AED", "min_area": {"m2": "232.16", "ft2": "2498.95"}, "max_area": {"m2": "232.16", "ft2": "2498.95"}}]"""
listing.updated_at = """2024-02-26T23:06:24+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "22", "title": {"ru": "План оплаты 60/40", "en": "Payment plan 60/40", "ar": "خطة الدفع 60/40"}, "on_booking_percent": "10", "on_booking_fix": null, "on_construction_percent": "49", "on_construction_fix": null, "on_construction_payments_count": "17", "on_handover_percent": "1", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": "40", "post_handover_fix": null, "on_post_handover_payments_count": "40", "additional": [{"title": {"ru": "DLD fee", "en": "DLD fee", "ar": "رسوم DLD"}, "percent": "4", "fix": null}, {"title": {"ru": "Registration fee", "en": "Registration fee", "ar": "رسوم التسجيل"}, "percent": null, "fix": "1092"}], "additional_percent": "4", "additional_fix": "1092", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": "month", "count": "1", "repeat_count": "40"}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
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

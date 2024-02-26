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
listings = Listing.objects.filter(complex_id=1526)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T16:59:01+04:00':
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
listing.complex_id = 1526
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/8/40/0d/400d047f73ddea0da462251df44951a2.jpg"""
listing.photo = """https://files.alnair.ae/uploads/2023/8/19/e1/19e1eb3820e5506584da2ff0f46e5777.jpg"""
listing.title_a_ru = """Eywa"""
listing.title_a_en = """Eywa"""
listing.title_a_ar = """ايوا"""
listing.description_a_ru = """<p>Познакомьтесь с Eywa, новаторской концепцией, ориентированной на состоятельных людей, любящих хорошее самочувствие, образ жизни, благоприятный для природы, и философию Васту Шастры. Расположенный на Марс-Драйв в оживленном районе Бизнес-Бэй с видом на Дубайский канал, 19-этажная резиденция Eywa предлагает высококлассное проживание на набережной в элитных резиденциях. Привлекательная башня открывает новый мир науки, духовности и роскоши, сочетая в себе интерьеры, ориентированные на природу, и передовые технологии с непревзойденными общественными удобствами. Из большинства из 48 роскошных апартаментов и пентхаусов площадью от двух до пяти спален открывается лучший вид на Бурдж-Халифу и извилистый канал.</p>"""
listing.description_a_en = """<p>Meet Aiwa, a pioneering concept geared toward high-net-worth individuals with a love for wellness, a nature-friendly lifestyle, and the philosophies of Vastu Shastra. Sitting on Mars Drive in the bustling Business Bay overlooking the Dubai Canal, the 19-story Aiwa offers upscale waterfront living in high-end residences. The eye-catching tower provides a new world of science, spirituality, and luxury, combining nature-focused interiors and cutting-edge technologies with unparalleled community amenities. Most of the  48 deluxe apartments and penthouses that range from two to five bedrooms best views of Burj Khalifa and the meandering canal.</p>"""
listing.description_a_ar = """<p>تعرف على Aiwa، وهو مفهوم رائد موجه نحو الأفراد ذوي الثروات العالية الذين يحبون الصحة، وأسلوب حياة صديق للطبيعة، وفلسفات فاستو شاسترا. يقع فندق Aiwa المكون من 19 طابقًا في منطقة مارس درايف في الخليج التجاري الصاخب المطل على قناة دبي، ويوفر حياة راقية على الواجهة البحرية في مساكن راقية. يوفر البرج اللافت للنظر عالمًا جديدًا من العلوم والروحانية والرفاهية، ويجمع بين التصميمات الداخلية التي تركز على الطبيعة والتقنيات المتطورة مع وسائل الراحة المجتمعية التي لا مثيل لها. معظم الشقق الفاخرة وشقق البنتهاوس البالغ عددها 48 والتي تتراوح مساحتها من غرفتي نوم إلى خمس غرف نوم تتمتع بإطلالة رائعة على برج خليفة والقناة المتعرجة.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Строится"""
listing.status_a_en = """In Progress"""
listing.status_a_ar = """تحت التشيد"""
listing.construction_start_at = """2023-10-31T18:12:50+04:00"""
listing.construction_progress = 0.0
listing.planned_completion_at = """2026-04-01T18:12:50+04:00"""
listing.predicted_completion_at = """2026-04-01T18:12:50+04:00"""
listing.listing_amenities = """[{"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}, {"ru": "Широкополосный Интернет", "en": "Broadband Internet", "ar": "الإنترنت ذات النطاق العريض"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}]"""
listing.developer_a_title_a_ru = """Rvl Real Estate"""
listing.developer_a_title_a_en = """Rvl Real Estate"""
listing.developer_a_title_a_ar = """رفل للعقارات ش.ذ.م.م"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/9/4d/29/4d2991adf56e0248c2ef5d3244aa346e.png"""
listing.listing_districts = """Business Bay"""
listing.address = """Business Bay, Dubai"""
listing.latitude = 25.18311052
listing.longitude = 55.27323738
listing.listing_album = """["https://files.alnair.ae/uploads/2023/8/b0/c3/b0c3f9b14ab82b07904c570be00c73a3.jpg", "https://files.alnair.ae/uploads/2023/8/67/a3/67a35b969c9c7b76feaec718e5b2215e.jpg", "https://files.alnair.ae/uploads/2023/8/0c/bf/0cbff1f7c8b0d49742d8490d42591ec4.jpg", "https://files.alnair.ae/uploads/2023/8/e1/c2/e1c2fdf2228a6743b5fb1cb62a3efff5.jpg", "https://files.alnair.ae/uploads/2023/8/65/17/65173ad0df2226e727bf639464565b62.jpg", "https://files.alnair.ae/uploads/2023/8/1d/b0/1db0f81def4d4e07532f5f48fa39bba2.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/8/66/8c/668c0b49619b69fec7bdcda87446645c.png", "https://files.alnair.ae/uploads/2023/8/bf/53/bf53918bc7a7570aa75c9d23ba66a2fd.png", "https://files.alnair.ae/uploads/2023/8/29/2c/292c7a9b45ca3efd0cc5280c7c314e74.png", "https://files.alnair.ae/uploads/2023/8/01/50/0150fb4a85cd21547b18c6cb37fd1833.png", "https://files.alnair.ae/uploads/2023/8/61/58/61586660bf04e10f56511e57f7022e75.png"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 27
listing.price_a_min = 10133906
listing.price_a_max = 30570620
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_2", "count": "8", "min_price": "10133906", "max_price": "14752504", "min_price_m2": "36592", "max_price_m2": "40313", "currency": "AED", "min_area": {"m2": "273.60", "ft2": "2945.00"}, "max_area": {"m2": "365.95", "ft2": "3939.05"}}, {"key": "rooms_3", "count": "14", "min_price": "18103208", "max_price": "28644273", "min_price_m2": "37677", "max_price_m2": "52745", "currency": "AED", "min_area": {"m2": "455.60", "ft2": "4904.03"}, "max_area": {"m2": "611.77", "ft2": "6585.03"}}, {"key": "rooms_4", "count": "5", "min_price": "26458742", "max_price": "30570620", "min_price_m2": "45965", "max_price_m2": "50679", "currency": "AED", "min_area": {"m2": "571.54", "ft2": "6152.00"}, "max_area": {"m2": "603.22", "ft2": "6493.00"}}]"""
listing.updated_at = """2024-02-26T16:59:01+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "488", "title": {"ru": "План оплаты", "en": "Payment Plan", "ar": "خطة الدفع"}, "on_booking_percent": "20", "on_booking_fix": null, "on_construction_percent": "40", "on_construction_fix": null, "on_construction_payments_count": "4", "on_handover_percent": "40", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": [{"title": {"ru": "DLD Fee", "en": "DLD Fee", "ar": "DLD Fee"}, "percent": "4", "fix": null}, {"title": {"ru": "Admin charges", "en": "Admin charges", "ar": "الرسوم الإدارية"}, "percent": null, "fix": "3000"}], "additional_percent": "4", "additional_fix": "3000", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
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

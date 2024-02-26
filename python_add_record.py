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
listings = Listing.objects.filter(complex_id=1210)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T23:08:54+04:00':
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
listing.complex_id = 1210
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/5/94/c4/94c4d09fa333ba41303b67334942875e.jpg"""
listing.photo = """https://files.alnair.ae/uploads/2023/5/d3/04/d3047fd2026ce107a98442abfbb8239b.jpg"""
listing.title_a_ru = """Como Residences"""
listing.title_a_en = """Como Residences"""
listing.title_a_ar = """كوزمو ريزيدنسز"""
listing.description_a_ru = """<p>Новейшая достопримечательность Palm Jumeirah позволяет вам наслаждаться образом жизни поистине мирового класса. Исследуйте широкие террасы с блестящими бассейнами и пышной зеленью, полюбуйтесь захватывающим видом на море и городской пейзаж и отдохните в удивительно просторных домах с выдающимися удобствами. Эксклюзивная коллекция роскошных апартаментов и апартаментов с исключительными удобствами предлагает жителям ультра-шикарный, космополитичный образ жизни в окружении искусства и красоты.</p>"""
listing.description_a_en = """<p>Palm Jumeirah's  newest landmark allows you to enjoy a truly world-class lifestyle. Explore sweeping terraces with glistening pools and verdant greenery, gaze out at breathtaking views over the sea and cityscape, and relax in wonderfully spacious homes with outstanding amenities. The exclusive collection of luxury apartments and exceptional amenity suite offers residents an ultra-chic, cosmopolitan lifestyle surrounded by art and beauty.</p>"""
listing.description_a_ar = """<p>يتيح لك أحدث معلم في نخلة جميرا الاستمتاع بأسلوب حياة عالمي حقا. استكشف التراسات الواسعة مع حمامات السباحة المتلألئة والمساحات الخضراء الخضراء ، وانظر إلى المناظر الخلابة للبحر ومناظر المدينة ، واسترخ في منازل فسيحة رائعة مع وسائل الراحة الرائعة. توفر المجموعة الحصرية من الشقق الفاخرة وجناح الراحة الاستثنائي للمقيمين أسلوب حياة فائق الأناقة وعالمي محاط بالفن والجمال.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Строится"""
listing.status_a_en = """In Progress"""
listing.status_a_ar = """تحت التشيد"""
listing.construction_start_at = """2023-09-27T18:12:49+04:00"""
listing.construction_progress = 0.01
listing.planned_completion_at = """2027-03-27T18:12:49+04:00"""
listing.predicted_completion_at = """2027-03-27T18:12:49+04:00"""
listing.listing_amenities = """[{"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Широкополосный Интернет", "en": "Broadband Internet", "ar": "الإنترنت ذات النطاق العريض"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}, {"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}]"""
listing.developer_a_title_a_ru = """Nakheel"""
listing.developer_a_title_a_en = """Nakheel"""
listing.developer_a_title_a_ar = """نخيلهيل"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/3/f5/40/f5409ee3abc4bcc64c98cfc1b932d3ec.png"""
listing.listing_districts = """Palm Jumeirah"""
listing.address = """The Palm Jumeirah, Dubai"""
listing.latitude = 25.11118234
listing.longitude = 55.14548779
listing.listing_album = """["https://files.alnair.ae/uploads/2023/5/4c/0a/4c0a625362b833af02881b111f6a3b49.jpg", "https://files.alnair.ae/uploads/2023/5/08/e0/08e045e1cbf8f04922ca8cd2cf470da4.jpg", "https://files.alnair.ae/uploads/2023/5/02/35/023517072f55d2c111e3b94e699b2aeb.jpg", "https://files.alnair.ae/uploads/2023/5/f2/fe/f2fe73e5b6e501bf9146e1666ca7c481.jpg", "https://files.alnair.ae/uploads/2023/5/0b/af/0baf9d85f26940430f422bc96c4d2b92.jpg", "https://files.alnair.ae/uploads/2023/5/31/ad/31ad3c22baeb0c4ba4ddf40ce9c67341.jpg", "https://files.alnair.ae/uploads/2023/5/ad/11/ad115b5b7d38d85b89b888dddb7b9254.jpg", "https://files.alnair.ae/uploads/2023/5/5a/e2/5ae2dff56436e062077f754bc3a1406b.jpg", "https://files.alnair.ae/uploads/2023/5/9a/49/9a49e59b6fcdc9ed12737012590d55f2.jpg", "https://files.alnair.ae/uploads/2023/5/77/b0/77b02e9796b57eb40d2ccc578ea3e905.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/5/aa/0a/aa0abff74021f89addc1d5e50c210b9d.jpg", "https://files.alnair.ae/uploads/2023/5/fb/c9/fbc9f6abec1081c1148b6d6a35bbab86.jpg", "https://files.alnair.ae/uploads/2023/5/d9/31/d9319d41ba9da028595182a927d96dcd.jpg", "https://files.alnair.ae/uploads/2023/5/13/31/1331fe094d1b958b03997298741dc031.jpg", "https://files.alnair.ae/uploads/2023/5/ca/d5/cad534e2b84b3827944ab144800326ca.jpg", "https://files.alnair.ae/uploads/2023/5/9e/2d/9e2da707bd9ee188ccd15cdf97a52ea4.jpg", "https://files.alnair.ae/uploads/2023/5/f4/82/f482904d83437c730aa1c6ffb2fc183a.jpg", "https://files.alnair.ae/uploads/2023/5/1c/eb/1cebd719633eca6515ca71d4a8ea5f73.jpg", "https://files.alnair.ae/uploads/2023/5/72/2d/722d8b0d5905cd589c936a98b1cffe99.jpg", "https://files.alnair.ae/uploads/2023/5/62/75/6275c9156581cda6b1cb05de6258cc8b.jpg"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 0
listing.price_a_min = None
listing.price_a_max = None
listing.price_a_currency = """AED"""
listing.listing_br_prices = None
listing.updated_at = """2024-02-26T23:08:54+04:00"""
listing.is_sold_out = 1
listing.listing_payment_plans = """[{"id": "87", "title": {"ru": "План оплат 80/20", "en": "Payment Plan 80/20", "ar": "خطة الدفع 80/20"}, "on_booking_percent": "20", "on_booking_fix": null, "on_construction_percent": "60", "on_construction_fix": null, "on_construction_payments_count": "6", "on_handover_percent": "20", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": {"title": {"ru": "DLD Fee", "en": "DLD Fee", "ar": "رسوم DLD"}, "percent": "4", "fix": null}, "additional_percent": "4", "additional_fix": "0", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
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

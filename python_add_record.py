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
listings = Listing.objects.filter(complex_id=1574)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2024-02-26T21:28:06+04:00':
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
listing.complex_id = 1574
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/10/4f/51/4f512a686762fe3c3bdd59862437290f.jpg"""
listing.photo = """https://files.alnair.ae/uploads/2023/10/5c/88/5c88bd0ad1b754e881d22a44c1ae3c5a.jpg"""
listing.title_a_ru = """Damac Casa"""
listing.title_a_en = """Damac Casa"""
listing.title_a_ar = """كازا"""
listing.description_a_ru = """<p>Башня Damac Casa в Аль-Суфухе стала маяком роскоши благодаря апартаментам с 1-5 спальнями и супер-роскошным пентхаусам, разработанным компанией Damac Properties. Это высотное архитектурное чудо обещает гармоничное сочетание изысканности и захватывающих дух видов на знаменитую Пальму Джумейра и готово по-новому определить стандарты роскошной жизни в Дубае. Расположенный в процветающем районе Аль-Суфух, он приглашает людей с утонченным вкусом окунуться в необыкновенный мир жизни.</p>"""
listing.description_a_en = """<p>Damac Casa Tower atAl Sufouh emerges as a beacon of opulence with 1 to 5 bedroom apartments and super luxury penthouses, developed byDamac Properties. This high-rise architectural marvel promises a harmonious blend of sophistication and breathtaking views of the iconic Palm Jumeirah and is poised to redefine the standards of luxury living in Dubai. Located in the flourishing Al Sufouh district, it summons those with discerning tastes to indulge in an extraordinary living experience.</p>"""
listing.description_a_ar = """<p>يبرز برج داماك كازا في الصفوح كمنارة للفخامة مع شقق من غرفة نوم واحدة إلى 5 غرف نوم وشقق بنتهاوس فائقة الفخامة، تم تطويرها بواسطة داماك العقارية. تعد هذه الأعجوبة المعمارية الشاهقة بمزيج متناغم من الرقي والمناظر الخلابة لنخلة جميرا الشهيرة، وتستعد لإعادة تعريف معايير المعيشة الفاخرة في دبي. تقع في منطقة الصفوح المزدهرة، وهي تستدعي أصحاب الأذواق المميزة للاستمتاع بتجربة معيشية غير عادية.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Строится"""
listing.status_a_en = """In Progress"""
listing.status_a_ar = """تحت التشيد"""
listing.construction_start_at = """2023-12-26T18:12:50+04:00"""
listing.construction_progress = 0.0
listing.planned_completion_at = """2028-05-31T00:00:00+04:00"""
listing.predicted_completion_at = """2028-05-31T00:00:00+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Детский бассейн", "en": "Children’s pool", "ar": "حمام سباحة للأطفال"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """Damac"""
listing.developer_a_title_a_en = """Damac"""
listing.developer_a_title_a_ar = """داماك"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/2/87/11/8711de4977ea543b20637d56aae008a7.jpg"""
listing.listing_districts = """["Dubai Media City", "Al Safouh Second"]"""
listing.address = """Casa, Al Sufouh, Dubai"""
listing.latitude = 25.09744591
listing.longitude = 55.15582883
listing.listing_album = """["https://files.alnair.ae/uploads/2023/10/56/26/5626f30312e8696de2e977e7b7d3d962.jpg", "https://files.alnair.ae/uploads/2023/10/ca/c1/cac1c3792b3e9c3153ec4b083c89921c.jpg", "https://files.alnair.ae/uploads/2023/10/71/18/7118527314872d2a438e0bf4175d757a.jpg", "https://files.alnair.ae/uploads/2023/10/36/8c/368c8aaeb95e93bd0c377480789cc59e.jpg", "https://files.alnair.ae/uploads/2023/10/86/78/86781296d2776e7d503e2898811d098a.jpg", "https://files.alnair.ae/uploads/2023/10/d9/d6/d9d695e5a77e62a7d5c427f2646fac84.jpg", "https://files.alnair.ae/uploads/2023/10/02/ee/02ee02447309ab3137015f771298311b.jpg", "https://files.alnair.ae/uploads/2023/10/e7/8d/e78d3a4fbf9b7f70a51db7725af7304a.jpg", "https://files.alnair.ae/uploads/2023/10/55/f2/55f244268cd02734334d75aee711037c.jpg", "https://files.alnair.ae/uploads/2023/10/97/79/97792a391b61c1a66f3835d1652000f1.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/10/60/13/601353f0ff6f70ffa379e1c2821b797c.jpg", "https://files.alnair.ae/uploads/2023/10/89/c7/89c754a23d5d0282700019a3413dce69.jpg", "https://files.alnair.ae/uploads/2023/10/a7/9b/a79be1da4aad56ace66d4514df275e6d.jpg", "https://files.alnair.ae/uploads/2023/10/3a/8a/3a8a48ed5c56edc6945ed88c4efc2bb8.jpg", "https://files.alnair.ae/uploads/2023/10/5e/33/5e33a4f6bf4bde39ae307ad038b139c8.jpg", "https://files.alnair.ae/uploads/2023/10/d9/75/d975d49a311eff267233150d2aeb2965.jpg", "https://files.alnair.ae/uploads/2023/10/a9/6f/a96f66c70eac371b4cac3c1001fb2520.jpg", "https://files.alnair.ae/uploads/2023/10/77/b3/77b3ebd199492a309b4c4049003349db.jpg", "https://files.alnair.ae/uploads/2023/10/9f/55/9f5511712b69204cb989c845d18195ae.jpg", "https://files.alnair.ae/uploads/2023/10/30/56/3056d5eb1ff001b8312fa832e4618dd2.jpg", "https://files.alnair.ae/uploads/2023/10/8f/fa/8ffa169062c539753a24ed7dba67a763.jpg", "https://files.alnair.ae/uploads/2023/10/85/44/8544a4cd8c9b02c9913c7394ffa97f18.jpg"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 56
listing.price_a_min = 2650000
listing.price_a_max = 24807000
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_1", "count": "17", "min_price": "2650000", "max_price": "3467000", "min_price_m2": "30409", "max_price_m2": "33964", "currency": "AED", "min_area": {"m2": "85.01", "ft2": "915.04"}, "max_area": {"m2": "102.08", "ft2": "1098.78"}}, {"key": "rooms_2", "count": "15", "min_price": "4055000", "max_price": "9987000", "min_price_m2": "27082", "max_price_m2": "36580", "currency": "AED", "min_area": {"m2": "133.81", "ft2": "1440.32"}, "max_area": {"m2": "273.43", "ft2": "2943.17"}}, {"key": "rooms_3", "count": "16", "min_price": "5747000", "max_price": "14379000", "min_price_m2": "30358", "max_price_m2": "40241", "currency": "AED", "min_area": {"m2": "189.31", "ft2": "2037.71"}, "max_area": {"m2": "359.79", "ft2": "3872.74"}}, {"key": "rooms_4", "count": "3", "min_price": "18048000", "max_price": "19840000", "min_price_m2": "40706", "max_price_m2": "41961", "currency": "AED", "min_area": {"m2": "443.37", "ft2": "4772.39"}, "max_area": {"m2": "472.84", "ft2": "5089.60"}}, {"key": "rooms_5", "count": "5", "min_price": "23615000", "max_price": "24807000", "min_price_m2": "42339", "max_price_m2": "43169", "currency": "AED", "min_area": {"m2": "550.98", "ft2": "5930.69"}, "max_area": {"m2": "577.44", "ft2": "6215.51"}}]"""
listing.updated_at = """2024-02-26T21:28:06+04:00"""
listing.is_sold_out = 0
listing.listing_payment_plans = """[{"id": "574", "title": {"ru": "План платежей", "en": "Payment Plan", "ar": "خطة الدفع"}, "on_booking_percent": "20", "on_booking_fix": null, "on_construction_percent": "80", "on_construction_fix": null, "on_construction_payments_count": "17", "on_handover_percent": null, "on_handover_fix": null, "on_handover_payments_count": "0", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": {"title": {"ru": "DLD Fee", "en": "DLD Fee", "ar": "DLD Fee"}, "percent": "4", "fix": null}, "additional_percent": "4", "additional_fix": "0", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
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

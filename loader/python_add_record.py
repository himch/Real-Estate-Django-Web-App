import os
from random import choice
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
import django
django.setup()
from listings.models import Listing
from realtors.models import Realtor
realtor_list = Realtor.objects.all()
realtors_ids = [realtor.id for realtor in realtor_list]
listing = Listing()
listing.source = 'alnair'
listing.offer_type = 'sell'
listing.realtor_id = choice(realtors_ids)
listing.complex_id = 116
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/2/f9/fd/f9fd6af5df1d0ccf2456db6c907af99a.png"""
listing.photo = """https://files.alnair.ae/uploads/2023/2/7c/c8/7cc86e746417802330e0ae9ca95fcd71.jpg"""
listing.title_a_ru = """Riviera 31"""
listing.title_a_en = """Riviera 31"""
listing.title_a_ar = """ريفييرا 31"""
listing.description_a_ru = """<p>Riviera сочетает в себе лучшее из французского средиземноморского дизайна и современную архитектуру, создавая идеальное место для современной общественной жизни. Ривьера состоит из 69 жилых зданий средней этажности, мега-интегрированного торгового района, захватывающих дух видов на набережную и пышной зелени.</p>"""
listing.description_a_en = """<p>Riviera combines the best of French Mediterranean design perspective and modern architecture to create the ideal place for modern community living. Riviera comprises of 69 mid-rise residential buildings, a mega integrated retail district, breathtaking waterfront views and lush greenery.</p>"""
listing.description_a_ar = """<p>تجمع ريفييرا بين أفضل منظور تصميم البحر الأبيض المتوسط الفرنسي والهندسة المعمارية الحديثة لإنشاء المكان المثالي للعيش المجتمعي الحديث. تتكون ريفييرا من 69 مبنى سكني متوسط الارتفاع ، ومنطقة بيع بالتجزئة ضخمة متكاملة ، وإطلالات خلابة على الواجهة البحرية ، ومساحات خضراء مورقة.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Завершено"""
listing.status_a_en = """Completed"""
listing.status_a_ar = """منتهى"""
listing.construction_start_at = """2018-04-15T18:10:34+04:00"""
listing.construction_progress = 100.0
listing.planned_completion_at = """2023-06-30T18:10:34+04:00"""
listing.predicted_completion_at = """2023-06-30T00:00:00+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """Azizi"""
listing.developer_a_title_a_en = """Azizi"""
listing.developer_a_title_a_ar = """عزيزي"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/2/61/96/61960833617390084dcf04c2b55fa878.jpg"""
listing.listing_districts = """["Al Merkadh", "Meydan", "Mohammed Bin Rashid City (MBR)"]"""
listing.address = """Riviera 31, Meydan , Dubai"""
listing.latitude = 25.17111256
listing.longitude = 55.30597468
listing.listing_album = """["https://files.alnair.ae/uploads/2023/2/32/f1/32f1df72e6985dfd3a376488c02c47df.jpg", "https://files.alnair.ae/uploads/2023/2/fe/57/fe572c062d6abfc7c37af920d09e72f6.jpg"]"""
listing.albums_a_title_a_ru = """Примеры отделки"""
listing.albums_a_title_a_en = """Finishing examples"""
listing.albums_a_title_a_ar = """أمثلة على التشطيب"""
listing.listing_albums_a_images = """["https://files.alnair.ae/uploads/2023/2/a4/e7/a4e7a911e76e40a4418bb777397a12ea.jpg", "https://files.alnair.ae/uploads/2023/2/ce/3b/ce3b9e960e1da189b8e3f136d641a257.jpg", "https://files.alnair.ae/uploads/2023/2/e7/78/e77870141f2681365d9bdb183cf70bd3.jpg", "https://files.alnair.ae/uploads/2023/2/85/92/85926b2dbe119d61f138ca664b865219.jpg", "https://files.alnair.ae/uploads/2023/2/8c/48/8c48b1508c80005e616686db2d768197.jpg"]"""
listing.buildings_count = 1
listing.for_sale_count = 3
listing.price_a_min = 2074000
listing.price_a_max = 3335000
listing.price_a_currency = """AED"""
listing.listing_br_prices = """[{"key": "rooms_studio", "count": "1", "min_price": "2074000", "max_price": "2074000", "min_price_m2": "23864", "max_price_m2": "23864", "currency": "AED", "min_area": {"m2": "86.91", "ft2": "935.49"}, "max_area": {"m2": "86.91", "ft2": "935.49"}}, {"key": "rooms_1", "count": "2", "min_price": "2976000", "max_price": "3335000", "min_price_m2": "16972", "max_price_m2": "17963", "currency": "AED", "min_area": {"m2": "175.31", "ft2": "1887.02"}, "max_area": {"m2": "185.62", "ft2": "1998.00"}}]"""
listing.updated_at = """2024-01-28T22:33:00+04:00"""
listing.is_sold_out = 0
listing.payment_plans_a_title_a_ru = """План оплаты"""
listing.payment_plans_a_title_a_en = """Payment Plan"""
listing.payment_plans_a_title_a_ar = """خطة الدفع"""
listing.payment_plans_a_on_booking_percent = 100
listing.payment_plans_a_on_booking_fix = None
listing.payment_plans_a_on_construction_percent = None
listing.payment_plans_a_on_construction_fix = None
listing.payment_plans_a_on_construction_payments_count = 0
listing.payment_plans_a_on_handover_percent = None
listing.payment_plans_a_on_handover_fix = None
listing.payment_plans_a_on_handover_payments_count = 0
listing.payment_plans_a_post_handover_percent = None
listing.payment_plans_a_post_handover_fix = None
listing.payment_plans_a_on_post_handover_payments_count = 0
listing.payment_plans_a_additional = None
listing.payment_plans_a_additional_percent = 0
listing.payment_plans_a_additional_fix = 0
listing.payment_plans_a_roi_percent = None
listing.payment_plans_a_roi_fix = None
listing.payment_plans_a_roi_payments_count = 0
listing.payment_plans_a_currency = """AED"""
listing.payment_plans_a_period_after_handover_a_period = None
listing.payment_plans_a_period_after_handover_a_count = None
listing.payment_plans_a_period_after_handover_a_repeat_count = None
listing.payment_plans_a_period_after_roi_a_period = None
listing.payment_plans_a_period_after_roi_a_count = None
listing.payment_plans_a_period_after_roi_a_repeat_count = None
listing.sales_status_a_ru = """В продаже"""
listing.sales_status_a_en = """On Sale"""
listing.sales_status_a_ar = """معروض للبيع"""
listing.stocks_a_title_a_ru = """Получите  90% от комиссии застройщика"""
listing.stocks_a_title_a_en = """Get 90% of the developer's commission"""
listing.stocks_a_title_a_ar = """90% من عمولة المطور"""
listing.stocks_a_description_a_ru = """<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p></p>"""
listing.stocks_a_description_a_en = """<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p></p>"""
listing.stocks_a_description_a_ar = """<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"""
listing.stocks_a_start_at = None
listing.stocks_a_end_at = None
listing.stocks_a_logo = """https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"""
listing.eoi_a_is_eoi_return = None
listing.eoi_a_eoi_items = None
listing.service_charge = None
listing.assignment = None
listing.listing_amenities_list = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.listing_districts_list = """["Al Merkadh", "Meydan", "Mohammed Bin Rashid City (MBR)"]"""
listing.listing_albums_list = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/2/a4/e7/a4e7a911e76e40a4418bb777397a12ea.jpg", "https://files.alnair.ae/uploads/2023/2/ce/3b/ce3b9e960e1da189b8e3f136d641a257.jpg", "https://files.alnair.ae/uploads/2023/2/e7/78/e77870141f2681365d9bdb183cf70bd3.jpg", "https://files.alnair.ae/uploads/2023/2/85/92/85926b2dbe119d61f138ca664b865219.jpg", "https://files.alnair.ae/uploads/2023/2/8c/48/8c48b1508c80005e616686db2d768197.jpg"]}}]"""
listing.listing_payment_plans_list = """[{"id": "875", "title": {"ru": "План оплаты", "en": "Payment Plan", "ar": "خطة الدفع"}, "on_booking_percent": "100", "on_booking_fix": null, "on_construction_percent": null, "on_construction_fix": null, "on_construction_payments_count": "0", "on_handover_percent": null, "on_handover_fix": null, "on_handover_payments_count": "0", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": null, "additional_percent": "0", "additional_fix": "0", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
listing.listing_stocks_list = """[{"title": {"ru": "Получите  90% от комиссии застройщика", "en": "Get 90% of the developer's commission", "ar": "90% من عمولة المطور"}, "description": {"ru": "<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p></p>", "ar": "<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"}]"""
listing.save()
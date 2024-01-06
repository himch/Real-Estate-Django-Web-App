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
listing.realtor_id = choice(realtors_ids)
listing.complex_id = 243
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/4/d6/74/d6743903ba7caaa3855d854705fe8d43.jpg"""
listing.photo = """https://files.alnair.ae/uploads/2023/4/11/47/1147247180f11fbb79b834902bab310b.jpg"""
listing.title_a_ru = """Chic Tower"""
listing.title_a_en = """Chic Tower"""
listing.title_a_ar = """شييك تاور"""
listing.description_a_ru = """<p>Шикарная башня от Damac Properties - это последний и недавно запущенный проект, предлагающий кураторские дизайн-студии и апартаменты с 4 спальнями, расположенные в Бизнес-Бэй, Дубай. Откройте для себя новые высоты роскоши в престижном месте, известном своими выдающимися преимуществами, которые оно может предложить в непосредственной близости. Эксклюзивное место, отличное от остальных районов Дубая, где вам предлагаются некоторые из преимуществ премиум-класса.</p>"""
listing.description_a_en = """<p>Chic Tower byDamac Properties is the latest and newly launched project offering curated design studios to 4 bedroom apartments located atBusiness Bay, Dubai. Explore the new heights of luxury in the premium location known for its outstanding benefits that it has to offer in its close proximity. A location that is exclusive and distinct from the rest of the parts in Dubai, where you are offered some of the premium benefits.</p>"""
listing.description_a_ar = """<p>برج شيك من داماك العقارية هو أحدث مشروع تم إطلاقه حديثا ويقدم استوديوهات تصميم منسقة لشقق من 4 غرف نوم تقع في الخليج التجاري ، دبي. استكشف آفاق الرفاهية الجديدة في الموقع المتميز المعروف بفوائده المتميزة التي يقدمها على مقربة منه. موقع حصري ومتميز عن باقي الأجزاء في دبي ، حيث يتم تقديم بعض المزايا المميزة لك.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Запланировано"""
listing.status_a_en = """Scheduled"""
listing.status_a_ar = """البناء المقرر"""
listing.construction_start_at = """2023-03-15T18:12:53+04:00"""
listing.construction_progress = 3.99
listing.planned_completion_at = """2025-07-30T18:12:53+04:00"""
listing.predicted_completion_at = """2025-07-30T18:12:53+04:00"""
listing.listings_listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Детская игровая площадка", "en": "Kids Play Area", "ar": "منطقة لعب الأطفال"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
listing.developer_a_title_a_ru = """Damac"""
listing.developer_a_title_a_en = """Damac"""
listing.developer_a_title_a_ar = """داماك"""
listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/2/87/11/8711de4977ea543b20637d56aae008a7.jpg"""
listing.districts = """Business Bay"""
listing.address = """Chic Tower, Business Bay, Dubai"""
listing.latitude = 25.18354928
listing.longitude = 55.26139333
listing.listings_listing_album = """["https://files.alnair.ae/uploads/2023/4/c9/7a/c97a58a6a6411df2bb53f4d42d6c856e.jpg", "https://files.alnair.ae/uploads/2023/4/e9/7d/e97dcec6e1838d0911b023655ed95091.jpg", "https://files.alnair.ae/uploads/2023/4/6a/5c/6a5c95cd282b1666f2e4a1578ef40062.jpg", "https://files.alnair.ae/uploads/2023/4/12/82/12825c7741e1ab080e75302e1ef49a94.jpg", "https://files.alnair.ae/uploads/2023/4/17/d6/17d6d3a958fc3121872a030aa686db1d.jpg", "https://files.alnair.ae/uploads/2023/4/23/8f/238fdc19d730164153d8efed216f30cd.jpg", "https://files.alnair.ae/uploads/2023/4/ff/51/ff51eb201ee9c07aac874722c1836094.jpg", "https://files.alnair.ae/uploads/2023/4/d8/8b/d88be2edc1ba0b04b001b63cfa913410.jpg", "https://files.alnair.ae/uploads/2023/4/bf/a6/bfa66dfcf6ffb9a577acbc44a044cc07.jpg", "https://files.alnair.ae/uploads/2023/4/47/63/4763833a16953d525a39653cdd3f0c21.jpg", "https://files.alnair.ae/uploads/2023/4/bf/a0/bfa067f0e39965588117c1d3536e553d.jpg", "https://files.alnair.ae/uploads/2023/4/09/aa/09aa08844b3495342014f71dbf2db9cb.jpg", "https://files.alnair.ae/uploads/2023/4/48/56/48566934ba08e74a24682b447288ba64.jpg", "https://files.alnair.ae/uploads/2023/4/1d/17/1d177660a989834530b2f25a76a7e775.jpg", "https://files.alnair.ae/uploads/2023/4/14/54/1454cf1667fdadb25ad51d29dc5bc2dc.jpg", "https://files.alnair.ae/uploads/2023/4/9e/1a/9e1a8e611bc605a3399fd3f1a1dc5ff7.jpg", "https://files.alnair.ae/uploads/2023/4/61/c8/61c881ccd0660c3c1af1be0f05058013.jpg", "https://files.alnair.ae/uploads/2023/4/0a/39/0a398d07bc7ed2feeafd0915250ae091.jpg"]"""
listing.albums_a_title_a_ru = """Примеры отделки"""
listing.albums_a_title_a_en = """Finishing examples"""
listing.albums_a_title_a_ar = """أمثلة على التشطيب"""
listing.listings_listing_albums_a_images = """["https://files.alnair.ae/uploads/2023/4/ce/ba/ceba02f037eb32252f64c740627a7653.jpg", "https://files.alnair.ae/uploads/2023/4/63/26/6326a5478891a873d93389d3ace4fc04.jpg", "https://files.alnair.ae/uploads/2023/4/3a/82/3a82ec2a1f1ee68e31f3b0f1f95e3293.jpg", "https://files.alnair.ae/uploads/2023/4/28/ed/28ed8fc6df78d84f11e36b5398ab1537.jpg", "https://files.alnair.ae/uploads/2023/4/2e/ff/2eff5cc989394d57b27ecf04df304fb8.jpg", "https://files.alnair.ae/uploads/2023/4/2e/32/2e32ec06a854d1813d8c8cd8b06e1700.jpg", "https://files.alnair.ae/uploads/2023/4/43/bc/43bc2abce63b29554e89cb0780513bb4.jpg", "https://files.alnair.ae/uploads/2023/4/f7/4b/f74b25183f818d647f596b5848ef5db0.jpg", "https://files.alnair.ae/uploads/2023/4/3c/dc/3cdc172eb82af76bfa888383b4d9e4e3.jpg", "https://files.alnair.ae/uploads/2023/4/ee/63/ee6361f5d0174023ab7c1e1b6306f938.jpg", "https://files.alnair.ae/uploads/2023/4/78/e1/78e1081275477a94e51953bd44588e30.jpg", "https://files.alnair.ae/uploads/2023/4/27/d2/27d22fab2835c4d036f463f7410ffc61.jpg", "https://files.alnair.ae/uploads/2023/4/c4/7f/c47ff17d607f3a197e36486023a1034a.jpg", "https://files.alnair.ae/uploads/2023/4/f6/05/f6056e3ac731582d0a858219253511cf.jpg", "https://files.alnair.ae/uploads/2023/4/d7/ab/d7ab0ccc6ee29accecfc5a2c57b0069c.jpg", "https://files.alnair.ae/uploads/2023/4/3d/89/3d89384cec6148b421ad1050a7b29110.jpg", "https://files.alnair.ae/uploads/2023/4/d9/65/d965ca1ba599c9be7461ebf5fc6c3edc.jpg", "https://files.alnair.ae/uploads/2023/4/ce/c3/cec3b3b7e261931f0ea4959ce0863af1.jpg"]"""
listing.buildings_count = 1
listing.for_sale_count = 7
listing.price_a_min = 2474000
listing.price_a_max = 5172000
listing.price_a_currency = """AED"""
listing.br_prices_a_key = """rooms_1"""
listing.br_prices_a_count = 7
listing.br_prices_a_min_price = 2474000
listing.br_prices_a_max_price = 5172000
listing.br_prices_a_min_price_m2 = 28741
listing.br_prices_a_max_price_m2 = 29067
listing.br_prices_a_currency = """AED"""
listing.br_prices_a_min_area_a_m2 = 86.08
listing.br_prices_a_min_area_a_ft2 = 926.56
listing.br_prices_a_max_area_a_m2 = 177.95
listing.br_prices_a_max_area_a_ft2 = 1915.44
listing.updated_at = """2024-01-06T17:51:26+04:00"""
listing.is_sold_out = 0
listing.payment_plans_a_title_a_ru = """План оплаты 80/20"""
listing.payment_plans_a_title_a_en = """Payment plan 80/20"""
listing.payment_plans_a_title_a_ar = """خطة الدفع 80/20"""
listing.payment_plans_a_on_booking_percent = 20
listing.payment_plans_a_on_booking_fix = None
listing.payment_plans_a_on_construction_percent = 60
listing.payment_plans_a_on_construction_fix = None
listing.payment_plans_a_on_construction_payments_count = 17
listing.payment_plans_a_on_handover_percent = 20
listing.payment_plans_a_on_handover_fix = None
listing.payment_plans_a_on_handover_payments_count = 1
listing.payment_plans_a_post_handover_percent = None
listing.payment_plans_a_post_handover_fix = None
listing.payment_plans_a_on_post_handover_payments_count = 0
listing.payment_plans_a_additional_a_title_a_ru = """DLD fee"""
listing.payment_plans_a_additional_a_title_a_en = """DLD fee"""
listing.payment_plans_a_additional_a_title_a_ar = """رسوم DLD"""
listing.payment_plans_a_additional_a_percent = 4
listing.payment_plans_a_additional_a_fix = None
listing.payment_plans_a_additional_percent = 4
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
listing.listings_listing_stocks = """[{"title": {"ru": "Получите 80% комиссии в течение 5 дней", "en": "Get 80% of commission within 5 days", "ar": "احصل على 80% من العمولة خلال 5 أيام"}, "description": {"ru": "<p>При бронировании и продаже квартиры  при помощи Alnair самозанятый брокер получает 80% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки) через 5 дней после подписания SPA. Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iRESTв течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<p><a href="https://about.alnair.ae/booking_80">Описание процесса</a></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 80% of the developer's commission (after deducting transaction-related expenses) within 5 days after signing the SPA. To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_80"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_80">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>", "ar": "<p>عند حجز وبيع شقة بمساعدة النير، يحصل الوسيط الذي يعمل لحسابه الخاص على 80% من عمولة المطور (بعد خصم المصاريف المتعلقة بالمعاملة) خلال 5 أيام بعد توقيع عقد البيع والشراء. للقيام بذلك، من الضروري حجز شقة من خلال نموذج الحجز على موقع Alnair وانتظار اتصال مديري الشركة الشريكة iREST خلال ساعة واحدة لتوضيح التفاصيل وإتمام المعاملة.<a href="https%20://about.alnair.ae/booking_80"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www .w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_80">عملية التسجيل</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">الحصول على iREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/25/69/25692832ad3d850fa8a7bcdcee24d041.png"}, {"title": {"ru": "Получите  90% от комиссии застройщика", "en": "Get 90% of the developer's commission", "ar": "90% من عمولة المطور"}, "description": {"ru": "<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p></p>", "en": "<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p></p>", "ar": "<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"}, "start_at": null, "end_at": null, "logo": "https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"}]"""
listing.eoi_a_is_eoi_return = None
listing.eoi_a_eoi_items = None
listing.service_charge = None
listing.assignment = None
listing.save()

# import os
# from random import choice
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
#
# import django
#
# django.setup()
#
# from listings.models import Listing
# from realtors.models import Realtor
#
# realtor_list = Realtor.objects.all()
# realtors_ids = [realtor.id for realtor in realtor_list]
#
# listing = Listing()
# listing.realtor_id = choice(realtors_ids)
#
# listing.complex_id = 1198
# listing.type = """residential_complex"""
# listing.logo = """https://files.alnair.ae/uploads/2023/4/15/50/1550025d538acc41be81a583f1a37fec.jpg"""
# listing.photo = """https://files.alnair.ae/uploads/2023/4/a0/db/a0db9f8bff2b373d14c6931092ba9ce5.jpg"""
# listing.title_a_ru = """Fashionz"""
# listing.title_a_en = """Fashionz"""
# listing.title_a_ar = """الموضة"""
# listing.description_a_ru = """<p>FASHIONZ - стиль жизни от кутюр, где прославляется индивидуальность и мода оживает каждый день. Влюбитесь по уши, окунувшись в роскошную жизнь в FASHIONZ, одной из самых высоких башен в Jumeirah Village Triangle. Вдохновленный иконами стиля, FASHIONZ отличается современным дизайном и идеальным сочетанием внутренних и наружных удобств, которые подарят вам мир комфорта, роскоши и стиля.<p>Насладитесь уникальным в своем роде эстетическим центром FashionTV Salon FTV, где вы можете побаловать себя стилем. Роскошный ресторан FashionTV на крыше с бассейном здесь вас ждет изысканная атмосфера и восхитительная кухня, а кафе FTV станет идеальным местом для стильного и в то же время непринужденного ужина с друзьями. Тренажерный зал и спа-салон FashionTV помогут вам поддерживать свою физическую форму и восстановить силы.</p><p>В FASHIONZ каждая деталь была продумана до мелочей, чтобы обеспечить вам непревзойденный жизненный опыт. Приезжайте и ощутите воплощение роскоши жизни в FASHIONZ by DANUBE.</p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"""
# listing.description_a_en = """<p>FASHION is a couture lifestyle where individuality is glorified and fashion comes to life every day. Fall head over heels in love with the luxurious life at FASHION, one of the tallest towers in Jumeirah Village Triangle. Inspired by style icons, FASHION features a modern design and a perfect combination of indoor and outdoor amenities that will give you a world of comfort, luxury and style.<p>Enjoy the unique aesthetic center FashionTV Salon FTV, where you can pamper yourself with style. Luxury restaurant FashionTV on the roof with a swimming pool here you will find a refined atmosphere and delicious cuisine, and cafe FTV will be the perfect place for a stylish and at the same time casual dinner with friends. The FashionTV gym and Spa will help you maintain your fitness and restore your strength.</p><p>At FASHIONZ, every detail has been thought through to the smallest detail to provide you with an unsurpassed life experience. Come and experience the embodiment of the luxury of life in FASHIONZ by DANUBE.</p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"""
# listing.description_a_ar = """<p>الموضة هي أسلوب حياة راقي حيث يتم تمجيد الفردية وتأتي الموضة إلى الحياة كل يوم. تقع رأسا على عقب في الحب مع الحياة الفاخرة في الأزياء ، واحدة من أطول الأبراج في مثلث قرية الجميرا. مستوحاة من أيقونات الأناقة ، تتميز الموضة بتصميم عصري ومزيج مثالي من وسائل الراحة الداخلية والخارجية التي ستمنحك عالما من الراحة والرفاهية والأناقة.<p>تتمتع فريدة من نوعها مركز الجمالية فاشيونتف صالون فتف ، حيث يمكنك تدليل نفسك مع الاسلوب. مطعم فاخر فاشيونتف على السطح مع حمام سباحة هنا سوف تجد جو المكرر والمأكولات اللذيذة ، وسوف مقهى فتف يكون المكان المثالي لعشاء أنيق وفي الوقت نفسه عارضة مع الأصدقاء. سوف فاشيونتف جيم وسبا تساعدك على الحفاظ على لياقتك واستعادة قوتك.</p><p>في فاشيونز ، تم التفكير في كل التفاصيل إلى أصغر التفاصيل لتزويدك بتجربة حياة غير مسبوقة. تعال وتجربة تجسيد ترف الحياة في فاشيونز من الدانوب.</p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"""
# listing.price_on_request = 0
# listing.status_a_ru = """Строится"""
# listing.status_a_en = """In Progress"""
# listing.status_a_ar = """تحت التشيد"""
# listing.construction_start_at = """2023-08-01T18:12:59+04:00"""
# listing.construction_progress = 0.03
# listing.planned_completion_at = """2027-02-01T00:00:00+04:00"""
# listing.predicted_completion_at = """2027-02-01T00:00:00+04:00"""
# listing.listings_listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Консьерж-сервис", "en": "Concierge Service", "ar": "خدمة الكونسيرج"}, {"ru": "Детский бассейн", "en": "Children’s pool", "ar": "حمام سباحة للأطفال"}, {"ru": "Охрана", "en": "Security", "ar": "حماية"}, {"ru": "Широкополосный Интернет", "en": "Broadband Internet", "ar": "الإنترنت ذات النطاق العريض"}, {"ru": "Лобби", "en": "Lobby", "ar": "ردهة"}]"""
# listing.developer_a_title_a_ru = """Danube"""
# listing.developer_a_title_a_en = """Danube"""
# listing.developer_a_title_a_ar = """نهر الدانوب"""
# listing.developer_a_logo = """https://files.alnair.ae/uploads/2023/3/ce/cf/cecfd137a1c39320cc6947dac2f6a78a.jpg"""
# listing.listings_listing_districts = """["Al Barsha South Fifth", "Jumeirah Village Triangle (JVT)"]"""
# listing.address = """Jumeirah Village, Jumeirah Village Triangle, Dubai"""
# listing.latitude = 25.0421685
# listing.longitude = 55.18873571
# listing.listings_listing_album = """["https://files.alnair.ae/uploads/2023/4/3c/6b/3c6b2162af242adb5012ad01a081219e.jpg", "https://files.alnair.ae/uploads/2023/4/0b/9e/0b9ea3243fc42552f4f2f1b5fe6c83c7.jpg", "https://files.alnair.ae/uploads/2023/4/ea/10/ea101c205fd67013d7f6a1566c7d21e9.jpg", "https://files.alnair.ae/uploads/2023/4/89/0d/890d71141f15cedad079dd05c0992b1e.jpg"]"""
# listing.albums_a_title_a_ru = """Примеры отделки"""
# listing.albums_a_title_a_en = """Finishing examples"""
# listing.albums_a_title_a_ar = """أمثلة على التشطيب"""
# listing.listings_listing_albums_a_images = """["https://files.alnair.ae/uploads/2023/4/7e/17/7e170e00b27dd9e26aa3e4a3c78ce152.jpg", "https://files.alnair.ae/uploads/2023/4/a5/6c/a56c3347b44cfd98c68de64dbfd389d4.jpg", "https://files.alnair.ae/uploads/2023/4/24/c1/24c145495f9f167b24f48cc90dc6450e.jpg", "https://files.alnair.ae/uploads/2023/4/5e/bf/5ebfde45bce70a58d69e4f7a9fa937cf.jpg"]"""
# listing.buildings_count = 1
# listing.for_sale_count = 90
# listing.price_a_min = 764000
# listing.price_a_max = 2449000
# listing.price_a_currency = """AED"""
# listing.listings_listing_br_prices = """[{"key": "rooms_studio", "count": "10", "min_price": "764000", "max_price": "914000", "min_price_m2": "19409", "max_price_m2": "23705", "currency": "AED", "min_area": {"m2": "32.23", "ft2": "346.92"}, "max_area": {"m2": "42.61", "ft2": "458.65"}}, {"key": "rooms_1", "count": "40", "min_price": "1338000", "max_price": "1655000", "min_price_m2": "16947", "max_price_m2": "21502", "currency": "AED", "min_area": {"m2": "70.49", "ft2": "758.75"}, "max_area": {"m2": "81.10", "ft2": "872.95"}}, {"key": "rooms_2", "count": "36", "min_price": "1676000", "max_price": "1915000", "min_price_m2": "16318", "max_price_m2": "19264", "currency": "AED", "min_area": {"m2": "99.41", "ft2": "1070.04"}, "max_area": {"m2": "109.45", "ft2": "1178.11"}}, {"key": "rooms_3", "count": "4", "min_price": "2366000", "max_price": "2449000", "min_price_m2": "17307", "max_price_m2": "17957", "currency": "AED", "min_area": {"m2": "136.38", "ft2": "1467.98"}, "max_area": {"m2": "136.71", "ft2": "1471.53"}}]"""
# listing.updated_at = """2024-01-06T18:51:05+04:00"""
# listing.is_sold_out = 0
# listing.payment_plans_a_title_a_ru = """План оплаты"""
# listing.payment_plans_a_title_a_en = """Payment plan"""
# listing.payment_plans_a_title_a_ar = """خطة الدفع"""
# listing.payment_plans_a_on_booking_percent = 10
# listing.payment_plans_a_on_booking_fix = None
# listing.payment_plans_a_on_construction_percent = 40
# listing.payment_plans_a_on_construction_fix = None
# listing.payment_plans_a_on_construction_payments_count = 28
# listing.payment_plans_a_on_handover_percent = 50
# listing.payment_plans_a_on_handover_fix = None
# listing.payment_plans_a_on_handover_payments_count = 36
# listing.payment_plans_a_post_handover_percent = None
# listing.payment_plans_a_post_handover_fix = None
# listing.payment_plans_a_on_post_handover_payments_count = 0
# listing.listings_listing_payment_plans_a_additional = """[{"title": {"ru": "DLD Fee", "en": "DLD Fee", "ar": "DLD Fee"}, "percent": "4", "fix": null}, {"title": {"ru": "Registration Charges", "en": "Registration Charges", "ar": "رسوم التسجيل"}, "percent": null, "fix": "1093"}]"""
# listing.payment_plans_a_additional_percent = 4
# listing.payment_plans_a_additional_fix = 1093
# listing.payment_plans_a_roi_percent = None
# listing.payment_plans_a_roi_fix = None
# listing.payment_plans_a_roi_payments_count = 0
# listing.payment_plans_a_currency = """AED"""
# listing.payment_plans_a_period_after_handover_a_period = None
# listing.payment_plans_a_period_after_handover_a_count = None
# listing.payment_plans_a_period_after_handover_a_repeat_count = None
# listing.payment_plans_a_period_after_roi_a_period = None
# listing.payment_plans_a_period_after_roi_a_count = None
# listing.payment_plans_a_period_after_roi_a_repeat_count = None
# listing.sales_status_a_ru = """В продаже"""
# listing.sales_status_a_en = """On Sale"""
# listing.sales_status_a_ar = """معروض للبيع"""
# listing.stocks_a_title_a_ru = """Получите  90% от комиссии застройщика"""
# listing.stocks_a_title_a_en = """Get 90% of the developer's commission"""
# listing.stocks_a_title_a_ar = """90% من عمولة المطور"""
# listing.stocks_a_description_a_ru = """<p>При бронировании и продаже квартиры при помощи Alnair самозанятый брокер получает 90% от комиссии застройщика (за вычетом расходов, связанных с проведением сделки). Для этого необходимо забронировать квартиру через форму бронирования на сайте Alnair и подождать, пока менеджеры компании партнера iREST в течение 1 часа свяжутся с вами для уточнения деталей и оформления сделки.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Описание процесса</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">Договор оферты iREST</a></p><p></p><p></p><p></p></p>"""
# listing.stocks_a_description_a_en = """<p>When booking and selling an apartment with Alnair help, a self-employed broker gets 90% of the developer's commission (after deducting transaction-related expenses). To do this, it is necessary to book an apartment through the booking form on the Alnair website and wait for the managers of the partner company iREST to contact you within 1 hour to clarify the details and complete the transaction.<a href="https://about.alnair.ae/booking_90"></a><p xmlns="http://www.w3.org/1999/xhtml"></p><p xmlns="http://www.w3.org/1999/xhtml"><a href="https://about.alnair.ae/booking_90">Process description</a></p><p></p><p><a href="https://www.irest.agency/alnair-terms">IREST offer agreement</a></p><p></p></p>"""
# listing.stocks_a_description_a_ar = """<p>عند الحجز عبر بوابة النيير، يحصل الوسيط أو الوكالة التي تعمل لحسابها الخاص على 90% من عمولة المطور (مطروحًا منها المصاريف المتعلقة بالصفقة). للمشاركة في العرض الترويجي، يتعين عليك حجز شقة باستخدام نموذج الحجز وانتظار اتصال مديري iREST التابعين للشركة الشريكة لتوضيح التفاصيل وإتمام الصفقة.<p><a href="https://about.%20alnair.ae/booking_new">وصف العملية</a></p><p><a href="https://www.irest.agency/alnair-terms">اتفاقية عرض IREST</a></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p></p>"""
# listing.stocks_a_start_at = None
# listing.stocks_a_end_at = None
# listing.stocks_a_logo = """https://files.alnair.ae/uploads/2023/12/a3/a9/a3a9489d42c70388ac6c4b5bf0f75936.png"""
# listing.eoi_a_is_eoi_return = None
# listing.eoi_a_eoi_items = None
# listing.service_charge = None
# listing.assignment = None
# listing.save()
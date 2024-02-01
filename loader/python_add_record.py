import os
from random import choice
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
import django
django.setup()
from listings.models import Listing
from realtors.models import Realtor
realtor_list = Realtor.objects.all()
realtors_ids = [realtor.id for realtor in realtor_list]
listings = Listing.objects.filter(complex_id=1550)
if listings.exists():
    listing = listings.first()
    if listing.updated_at == '2023-09-20T12:55:15+04:00':
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
listing.complex_id = 1550
listing.type = """residential_complex"""
listing.logo = """https://files.alnair.ae/uploads/2023/9/87/95/879572f684bf34f6eff0b4aeffb3021c.png"""
listing.photo = """https://files.alnair.ae/uploads/2023/9/06/47/0647f526b7a94f234eabbcd65db1ed0e.jpg"""
listing.title_a_ru = """DIFC living"""
listing.title_a_en = """DIFC living"""
listing.title_a_ar = """مركز دبي المالي العالمي المعيشة"""
listing.description_a_ru = """<p>DIFC Living — первом жилом комплексе от Международного финансового центра Дубая (DIFC). Наши исключительные жилые объекты безупречно интегрированы в инфраструктуру DIFC, образуя гармоничное и современное пространство для жизни в синергии с процветающим сообществом и экологичным будущим. DIFC Living предлагает своим жильцам беспрепятственный доступ к торговому центру Gate Avenue. Насладитесь непревзойденным удобством и легким доступом в один из самых ярких и востребованных районов Дубая. Откройте для себя путь к жизни высшего класса.</p>"""
listing.description_a_en = """<p>DIFC Living — the first residential complex from Dubai International Financial Center (DIFC). Our exceptional residential properties are perfectly integrated into the infrastructure DIFC, forming a harmonious and modern space for living in synergy with a thriving community and an eco -friendly future. DIFC Living offers its residents unhindered access to the mall Gate Avenue. Enjoy unsurpassed convenience and easy access to one of the most vibrant and sought-after areas of Dubai. Discover the path to upper-class life.</p>"""
listing.description_a_ar = """<p>DIFC Living – أول مجمع سكني من مركز دبي المالي العالمي (DIFC). تندمج عقاراتنا السكنية الاستثنائية بشكل مثالي في البنية التحتية لمركز دبي المالي العالمي، مما يشكل مساحة متناغمة وحديثة للعيش في تآزر مع مجتمع مزدهر ومستقبل صديق للبيئة. يوفر DIFC Living لسكانه إمكانية الوصول دون عوائق إلى المركز التجاري Gate Avenue. استمتع براحة لا مثيل لها وسهولة الوصول إلى واحدة من أكثر المناطق حيوية ومرغوبة في دبي. اكتشف الطريق إلى حياة الطبقة العليا.</p>"""
listing.price_on_request = 0
listing.status_a_ru = """Строится"""
listing.status_a_en = """In Progress"""
listing.status_a_ar = """تحت التشيد"""
listing.construction_start_at = None
listing.construction_progress = None
listing.planned_completion_at = """2026-09-30T00:00:00+04:00"""
listing.predicted_completion_at = """2026-09-30T00:00:00+04:00"""
listing.listing_amenities = """[{"ru": "Общий бассейн", "en": "Shared Pool", "ar": "بركة مشتركه"}, {"ru": "Общий SPA", "en": "Shared SPA", "ar": "صالون سبا مشترك"}]"""
listing.developer_a_title_a_ru = None
listing.developer_a_title_a_en = None
listing.developer_a_title_a_ar = None
listing.developer_a_logo = None
listing.listing_districts = """["DIFC", "Za´Abeel Second"]"""
listing.address = """675H+FC7 - Al Mustaqbal St - Trade Centre - DIFC - Dubai"""
listing.latitude = 25.20846608
listing.longitude = 55.27842611
listing.listing_album = """["https://files.alnair.ae/uploads/2023/9/e7/df/e7df9426541b8f83abf9e5dcbd4c0f8f.jpg", "https://files.alnair.ae/uploads/2023/9/69/da/69da8142646d4e4e519081f821ca80cb.jpg", "https://files.alnair.ae/uploads/2023/9/80/1a/801a15701a9a85188905ae3b7622ddc0.jpg", "https://files.alnair.ae/uploads/2023/9/4d/a1/4da1294ba601b02a0a6d989443e7d422.jpg", "https://files.alnair.ae/uploads/2023/9/dd/46/dd46a22e713b3737d660f2d929ad9fcc.jpg", "https://files.alnair.ae/uploads/2023/9/5a/91/5a91d454953fb76002a3bd6e5c62badf.jpg", "https://files.alnair.ae/uploads/2023/9/41/f4/41f457206b0de44387bca936dae574ad.jpg", "https://files.alnair.ae/uploads/2023/9/a7/c4/a7c4e692be4a25f3c31b4f9533e90150.jpg"]"""
listing.listing_albums = """[{"title": {"ru": "Примеры отделки", "en": "Finishing examples", "ar": "أمثلة على التشطيب"}, "images": {"image": ["https://files.alnair.ae/uploads/2023/9/48/f3/48f3ff69d864d67b344731cbed4908a7.jpg", "https://files.alnair.ae/uploads/2023/9/68/23/68233a7ed4b10b609b872d683d6f3f3a.jpg", "https://files.alnair.ae/uploads/2023/9/cc/e5/cce5e91221512826e2947d5501c135fb.jpg", "https://files.alnair.ae/uploads/2023/9/3e/a7/3ea7aa4d07ae19cc1ece91741e2a8794.jpg", "https://files.alnair.ae/uploads/2023/9/28/ca/28ca0fcf44042333acb801c0ea4f6b28.jpg", "https://files.alnair.ae/uploads/2023/9/d1/98/d198d8b52fea23dcc4661d7deaaec1d3.jpg", "https://files.alnair.ae/uploads/2023/9/bf/6e/bf6e564e7d64ae80428817b87ed4f369.jpg", "https://files.alnair.ae/uploads/2023/9/d5/43/d543724150f8b73024e442d504e7b572.jpg", "https://files.alnair.ae/uploads/2023/9/01/07/010742b59dacb5e82c8393b83e3d6ddf.jpg", "https://files.alnair.ae/uploads/2023/9/ea/46/ea46106568657ffabbf826244d4df3f7.jpg", "https://files.alnair.ae/uploads/2023/9/ce/49/ce496b199d24a7ecfd81ec27f8de993f.jpg", "https://files.alnair.ae/uploads/2023/9/9f/f2/9ff276e12437dfcad5e5b809e51237ed.jpg", "https://files.alnair.ae/uploads/2023/9/b6/81/b6810acf7fb1c9380c60db5363f605b1.jpg", "https://files.alnair.ae/uploads/2023/9/47/82/478221274ffadc81385ef3f649b9d8b2.jpg"]}}]"""
listing.buildings_count = 1
listing.for_sale_count = 0
listing.price_a_min = None
listing.price_a_max = None
listing.price_a_currency = """AED"""
listing.br_prices = None
listing.updated_at = """2023-09-20T12:55:15+04:00"""
listing.is_sold_out = 1
listing.listing_payment_plans = """[{"id": "553", "title": {"ru": "План оплаты", "en": "Payment Plan", "ar": "خطة الدفع"}, "on_booking_percent": "15", "on_booking_fix": null, "on_construction_percent": "55", "on_construction_fix": null, "on_construction_payments_count": "5", "on_handover_percent": "30", "on_handover_fix": null, "on_handover_payments_count": "1", "post_handover_percent": null, "post_handover_fix": null, "on_post_handover_payments_count": "0", "additional": {"title": {"ru": "DLD", "en": "DLD", "ar": "DLD"}, "percent": "4", "fix": null}, "additional_percent": "4", "additional_fix": "0", "roi_percent": null, "roi_fix": null, "roi_payments_count": "0", "currency": "AED", "period_after_handover": {"period": null, "count": null, "repeat_count": null}, "period_after_roi": {"period": null, "count": null, "repeat_count": null}}]"""
listing.sales_status_a_ru = """В продаже"""
listing.sales_status_a_en = """On Sale"""
listing.sales_status_a_ar = """معروض للبيع"""
listing.stocks = None
listing.eoi_a_is_eoi_return = None
listing.eoi_a_eoi_items = None
listing.service_charge = None
listing.assignment = None
listing.save()
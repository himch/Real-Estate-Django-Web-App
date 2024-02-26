from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django_admin_geomap import geomap_context

from developers.models import Developer
from listings.models import Listing
from our_company.models import OurCompany
from pages.utils import is_htmx


def developer(request, slug):
    our_company = OurCompany.objects.all().first()

    developer_item = get_object_or_404(Developer, slug=slug)
    realtor = developer_item.realtor

    listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, developer=developer_item.pk)
    len_listings = listings.count()

    # url для htmx подгрузки
    request_get = request.GET.copy()
    if 'page' in request_get:
        request_get['page'] = str(int(request_get['page']) + 1)
    else:
        request_get['page'] = '2'  # следующая страница
    htmx_url = request_get.urlencode()

    # разбиение обьектов на порции-страницы для отображения в виде списка
    page = request.GET.get('page')
    paginator = Paginator(listings, 8)
    paged_listings = paginator.get_page(page)

    # точки на карте для обьектов недвижимости
    geo_context = geomap_context(listings, auto_zoom="12" if len_listings == 1 else "15")

    context = {
        'our_company': our_company,
        'developer': developer_item,
        'listings': paged_listings,
        'len_listings': len(listings),
        'realtor': realtor,
        'htmx_url': htmx_url,
    }
    context.update(geo_context)

    if is_htmx(request):
        return render(request,
                      "includes/buy/buy_loaded_block.html",
                      {"listings": paged_listings,
                       'len_listings': len_listings,
                       'htmx_url': htmx_url,
                       }
                      )
    return render(request, 'includes/content/zastroischik.html', context)


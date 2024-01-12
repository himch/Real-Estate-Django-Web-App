from django.urls import path
from django.conf.urls.static import static

from realestate import settings
from . import views

urlpatterns = [
    # path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('rent/<int:listing_id>', views.rent, name='rent'),
    path('search', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
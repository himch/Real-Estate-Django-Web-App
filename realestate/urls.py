from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include, url

# admin.autodiscover()

urlpatterns = [
    path('i18n', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]
urlpatterns += i18n_patterns(
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    prefix_default_language=True,
)

# i18n_urls = (
#     url(r'^i18n/', include('django.conf.urls.i18n')),
# )
#
# urlpatterns = [
#     path('', include('pages.urls')),
#     path('listings/', include('listings.urls')),
#     path('accounts/', include('accounts.urls')),
#     path('contacts/', include('contacts.urls')),
#     path('admin/', admin.site.urls),
# ]
#
# urlpatterns.extend(i18n_patterns(*i18n_urls, prefix_default_language=False))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL_1, document_root=settings.MEDIA_ROOT_1)

# urlpatterns = i18n_patterns(urlpatterns)

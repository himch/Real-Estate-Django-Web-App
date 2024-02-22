from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import include

from accounts.views import UserProfileAPIView
from listings.views import *

# admin.autodiscover()

handler404 = "realestate.views.page_not_found_view"

urlpatterns = [
    path('i18n', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('api/v1/listinglist/', ListingAPIView.as_view()),
    path('api/v1/offers/buy/', OffersBuyAPIView.as_view()),
    path('api/v1/offers/<int:listing_id>/bookmark/', BookmarkAPIView.as_view(model=Bookmark), name='listing_bookmark'),
    path('api/v1/offers/<int:listing_id>/favorite/', BookmarkAPIView.as_view(model=Favorite), name='listing_favorite'),
    path('api/v1/offers/bookmarks/', BookmarksAPIView.as_view(model=Bookmark), name='user_bookmarks'),
    path('api/v1/offers/favorites/', BookmarksAPIView.as_view(model=Favorite), name='user_favorites'),
    path('api/v1/htmx/offers/<int:complex_id>/bookmark/', BookmarkHTMXAPIView.as_view(model='Bookmark'), name='listing_bookmark_htmx'),
    path('api/v1/htmx/offers/<int:complex_id>/favorite/', BookmarkHTMXAPIView.as_view(model='Favorite'), name='listing_favorite_htmx'),
    path('api/v1/htmx/offers/bookmarks/', BookmarksHTMXAPIView.as_view(model='Bookmark'), name='user_bookmarks_htmx'),
    path('api/v1/htmx/offers/favorites/', BookmarksHTMXAPIView.as_view(model='Favorite'), name='user_favorites_htmx'),
    path('api/v1/user/profile/', UserProfileAPIView.as_view(), name='user_profile'),
    path('tinymce/', include('tinymce.urls')),
    path('', include('drfpasswordless.urls')),
]
urlpatterns += i18n_patterns(
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
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

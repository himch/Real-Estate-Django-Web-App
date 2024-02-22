from django_admin_geomap import geomap_context
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404, render
from django_htmx.http import retarget, reswap, trigger_client_event

from rest_framework import generics, status
from rest_framework.response import Response
from pages.utils import check_number_var, is_htmx

from listings.models import Listing, Bookmark, Favorite
from listings.serializers import ListingSerializer, ListingFavoriteSerializer


class BookmarkHTMXAPIView(generics.GenericAPIView):
    # добавляем или удаляем обьект из закладок и возвращаем код для символа на карточке товара
    model = None

    def get_bookmark(self, user, complex_id):
        try:
            if self.model == 'Bookmark':
                bookmark = user.profile.bookmarks.all().get(complex_id=complex_id)
            elif self.model == 'Favorite':
                bookmark = user.profile.favorites.all().get(complex_id=complex_id)
        except Listing.DoesNotExist:
            bookmark = None
        return bookmark

    def add_bookmark(self, user, listing_object):
        if self.model == 'Bookmark':
            user.profile.bookmarks.add(listing_object)
        elif self.model == 'Favorite':
            user.profile.favorites.add(listing_object)

    def remove_bookmark(self, user, listing_object):
        if self.model == 'Bookmark':
            user.profile.bookmarks.remove(listing_object)
        elif self.model == 'Favorite':
            user.profile.favorites.remove(listing_object)

    def get_serializer_class(self):
        return ListingFavoriteSerializer

    def delete(self, request, complex_id):
        if is_htmx(request):
            user = auth.get_user(request)
            listing_object = Listing.objects.get(complex_id=complex_id)
            template_name = "includes/bookmarks/bookmarks_map.html"
            bookmark = self.get_bookmark(user, complex_id)
            if bookmark:
                self.remove_bookmark(user, listing_object)
            geo_context = geomap_context(user.profile.bookmarks.all(), auto_zoom="20")
            context = {"user": user, "bookmarked": False}
            context.update(geo_context)
            response = render(request,
                              template_name,
                              context
                              )
            trigger_client_event(response, "updateBookmarks", {}, )
            return response

    def post(self, request, complex_id):
        user = auth.get_user(request)
        template_name = "includes/bookmarks/icon_mark.html"

        if not isinstance(user, AnonymousUser):
            listing_object = Listing.objects.get(complex_id=complex_id)
            bookmark = self.get_bookmark(user, complex_id)

            if bookmark:
                self.remove_bookmark(user, listing_object)
                created = False
            else:
                self.add_bookmark(user, listing_object)
                created = True

            geo_context = geomap_context((user.profile.bookmarks.all(),), auto_zoom="20")

            if is_htmx(request):
                context = {"user": user, "bookmarked": created}
                context.update(geo_context)
                response = render(request,
                                  template_name,
                                  context
                                  )
                trigger_client_event(response, "updateBookmarks", {}, )
                return response

            if created:
                return Response(
                    {"result": 'added',
                     "bookmarked": created,
                     'message': f'Offer added to {self.model}'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"result": 'deleted',
                     "bookmarked": created,
                     'message': f'Offer deleted from {self.model}'},
                    status=status.HTTP_200_OK
                )
        else:
            if is_htmx(request):
                response = render(request,
                                  template_name,
                                  {"user": user, "bookmarked": False}
                                  )
                trigger_client_event(response, "updateBookmarks", {}, )
                return response
            return Response(
                {"result": 'error',
                 "bookmarked": False,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )

    def get(self, request, complex_id):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            listing_object = Listing.objects.get(complex_id=complex_id)
            bookmark = self.get_bookmark(user, complex_id)
            if bookmark:
                return Response(
                    {"result": 'bookmarked',
                     "bookmarked": True,
                     'message': f'Offer bookmarked in {self.model}'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"result": 'not bookmarked',
                     "bookmarked": False,
                     'message': f'Offer not bookmarked in {self.model}'
                     },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                {"result": 'error',
                 "bookmarked": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class BookmarksHTMXAPIView(generics.GenericAPIView):
    # возвращаем html c количеством bookmarks для шапки сайта
    model = None

    def get_count(self, user):
        if self.model == 'Bookmark':
            count = user.profile.bookmarks.all().count()
        elif self.model == 'Favorite':
            count = user.profile.favorites.all().count()
        else:
            count = 0
        return count

    def get(self, request):
        user = auth.get_user(request)
        template_name = "includes/header/icon_count.html"

        if not isinstance(user, AnonymousUser):
            count = self.get_count(user)
            if is_htmx(request):
                return render(request,
                              template_name,
                              {"user": user, "count": count}
                              )
            return Response(
                {"result": 'success',
                 "count": count,
                 'message': f'All offers for current user in {self.model}'},
                status=status.HTTP_200_OK
            )
        else:
            if is_htmx(request):
                return render(request,
                              template_name,
                              {"count": 0}
                              )
            return Response(
                {"result": 'error',
                 "count": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )


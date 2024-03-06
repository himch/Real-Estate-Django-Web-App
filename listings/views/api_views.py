from functools import reduce
import operator
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from pages.utils import check_number_var, is_htmx

from listings.models import Listing, Bookmark, Favorite
from listings.serializers import ListingSerializer, ListingFavoriteSerializer


class ListingAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


# POST /api/v1/offers/<int:listing_id>/bookmark/  - добавить/удалить обьект с указанным id в сравнение для текущего пользователя.
# Возвращает {"result": ['added' если добавлен, 'deleted' если удален, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в сравнении для данного пользователя или 0, если пользователь не авторизован]}
#
# GET /api/v1/offers/bookmarks/  - информация об обьектах в сравнении для текущего пользователя.
# Возвращает {"result": ['success' если успешно, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в сравнении для данного пользователя или 0, если пользователь не авторизован]}
#
# POST /api/v1/offers/<int:listing_id>/favorite/  - добавить/удалить обьект с указанным id в избранное для текущего пользователя.
# Возвращает {"result": ['added' если добавлен, 'deleted' если удален, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в избранном для данного пользователя или 0, если пользователь не авторизован]}
#
# GET /api/v1/offers/favorites/  - информация об обьектах в избранном для текущего пользователя.
# Возвращает {"result": ['success' если успешно, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в избранном для данного пользователя или 0, если пользователь не авторизован]}


class OffersBuyAPIView(generics.GenericAPIView):
    # queryset = Listing.objects.all()
    # serializer_class = ListingSerializer

    # def get_queryset(self, *args, **kwargs):
    #     queryset = Listing.objects.all()
    #     return queryset

    def get(self, request, *args, **kwargs):
        try:

            price_min = check_number_var(request.query_params, 'price_min', result_type_str=False)
            price_max = check_number_var(request.query_params, 'price_max', result_type_str=False)
            estate_types = list(sorted(Listing.sell_objects.values_list('type', flat=True).distinct()))
            filters = list(
                Q(type=estate_type) for estate_type in estate_types if
                'estate_type_' + estate_type in request.query_params)

            queryset = Listing.sell_objects.all()
            if filters:
                q = reduce(operator.or_, filters)
                queryset = queryset.filter(q)

            if price_max:
                q = Q(price_a_min__gte=price_min) & Q(price_a_min__lte=price_max)
            else:
                if price_min:
                    q = Q(price_a_min__gte=price_min)
                else:
                    q = None
            if q:
                queryset = queryset.filter(q)

            count = queryset.count()
            return Response({'count': count}, status=status.HTTP_200_OK)

        except Exception as e:
            print('Exception', e)
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    # def post(self, request):
    #     listing_data = request.data
    #     new_listing = Listing.objects.create(
    #         title=listing_data['title'],
    #     )
    #     new_listing.save()
    #
    #     serializer = ListingSerializer(new_listing)
    #     return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
    #     id = request.query_params["id"]
    #     listing_object = Listing.objects.get(id=id)
    #
    #     data = request.data
    #
    #     listing_object.title = data["title"]
    #     listing_object.save()
    #
    #     serializer = ListingSerializer(listing_object)
    #     return Response(serializer.data)

    # def patch(self, request, *args, **kwargs):
    #     id = request.query_params["id"]
    #     listing_object = Listing.objects.get(id=id)
    #
    #     data = request.data
    #
    #     listing_object.title = data.get('title', listing_object.title)
    #     listing_object.save()
    #     serializer = ListingSerializer(listing_object)
    #     return Response(serializer.data)


class BookmarkAPIView(generics.GenericAPIView):
    model = None

    def get_serializer_class(self):
        return ListingFavoriteSerializer

    def post(self, request, listing_id):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            bookmark, created = self.model.objects.get_or_create(user=user, listing_id=listing_id)
            if not created:
                bookmark.delete()

            if created:
                return Response(
                    {"result": 'added',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer added to {self.model._meta.verbose_name_plural.title()}'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"result": 'deleted',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer deleted from {self.model._meta.verbose_name_plural.title()}'},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"result": 'error',
                 "count": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )

    def get(self, request, listing_id):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            try:
                bookmark = self.model.objects.get(user=user, listing_id=listing_id).first
            except self.model.DoesNotExist:
                bookmark = None
            if bookmark:
                return Response(
                    {"result": 'bookmarked',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer bookmarked in {self.model._meta.verbose_name_plural.title()}'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"result": 'not bookmarked',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer not bookmarked in {self.model._meta.verbose_name_plural.title()}'
                     },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                {"result": 'error',
                 "count": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class BookmarksAPIView(generics.GenericAPIView):
    model = None

    def get(self, request):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            return Response(
                {"result": 'success',
                 "count": self.model.objects.filter(user=user).count(),
                 'message': f'All offers for current user in {self.model._meta.verbose_name_plural.title()}'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"result": 'error',
                 "count": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )


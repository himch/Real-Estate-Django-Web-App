from rest_framework import serializers
from .models import Listing, Favorite, Bookmark


class ListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Listing
		fields = ('title_a_en', 'offer_type', 'complex_id')


class ListingFavoriteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Favorite
		fields = '__all__'


class ListingBookmarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bookmark
		fields = '__all__'


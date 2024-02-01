from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Listing
		fields = ('title_a_en', 'offer_type', 'complex_id')
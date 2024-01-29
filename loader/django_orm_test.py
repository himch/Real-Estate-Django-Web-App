import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
import django
django.setup()
from listings.models import Listing

listings = Listing.objects.all()
for listing in listings:
    listing.save_albums()

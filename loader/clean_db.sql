DELETE FROM listings_mainalbumimage WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_mainalbumimage.album_id = listings_listing.id);
DELETE FROM listings_additional WHERE listings_additional.payment_plan_id IN (SELECT id FROM listings_paymentplan WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_paymentplan.listing_id = listings_listing.id));
DELETE FROM listings_paymentplan WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_paymentplan.listing_id = listings_listing.id);
DELETE FROM listings_price WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_price.listing_id = listings_listing.id);
DELETE FROM listings_image WHERE listings_image.album_id IN (SELECT id FROM listings_album WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_album.listing_id = listings_listing.id));
DELETE FROM listings_album WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_album.listing_id = listings_listing.id);
DELETE FROM listings_amenity WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_amenity.listing_id = listings_listing.id);
DELETE FROM listings_district WHERE NOT EXISTS (SELECT 1 FROM listings_listing WHERE listings_district.listing_id = listings_listing.id);
from django.urls import path
from tourist.api.views import(
	tourist_view,all_tourist_places,particular_place
)



app_name = 'account'

urlpatterns = [
	path('tourist_place/', tourist_view, name="tourist_place"), #Api end point to add tourist places(POST request)
    path('all_tourist_places/', all_tourist_places, name="all_tourist_places"), #Api end point to GET all tourist places from database
	# path('booking/', booking_view, name="booking"), #Api end point to book any tourist places(POST/PUT request)
	path('all_tourist_places/<int:place_id>', particular_place, name="particular_place"),
]


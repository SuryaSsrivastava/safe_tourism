from django.urls import path
from tourist.api.views import(
	tourist_view,all_tourist_places
)



app_name = 'account'

urlpatterns = [
	path('tourist_place/', tourist_view, name="tourist_place"), #Api end point to add tourist places(POST request)
    path('all_tourist_places/', all_tourist_places, name="all_tourist_places"), #Api end point to GET all tourist places from database
]

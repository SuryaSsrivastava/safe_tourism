from django.urls import path
from tourist.api.views import(
	tourist_view,all_tourist_places
)



app_name = 'account'

urlpatterns = [
	path('tourist_places/', tourist_view, name="tourist_places"),
    path('all_tourist_places/', all_tourist_places, name="all_tourist_places"),
]


from django.urls import path
from account.api.views import(
	registration_view,profile_create,login
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [

		path('register/', registration_view, name="register"),  #Api to register a new USER to our APP(POST request)
		path('profile/', profile_create,name='profile'), #Api to create a profile after registering(POST request)
		path('login/', login, name="login"), # Api to verify where a user is a valid User or Not(POST request)
]


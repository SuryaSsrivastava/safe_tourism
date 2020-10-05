from django.urls import path
from account.api.views import(
	registration_view,profile_create,login
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('register/', registration_view, name="register"),
	 path('profile/', profile_create,name='profile'),
	path('login/', login, name="login"),
]


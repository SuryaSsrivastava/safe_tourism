from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from account.api.serializers import RegistrationSerializer,ProfileSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.views.decorators.csrf import csrf_exempt

#Registration for New User
@api_view(['POST', ])
@permission_classes((AllowAny,))
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['id'] = account.id
			data['success'] = True
			data['id'] = account.id
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)

#Creating profile Once User is registered
@api_view(['POST'])
def profile_create(request):
  serializer = ProfileSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return JsonResponse({'success':True,"data":serializer.data})
  return JsonResponse({'success':False,'message':"user doesn't exist"} )


#Checking for valid User
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
	user = request.data.get("email")
	password = request.data.get("password")
	print(user,password)
	if user is None or password is None:
		return Response({'success':False,'message': 'Please provide both email and password'},
						status=HTTP_400_BAD_REQUEST)
	user = authenticate(username=user, password=password)
	if not user:
		return Response({'success':False,'message': 'Invalid Credentials'},
						status=HTTP_404_NOT_FOUND)
	token, _ = Token.objects.get_or_create(user=user)
	return Response({'success':True,'token': token.key},
					status=HTTP_200_OK)

from tourist.api.serializers import bookingSerializer,tourist_placeSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from tourist.models import tourist_place,booking
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated,AllowAny
# import requests 

@api_view(['POST'])
@permission_classes((AllowAny,))
def tourist_view(request):

    serializer = tourist_placeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success':True,"data":serializer.data})
    return JsonResponse({'success':False,'message':serializer.errors} )

@api_view(['GET'])
@permission_classes((AllowAny,))
def all_tourist_places(request):
    queryset = tourist_place.objects.all().order_by('id')
    serializer_class = tourist_placeSerializer
    d = {}
    d['success'] =True
    j=[]
    d['data'] = j
    for i in queryset.values():
        d['data'].append(i)
    return JsonResponse(d)

@api_view(['GET'])
@permission_classes((AllowAny,))
def particular_place(request,id):
    queryset = tourist_place.objects.filter(id=id)
    if not queryset:
        return JsonResponse({'success':False,'message':"place not found"})
    temp = queryset
   
    return JsonResponse({'success':True,'data':temp.values()[0]})

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def booking_view(request):
    
    if request.method == 'POST':
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()  
            id = book.id
            user = book.user_id
            d= {}
            d['user'] = str(user)
            d['place_name'] = str(id)
            return JsonResponse({'success':True,"data":d})
        else:
            return JsonResponse({'success':False})
   
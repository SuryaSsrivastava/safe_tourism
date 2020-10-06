from tourist.api.serializers import bookingSerializer,tourist_placeSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from tourist.models import tourist_place,booking
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated,AllowAny
import requests 

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
    queryset = tourist_place.objects.all().order_by('place_id')
    serializer_class = tourist_placeSerializer
    d = {}
    d['success'] =True
    j=[]
    d['data'] = j
    for i in queryset.values():
        d['data'].append(i)
    #corona Api

    # url = "https://coronavirus-19-api.herokuapp.com/countries"
    # data = requests.get(url)
    # serverError = False
    # try:
    #     data = data.json()
    # except :
    #     serverError = {"message" : 'server_error'}
    #     return JsonResponse(serverError)
    # cases,todayCases,deaths,recovered =0,0,0,0
    # error = False
    # country = "Global"
    
    # if request.method == "POST" and not request.POST["country"]=="":
    #     for x in data:
    #         if x.get("country").lower()== request.POST["country"].lower():
    #             cases += x["cases"]
    #             todayCases += x["todayCases"] 
    #             deaths += x["deaths"]
    #             recovered += x["recovered"]
    #             country = x["country"]
    #             error = False
    #             break
    #         else:
    #             error = True
    #             continue
    # else:
    #     for x in data:
    #         error = False
    #         try:
    #             todayCases += x["todayCases"]
    #         except:
    #             todayCases +=0
    #         try:
    #             cases += x["cases"]
    #         except:
    #             cases +=0
    #         try:
    #             deaths += x["deaths"]
    #         except:
    #             deaths +=0
    #         try:
    #             recovered += x["recovered"]
    #         except:
    #             recovered +=0
    # if error : 
    #     data = {"error":error,"cases" : cases,"todayCases":todayCases,"deaths":deaths,"recovered":recovered,"country":country}
    # else :
    #     data = {"cases" : cases,"todayCases":todayCases,"deaths":deaths,"recovered":recovered,"country":country}



    return JsonResponse(d)

@api_view(['GET'])
@permission_classes((AllowAny,))
def particular_place(request,place_id):
    queryset = tourist_place.objects.filter(place_id=place_id)
    if not queryset:
        return JsonResponse({'success':False,'message':"place not found"})
    temp = queryset
   
    return JsonResponse({'success':True,'data':temp.values()[0]})


# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def booking_view(request):

#     if request.method == 'POST':
#         serializer = bookingSerializer(data=request.data)
#         if serializer.is_valid():
#             max_limit =  tourist_place.objects.all()
#             curr_booking =  tourist_place.objects.all()
#             # print("max_limit",max_limit)
#             print("curr_booking",curr_booking)
#             return JsonResponse({'message':"hello"})
    # if request.method =='POST':
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({'success':True,"data":serializer.data})
    #     return JsonResponse({'success':False,'message':serializer.errors} )

    # else:
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({'success':True,"data":serializer.data})
    #     return JsonResponse({'success':False,'message':serializer.errors} )


   
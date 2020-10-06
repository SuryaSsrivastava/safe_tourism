from tourist.api.serializers import bookingSerializer,tourist_placeSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from tourist.models import tourist_place,booking
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated,AllowAny


@api_view(['POST'])
@permission_classes((AllowAny,))
def tourist_view(request):

    serializer = tourist_placeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success':True,"data":serializer.data})
    return JsonResponse({'success':False,'message':serializer.errors} )

@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def all_tourist_places(request):
    queryset = tourist_place.objects.all().order_by('place_id')
    serializer_class = tourist_placeSerializer
    d = {}
    js = []
    d['success'] = True
    d['data'] = js
    temp = {}
    l = ['place_id','place_name','location','max_limit','curr_booking','violation_found']
    for p in queryset:
        for j,val in enumerate(str(p).split(".")):
            
            temp[l[j]] = val

        d['data'].append(temp)
        
        temp={}
    # print(d)
    return JsonResponse(d)

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


   
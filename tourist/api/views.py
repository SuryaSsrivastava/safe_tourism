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
@permission_classes((IsAuthenticated,))
def all_tourist_places(request):
    queryset = tourist_place.objects.all().order_by('place_id')
    serializer_class = tourist_placeSerializer
    serializer = tourist_placeSerializer(tourist_place)
    d = {}
    js = {}
    count = 0
    l = ['place_id','place_name','location','max_limit','curr_booking','violation_found']
    for p in queryset:
        for j,val in enumerate(str(p).split(".")):
            
            d[l[j]] = val

        js[str(count)] = d
        count+=1
        d={}

    return JsonResponse(js)

   
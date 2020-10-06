from rest_framework import serializers
from tourist.models import tourist_place,booking


#What to show when a user clicks this Api
class tourist_placeSerializer(serializers.ModelSerializer):
    class Meta:
        model=tourist_place
        fields=('place_id','place_name','location','max_limit','curr_booking','violation_found')

    def to_representation(self, instance):
        # self.fields['place_id'] =  tourist_placeSerializer(read_only=True)
        return super(tourist_placeSerializer, self).to_representation(instance)

#what to show when a user clicks this Api
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=booking
        fields=('booking_id','user_id','place_id')
        # read_only_fields = ('created','updated')

    def to_representation(self, instance):
        # self.fields['booking_id'] =  bookingSerializer(read_only=True)
        return super(bookingSerializer, self).to_representation(instance)
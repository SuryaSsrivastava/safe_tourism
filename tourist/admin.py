from django.contrib import admin
from tourist.models import tourist_place,booking
# Register your models here.

class tourist_placesAdmin(admin.ModelAdmin):
    	list_display = ('id','place_name','place_detail','location','max_limit','curr_booking','violation_found','global_cases',
		'today_cases','deaths','recovered')

class bookingsAdmin(admin.ModelAdmin):
    	list_display = ('id','user_id','place_id')

admin.site.register(tourist_place, tourist_placesAdmin)
admin.site.register(booking,bookingsAdmin)

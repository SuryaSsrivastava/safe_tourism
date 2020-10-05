from django.db import models
from account.models import Account

# Create your models here.

class tourist_place(models.Model):
    place_id                = models.IntegerField(primary_key=True)
    place_name 				= models.CharField(max_length=60, unique=False,default='')
    location 				= models.CharField(max_length=30, unique=False,default='')
    max_limit				= models.CharField(max_length=20,default='50')
    curr_booking			= models.CharField(max_length=20,default='0')
    violation_found         = models.CharField(max_length=20,unique=False,default='0')

    def __str__(self):
        return (str(self.place_id)+"."+str(self.place_name)+"."+str(self.location)+"."+str(self.max_limit)+"."+str(self.curr_booking)+"."+str(self.violation_found))

class booking(models.Model):
    booking_id              = models.IntegerField(primary_key=True)
    user_id                 = models.ForeignKey(Account,on_delete=models.CASCADE)
    place_id                = models.ForeignKey(tourist_place,on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.booking_id)
    


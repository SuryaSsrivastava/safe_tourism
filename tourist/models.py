from django.db import models
from account.models import Account

# Create your models here.

class tourist_place(models.Model):
    place_id                = models.AutoField(primary_key=True)
    place_name 				= models.CharField(max_length=60, unique=False,default='')
    place_detail            = models.CharField(max_length=1000,unique=False,default="")
    location 				= models.CharField(max_length=30, unique=False,default='')
    max_limit				= models.CharField(max_length=20,default='50')
    curr_booking			= models.CharField(max_length=20,default='0')
    violation_found         = models.CharField(max_length=20,unique=False,default='0')
    global_cases            = models.CharField(max_length=20,default='0')
    today_cases             = models.CharField(max_length=20,default='0')
    deaths                  = models.CharField(max_length=20,default='0')
    recovered               = models.CharField(max_length=20,default='0')


    def __str__(self):
        return self.place_name

class booking(models.Model):
    booking_id              = models.AutoField(primary_key=True)
    user_id                 = models.ForeignKey(Account,on_delete=models.CASCADE)
    place_id                = models.ForeignKey(tourist_place,on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.booking_id)
    


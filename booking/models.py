from traceback import StackSummary
from django.db import models

# from garage.views import vehicle_view
from django.contrib.auth.models import User , auth 

from garage.models import add_vehicle, vehicle
from garage.views import vehicle_view
from service.models import price_model


class cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,default="N/A")
    vehicle = models.ForeignKey(vehicle,on_delete=models.CASCADE,null=True)
    service = models.CharField(max_length=255)  
    package =models.CharField(max_length=255)  
    price_model = models.ForeignKey(price_model , on_delete=models.CASCADE,null=True)
    # date = models.DateField(null=True)
    # states =  models.BooleanField(null=True)

    # def __str__(self) :
        # return self.vehicle


class booking(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,default="N/A")
    vehicle = models.ForeignKey(vehicle,on_delete=models.CASCADE,null=True)
    service = models.CharField(max_length=255)  
    package =models.CharField(max_length=255)  
    price_model = models.ForeignKey(price_model , on_delete=models.CASCADE,null=True)
    number =models.CharField(max_length=255 , null = True) 
    address =models.CharField(max_length=255 , null = True) 
    date = models.DateField(null=True)
    states =  models.BooleanField(null=True)

    # def __str__(self) :
        # return self.vehicle
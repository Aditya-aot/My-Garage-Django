from django.db import models

# from garage.views import vehicle_view
from django.contrib.auth.models import User , auth 


# Create your models here.


class brands(models.Model):
    title = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
   
    def __str__(self) :
        return self.title    


class vehicle(models.Model):
    brand = models.ForeignKey(brands, on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    def __str__(self) :
        return self.name

class add_vehicle(models.Model):
    vehicle = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    # image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    

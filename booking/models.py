from traceback import StackSummary
from django.db import models

# from garage.views import vehicle_view
from django.contrib.auth.models import User , auth 

from garage.models import vehicle


class regular(models.Model):
    vehicle   = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    price     = models.TextField(null = True) 
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

class running_repair(models.Model):
    vehicle   = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    price     = models.TextField(null = True) 
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

class washing_and_cleaning(models.Model):
    vehicle   = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    price     = models.TextField(null = True) 
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

class brakes(models.Model):
    vehicle   = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    price     = models.TextField(null = True) 
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

class cable_replacement(models.Model):
    vehicle   = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    price     = models.TextField(null = True) 
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

class battery(models.Model):
    vehicle   = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    price     = models.TextField(null = True) 
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)


class tyres(models.Model):
    vehicle   = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    price     = models.TextField(null = True) 
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

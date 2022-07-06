from traceback import StackSummary
from django.db import models

# from garage.views import vehicle_view
from django.contrib.auth.models import User , auth 

from garage.models import vehicle



class regular(models.Model):
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)   
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

    def __str__(self) :
        return self.title  

class running_repair(models.Model):
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

    def __str__(self) :
        return self.title 

class washing_and_cleaning(models.Model):
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

    def __str__(self) :
        return self.title 

class brakes(models.Model):
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

    def __str__(self) :
        return self.title 

class cable_replacement(models.Model):
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

    def __str__(self) :
        return self.title 

class battery(models.Model):
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

    def __str__(self) :
        return self.title 


class tyres(models.Model):
    title     = models.TextField(null = True)  
    Summary   = models.TextField(null = True)  
    image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
    discription = models.TextField(null = True)

    def __str__(self) :
        return self.title 


# class service(models.Model) :
#     name         =models.TextField(null = True) 
#     def __str__(self) :
#         return self.name


# class package(models.Model) :
#     service   = models.ForeignKey(service, on_delete=models.CASCADE, null = True)
#     title     = models.TextField(null = True)  
#     Summary   = models.TextField(null = True)  
#     image     = models.ImageField(upload_to='uploads/', blank=True, null=True) 
#     discription = models.TextField(null = True)

#     def __str__(self) :
#         return self.title


class price_model(models.Model) :
    vehicle      = models.ForeignKey(vehicle, on_delete=models.CASCADE, null = True)
    regular              = models.ForeignKey(regular, on_delete=models.CASCADE, null=True,blank=True)
    running_repair       = models.ForeignKey(running_repair, on_delete=models.CASCADE, null=True,blank=True)
    washing_and_cleaning  = models.ForeignKey( washing_and_cleaning, on_delete=models.CASCADE, null=True,blank=True)
    brakes               = models.ForeignKey(brakes, on_delete=models.CASCADE, null=True,blank=True)
    cable_replacement  = models.ForeignKey(cable_replacement, on_delete=models.CASCADE, null=True,blank=True)
    battery             = models.ForeignKey(battery, on_delete=models.CASCADE, null=True,blank=True)
    tyres               = models.ForeignKey(tyres, on_delete=models.CASCADE, null=True,blank=True)
    price         = models.TextField(null = True)


    def __str__(self) :
        return self.price




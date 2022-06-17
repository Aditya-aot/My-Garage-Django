from django.db import models

# Create your models here.


class brands(models.Model):
    title = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    


class vehicle(models.Model):
    brand = models.ForeignKey(brands, on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    

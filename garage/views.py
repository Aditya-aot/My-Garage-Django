from turtle import title
from unicodedata import name
from django.shortcuts import render

from .models import brands ,vehicle


# Create your views here.


def welcome(request) :

    context = {}
    return render(request, 'garage/welcome.html',context)


def home(request) :

    context = {}
    return render(request, 'garage/home.html',context)



def brand(request) :
    brand_name = brands.objects.all()

    context = {
                'brand' : brand_name 
    }
    return render(request, 'garage/brands.html',context)


def vehicle_view(request,pk) :
    vehicle_name = vehicle.objects.all()
    brand_vehicle = vehicle_name.filter(brand_id=pk)
    print('-------------------->>>>>>>>>>>>>>>>',brand_vehicle)
    context = {'vehi':brand_vehicle}
    return render(request, 'garage/vehicle.html',context)






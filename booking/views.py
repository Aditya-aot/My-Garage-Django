
from django.shortcuts import render ,redirect

from .models import  regular , running_repair , washing_and_cleaning , brakes , cable_replacement , battery, tyres


# Create your views here.


def service_view(request,pk) :

    list_of_service = ['regular' , 'running_repair' , 'washing_and_cleaning' , 'brakes' , 'cable_replacement' , 'battery', 'tyres']

    context = {
            'list':list_of_service
    }
    return render(request, 'booking/service.html',context)


def service_detail(request,pk) :

    pk=eval(pk)
    obj = pk.objects.all()
    
    context = {
          'obj':obj,
    }
    return render(request, 'booking/service_detail.html',context)


from django.shortcuts import render ,redirect
from garage.models import vehicle
from garage.views import add, vehicle_view



from .models import  price_model,regular , running_repair , washing_and_cleaning , brakes , cable_replacement , battery, tyres 
from garage.models import add_vehicle 
from booking.models import cart

# Create your views here.



def service_view(request,pk) :

    list_of_service = ['regular' , 'running_repair' , 'washing_and_cleaning' , 'brakes' , 'cable_replacement' , 'battery', 'tyres']
    price = price_model.objects.all()
    service_vehicle = [pk,pk,pk,pk,pk,pk,pk]

    obj = zip(list_of_service,service_vehicle)

    context = {
            'list':list_of_service,
            'vehicle':service_vehicle ,
            'obj' : obj ,
            'user_vehicle' : pk
    }
    return render(request, 'service/service.html',context)


def service_detail(request,pk,id) :

    pk_class=eval(pk)
    obj = pk_class.objects.all()
    # price = price_model.objects.all()
    # price_package = price.filter(pk)


    context = {
          'obj':obj,
          'service' : pk ,
          'user_vehicle' : id
    }
    return render(request, 'service/service_detail.html',context)



def confirm_booking(request,user_vehicle,pk,id) :
    pk_class=eval(pk)
    price = price_model.objects.all()
    package_name = pk_class.objects.all()
    vehicle_names = vehicle.objects.all()
    if pk == 'regular' :
        price = price.filter(regular=id,            vehicle=user_vehicle)
        package = package_name.filter(id=id).values('title')[0]['title']
        vehicle_name = vehicle_names.filter(id=user_vehicle).values('name')[0]['name']
        
    if pk == 'running_repair' :
        price = price.filter(running_repair=id,     vehicle=user_vehicle)
        package = package_name.filter(id=id).values('title')[0]['title']

    if pk == 'washing_and_cleaning' :
        price = price.filter(washing_and_cleaning=id, vehicle=user_vehicle)
        package = package_name.filter(id=id).values('title')[0]['title']
     
    if pk == 'brakes' :
        price = price.filter(brakes=id,            vehicle=user_vehicle)
        package = package_name.filter(id=id).values('title')[0]['title']

    if pk == 'cable_replacement' :
        price = price.filter(cable_replacement=id, vehicle=user_vehicle)
        package = package_name.filter(id=id).values('title')[0]['title']

    if pk == 'battery' :
        price = price.filter(battery=id,           vehicle=user_vehicle)
        package = package_name.filter(id=id).values('title')[0]['title']

    if pk == 'tyres' :
        price = price.filter(tyres=id,             vehicle=user_vehicle)
        package = package_name.filter(id=id).values('title')[0]['title']
    
    
    context = {
         'price' : price,
         'pk' :pk ,
         'user_vehicle':user_vehicle,
         'package':package
    }
    return render(request, 'service/confirm.html',context)

 
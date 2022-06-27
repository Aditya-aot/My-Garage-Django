
from django.shortcuts import render ,redirect

from .models import add_vehicle, brands ,vehicle


# Create your views here.


def welcome(request) :

    context = {}
    return render(request, 'garage/welcome.html',context)


def home(request) :

    obj = add_vehicle.objects.all()

    context = {
        'obj':obj
        }
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


def add(request , pk) :
    obj2 = add_vehicle.objects.all()


    if request.method == "POST" :
        obj = add_vehicle()
        # obj.user = request.user or None
        # obj.save()
        aa = add_vehicle( user=request.user, vehicle_id = pk)
        aa.save()



    context = {}
    # return render(request, 'garage/add.html',context)
    return redirect("/home" , context)



def my_vehicle_view(request) :
    obj = add_vehicle.objects.all()

    context = {
        'obj':obj
        }
    return render(request, 'garage/myvehicle.html',context)


def test(request) :
    return render(request, 'test/index.html')

def test2(request) :
    return render(request, 'test/index2.html')


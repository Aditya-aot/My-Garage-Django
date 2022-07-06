
from email.headerregistry import Address
from django.shortcuts import render ,redirect

from garage.views import vehicle_view
from service.models import price_model

from .models import  cart ,booking


# # Create your views here.




def add_cart(request,user_vehicle,pk,package,id) :

    if request.method =="POST" :
        user_cart = cart(user=request.user ,vehicle_id=user_vehicle,service=pk,package=package,price_model_id=id )    
        user_cart.save()

    context = {
    }
    return redirect("/booking/cart" , context)



def cart_view(request) :
    cart_model=cart.objects.all()
    cart_user = cart_model.filter(user=request.user)    

    context = {
        'cart':cart_user, 
    }
    return render(request, 'booking/cart.html',context)




def add_booking(request,user_vehicle,service,package,price) :
    
    # if request.method =="POST" :
 
    # # request.POST['username']
    #     number=request.POST.get("number",False) 
    #     address=request.POST.get("address",False) 
    #     date=request.POST.get("date",False)   
    #     print("-------------->>>>>>>>>>>",date,number,request.POST)
        
    context = {
        'user_vehicle':user_vehicle,
        'service' : service,
        'package' : package,
        'price' : price,
        # 'number':number,
        # 'address': address ,
        # 'date' : date
    }
    return render(request, 'booking/add_booking.html',context)



def add_booking_final(request,user_vehicle,service,package,price) :
    if request.method =="POST" :
 
    # request.POST['username']
        number=request.POST.get("number",False) 
        address=request.POST.get("address",False) 
        date=request.POST.get("date",False)   
        print("-------------->>>>>>>>>>>",date,number,request.POST)

    if request.method =="POST" :
        user_booking = booking(user=request.user, vehicle_id=user_vehicle, service=service , package=package, price_model_id=price ,number=number ,address=address ,date=date   )
        user_booking.save()

    context = {

    }
    return redirect("/booking" , context)


def booking_view(request) :
    
    obj_booking = booking.objects.all()
    user_booking = obj_booking.filter(user=request.user)

    context = {
        'user_booking':user_booking
    }
    return render(request, 'booking/booking.html',context)

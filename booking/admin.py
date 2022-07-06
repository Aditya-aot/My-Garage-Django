from django.contrib import admin

from garage.admin import vehicle_name
from .models import cart ,booking





class cart_name(admin.ModelAdmin) :
    list_display = ['__str__' ,'vehicle','service','package']
    list_filter =['vehicle','service','package']
    class Meta :
        model =cart

admin.site.register(cart,cart_name)



class booking_name(admin.ModelAdmin) :
    list_display = ['__str__' ,'vehicle','service','package','date','states']
    list_filter =['states','date','service','package','vehicle']
    class Meta :
        model =booking

admin.site.register(booking,booking_name)


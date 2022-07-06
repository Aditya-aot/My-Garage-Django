from django.contrib import admin
from .models import brands , vehicle , add_vehicle



class brand_name(admin.ModelAdmin) :
    list_display = ['__str__', ]
    class Meta :
        model = brands

admin.site.register(brands , brand_name)


class vehicle_name(admin.ModelAdmin) :
    list_display = ['__str__',  'brand_title' ]
    list_filter =['brand__title']
    class Meta :
        model = vehicle

    def brand_title(self, obj):
        return obj.brand.title


admin.site.register(vehicle , vehicle_name)



class add_vehicle_name(admin.ModelAdmin) :
    model = add_vehicle
    list_display = [ '__str__','user' , 'vehicle_name' , 'vehicle_brand_title']
    list_filter =['vehicle__name','vehicle__brand__title']
    
    class Meta :
        model = add_vehicle
        

    def vehicle_name(self, obj):
        return obj.vehicle.name

    def vehicle_brand_title(self, obj):
        return obj.vehicle.brand.title


admin.site.register(add_vehicle,add_vehicle_name) 
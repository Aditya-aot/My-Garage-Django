from django.contrib import admin

from django.shortcuts import render ,redirect

from .models import  price_model, regular , running_repair , washing_and_cleaning , brakes , cable_replacement , battery, tyres


# Create your views here.





class regular_name(admin.ModelAdmin) :
    list_display = ['__str__']
    class Meta :
        model =regular


class price_name(admin.ModelAdmin) :
    list_display = ['__str__' ,'price','vehicle','regular','running_repair','washing_and_cleaning','brakes','cable_replacement','battery','tyres']
    list_filter =['regular','running_repair','washing_and_cleaning','brakes','cable_replacement','battery','tyres','vehicle']
    # fields = ('price','vehicle','regular','running_repair','washing_and_cleaning','brakes','cable_replacement','battery','tyres')
    class Meta :
        model =price_model


admin.site.register(price_model ,price_name)




# admin.site.register(service_test)
# admin.site.register(ser)

admin.site.register(regular , regular_name)
admin.site.register( running_repair )
admin.site.register(washing_and_cleaning )
admin.site.register(brakes )
admin.site.register(cable_replacement)
admin.site.register(battery)
admin.site.register(tyres)

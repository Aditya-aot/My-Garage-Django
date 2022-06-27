from django.contrib import admin
from .models import regular , running_repair , washing_and_cleaning , brakes , cable_replacement , battery, tyres





class regular_name(admin.ModelAdmin) :
    list_display = ['__str__', 'vehicle_name']
    class Meta :
        model =regular
    def vehicle_name(self, obj):
        return obj.vehicle.name

admin.site.register(regular , regular_name)


admin.site.register( running_repair )
admin.site.register(washing_and_cleaning )
admin.site.register(brakes )
admin.site.register(cable_replacement)
admin.site.register(battery)
admin.site.register(tyres)

from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome , name='welcome') , 
    path('home', views.home , name='home') ,
    path('brand', views.brand , name='brand') ,
    path('vehicle/<str:pk>', views.vehicle_view , name='vehicle_view') ,
    path('add/<str:pk>', views.add , name='add') ,
    path('myvehicle', views.my_vehicle_view , name='my_vehicle_view') ,
    

]

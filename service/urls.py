from django.urls import path
from . import views


urlpatterns = [

    # path('home', views.home , name='home') ,
     path('/services/<str:pk>', views.service_view , name='service_view') ,
     path('/<str:pk>/<str:id>', views.service_detail , name='service_detail') ,
     path('/confirm/<str:user_vehicle>/<str:pk>/<str:id>',views.confirm_booking,name='confirm_booking')

]
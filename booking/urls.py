from django.urls import path
from . import views


urlpatterns = [

    # path('home', views.home , name='home') ,
     path('/services/<str:pk>', views.service_view , name='service_view') ,
     path('/<str:pk>', views.service_detail , name='service_detail') ,

]
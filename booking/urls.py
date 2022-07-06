from django.urls import path
from . import views


urlpatterns = [

#     # path('home', views.home , name='home') ,
    path('/cart/<str:user_vehicle>/<str:pk>/<str:package>/<str:id>', views.add_cart , name='add_cart') ,
    path('/cart', views.cart_view , name='cart_view') ,
    path('/<str:user_vehicle>/<str:service>/<str:package>/<str:price>', views.add_booking , name='add_booking') ,
    path('/final/<str:user_vehicle>/<str:service>/<str:package>/<str:price>', views.add_booking_final , name='add_booking_final') ,
    path('/', views.booking_view , name='booking_view') ,
]
from django.urls import path

from package_making.views import GetHotelPrice

urlpatterns = [
    path('get_hotel_price', GetHotelPrice.as_view(), name='get_hotel_price'),
]

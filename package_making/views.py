from django.http import JsonResponse
from django.views import View

from package_making.models import HotelPurchasePrice


from django.http import JsonResponse
from django.views import View
from datetime import datetime

class GetHotelPrice(View):
    def get(self, request, *args, **kwargs):
        country_id = request.GET.get('country_id')
        city_id = request.GET.get('city_id')
        hotel_id = request.GET.get('hotel_id')
        room_type_id = request.GET.get('room_type_id')
        meal = request.GET.get('meal')

        if country_id and city_id and hotel_id and room_type_id:
            result = HotelPurchasePrice.objects.filter(
                hotel__country_id=country_id,
                hotel__city_id=city_id,
                hotel_id=hotel_id,
                room_type_id=room_type_id,
                meal=meal
            ).values(
                'purchase_rate',
                'sale_rate',
                'rate_valid_from',
                'rate_valid_till',
                'currency',
            ).first()

            if result:
                date_difference = result['rate_valid_till'] - result['rate_valid_from']
                nights = date_difference.days
                cost = nights * result['sale_rate']
                result['cost'] = cost
                result['nights'] = nights
                return JsonResponse({'prices': result, 'success': True})
        return JsonResponse({'success': False})



from django.http import HttpResponse, JsonResponse
from .utils import get_center_data

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")

def center(request):
    if request.method == 'GET':
        month = request.GET.get('month', '')
        most_popular_car, most_popular_car_sales, max_car_type,max_car_type_count, max_brand, max_brand_count = get_center_data()
        return JsonResponse({
            'most_popular_car': most_popular_car,
            'most_popular_car_sales': most_popular_car_sales,
            'max_car_type': max_car_type,
            'max_car_type_count': max_car_type_count,
            'max_brand': max_brand,
            'max_brand_count': max_brand_count
        })
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import get_data_by_month
from .utils import get_center_data
from .utils import wordcloud_generate
from .utils import get_center_left_data

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")

@csrf_exempt
def center(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        month = body.get('month', '')

        car_list = get_data_by_month.get_cars_by_month(month)
        most_popular_car, most_popular_car_sales, max_car_type,max_car_type_count, max_brand, max_brand_count =(
            get_center_data.get_center_data(car_list))
        roll_list = get_center_data.get_roll_list(car_list)
        wordcloud_generate.generate_img(month)
        oil_rate, electric_rate, hybrid_rate = get_center_data.get_energe_type_rate(car_list)
        return JsonResponse({
            'most_popular_car': most_popular_car,
            'most_popular_car_sales': most_popular_car_sales,
            'max_car_type': max_car_type,
            'max_car_type_count': max_car_type_count,
            'max_brand': max_brand,
            'max_brand_count': max_brand_count,
            'roll_list': roll_list,
            'oil_rate': oil_rate,
            'electric_rate': electric_rate,
            'hybrid_rate': hybrid_rate
        })
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def center_left(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        month = body.get('month', '')
        pie_data = get_center_left_data.get_pie_type_data(month)
        return JsonResponse({
            'pie_data': pie_data
        })

from sales.models import *

def get_cars_by_month():
    # cars = CarInfo.objects.filter(month='202306').values()
    cars = CarInfo.objects.all()
    return cars

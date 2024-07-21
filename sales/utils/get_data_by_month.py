from sales.models import *

def get_cars_by_month(month):
    cars = CarInfo.objects.filter(month=month)
    # cars = CarInfo.objects.all()
    return cars

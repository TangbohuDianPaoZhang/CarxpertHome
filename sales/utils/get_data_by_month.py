from sales.models import *

def get_cars_by_month():
    cars = CarInfo.objects.filter(month='202406')
    # cars = CarInfo.objects.all()
    print(cars)
    return cars

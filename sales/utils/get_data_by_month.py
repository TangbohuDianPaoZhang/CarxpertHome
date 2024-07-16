from sales.models import *

def getCarsByMonth():
    # cars = CarInfo.objects.filter(month=month).values()
    cars = CarInfo.objects.all()
    print(cars)
    return cars

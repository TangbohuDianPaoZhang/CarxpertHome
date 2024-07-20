from .get_data_by_month import *


def get_pie_type_data():
    cars = get_cars_by_month()
    car_type_dic = {}
    for i in cars:
        if car_type_dic.get(i.carType, -1) == -1:
            car_type_dic[str(i.carType)] = int(i.sales)
        else:
            car_type_dic[str(i.carType)] += int(i.sales)
    car_type_dic = sorted(zip(car_type_dic.values(), car_type_dic.keys()), reverse=True)
    pie_data = []
    for k, v in car_type_dic:
        pie_data.append({'value': k, 'name': v})
    return pie_data

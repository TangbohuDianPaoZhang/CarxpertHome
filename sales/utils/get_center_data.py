from .get_data_by_month import *


def get_center_data():
    cars = list(get_cars_by_month())
    most_popular_car = cars[0].model
    most_popular_car_sales = cars[0].sales
    # 车型
    car_type_count_list = {}
    for i in cars:
        car_type = str(i.carType)
        if car_type not in car_type_count_list:
            car_type_count_list[car_type] = 1
        else:
            car_type_count_list[car_type] += 1
    car_type_count_list = sorted(car_type_count_list.items(), key=lambda x:x[1], reverse=True)
    max_car_type_count = car_type_count_list[0][1]
    max_car_type = car_type_count_list[0][0]
    # 品牌
    car_brand_count_list = {}
    for i in cars:
        car_brand = str(i.brand)
        if car_brand not in car_brand_count_list:
            car_brand_count_list[car_brand] = 1
        else:
            car_brand_count_list[car_brand] += 1
    max_brand_count = -1
    max_brand = ''
    for k, v in car_brand_count_list.items():
        if v > max_brand_count:
            max_brand_count = v
            max_brand = k

    return most_popular_car, most_popular_car_sales, max_car_type, max_car_type_count, max_brand, max_brand_count
    
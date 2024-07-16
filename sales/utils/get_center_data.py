from .get_data_by_month import *


def get_center_data():
    cars = list(getCarsByMonth())
    most_popular_car = cars[0].model
    most_popular_car_sales = cars[0].sales
    # 车型
    car_type_count_list = {}
    for i in cars:
        if car_type_count_list.get(i.carType, -1) == -1:
            car_type_count_list[str[i.carType]] = 1
        else:
            car_type_count_list[str(i.carType)] += 1
    car_type_count_list = sorted(car_type_count_list.items(), key=lambda x:x[1], reverse=True)
    max_car_type_count = car_type_count_list[0][1]
    max_car_type = car_type_count_list[0][0]
    # 品牌
    car_brand_count_list = {}
    for i in cars:
        if car_brand_count_list.get(i.brand, -1) == -1:
            car_brand_count_list[str[i.brand]] = 1
        else:
            car_brand_count_list[str(i.brand)] += 1
    max_brand_count = -1
    max_brand = ''
    for k, v in car_brand_count_list.items():
        if v > max_brand_count:
            max_brand_count = v
            max_brand = k

    return (most_popular_car, most_popular_car_sales, max_car_type,
            max_car_type_count, max_brand, max_brand_count)
    
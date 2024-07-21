from .get_data_by_month import *


def get_center_data(cars: list):
    # 车型
    car_type_list = {}
    car_type_count_list = {}
    for i in cars:
        if car_type_list.get(i.carType, -1) == -1:
            car_type_list[str(i.carType)] = int(i.sales)
            car_type_count_list[str(i.carType)] = 1
        else:
            car_type_list[str(i.carType)] += int(i.sales)
            car_type_count_list[str(i.carType)] += 1
    car_type_sales_list = sorted(car_type_list.items(), key=lambda x: x[1], reverse=True)
    max_car_type_count = car_type_sales_list[0][1]
    max_car_type = car_type_sales_list[0][0]

    # 当月销量最高车型
    most_popular_car = cars[0].model
    most_popular_car_sales = cars[0].sales
    for i in range(len(cars)):
        if cars[i].sales > most_popular_car_sales:
            most_popular_car = cars[i].model
            most_popular_car_sales = cars[i].sales

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
    max_brand_sales = 0
    for i in cars:
        brand = str(i.brand)
        if brand == max_brand:
            max_brand_sales += i.sales
    return most_popular_car, most_popular_car_sales, max_car_type, max_car_type_count, max_brand, max_brand_sales


def get_roll_list(cars: list):
    car_brand_sales_list = {}
    for i in cars:
        car_brand = str(i.brand)
        if car_brand not in car_brand_sales_list:
            car_brand_sales_list[car_brand] = i.sales
        else:
            car_brand_sales_list[car_brand] += i.sales
    car_brand_sales_list = sorted(car_brand_sales_list.items(), key=lambda x: x[1], reverse=True)[:10]
    roll_list = []
    for k, v in car_brand_sales_list:
        roll_list.append({
            'name': k,
            'value': v
        })
    return roll_list


def get_energe_type_rate(cars: list):
    energy_type_count_list = {}
    for i in cars:
        energy_type = str(i.energyType)
        if energy_type not in energy_type_count_list:
            energy_type_count_list[energy_type] = 1
        else:
            energy_type_count_list[energy_type] += 1
    car_count = len(cars)
    oil_rate = round(energy_type_count_list['汽油'] / car_count * 100, 1)
    electric_rate = round(energy_type_count_list['纯电动'] / car_count * 100, 1)
    hybrid_rate = round((car_count - energy_type_count_list['汽油'] - energy_type_count_list['纯电动']) / car_count * 100, 1)

    return oil_rate, electric_rate, hybrid_rate

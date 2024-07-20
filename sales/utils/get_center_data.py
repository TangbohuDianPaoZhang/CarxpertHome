from .get_data_by_month import *


def get_center_data(cars: list):
    # 车型
    car_type = ['微型车', '紧凑型车', '中型车', '中大型车', '大型车',
                '小型SUV', '紧凑型SUV', '中型SUV', '中大型SUV' ,'大型SUV',
                '紧凑型MPV', '中型MPV', '中大型MPV' ,'大型MPV']
    car_type_list = dict.fromkeys(car_type)
    for i in cars:
        temp = str(i.carType)
        if car_type_list[temp] is None:
            car_type_list[temp] = 1
        else:
            car_type_list[temp] += 1
    car_type_count_list = sorted(car_type_list.items(), key=lambda x: x[1], reverse=True)
    max_car_type_count = car_type_count_list[0][1]
    max_car_type = car_type_count_list[0][0]

    # 当月销量最高车型
    most_popular_car = cars[0].model
    most_popular_car_sales = cars[0].sales
    index = 0
    for i in range(len(car_type) - 1):
        index += car_type_list.get(car_type[i])
        if cars[index].sales > most_popular_car_sales:
            most_popular_car = cars[index].model
            most_popular_car_sales = cars[index].sales

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

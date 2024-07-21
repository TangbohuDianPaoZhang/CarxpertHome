from .get_data_by_month import *

def getRankData():
    cars = list(get_cars_by_month('202406'))
    carData = []
    for car in cars:
        # 获取最低价格和最高价格并连接为字符串
        price = f"{car.minPrice}-{car.maxPrice}"
        carData.append({
            'brand': car.brand,
            'rank': car.rank,
            'carImg': car.carImg,
            'carModel': car.model,
            'price': price,
            'sales': car.sales,
            'energyType': car.energyType,
            'cartype': car.carType
        })
    return carData
    # print(carData[0])
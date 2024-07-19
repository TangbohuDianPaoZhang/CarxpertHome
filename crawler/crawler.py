# import requests
# from bs4 import BeautifulSoup
# import mysql.connector
# import json
# import traceback
# import time
#
# def get_conn():
#     # 建立连接
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="123456",
#         database="cars",
#         auth_plugin='mysql_native_password'
#     )
#     # 创建游标
#     cursor = conn.cursor()
#     return conn, cursor
#
# def close_conn(conn, cursor):
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()
#
# def get_data(url):
#     res = json.loads(requests.get(url).text)
#     return res['data']['list']
#
# def insert_hotsearch(url, t, m):
#     cursor = None
#     conn = None
#     try:
#         conn, cursor = get_conn()
#         print(f"{time.asctime()}开始插入数据")
#         sql = """
#             INSERT INTO cardata_with_energytype(
#                 `series_name`, `image`, `rank`, `count`, `brand_name`,
#                 `type`, `sub_brand_name`, `min_price`, `max_price`, `month`
#             )
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
#         """
#         for i in get_data(url):
#             series_name = i.get('series_name')
#             image = i.get('image')
#             rank = i.get('rank')
#             count = i.get('count')
#             brand = i.get('brand_name')
#             sub_brand_name = i.get('sub_brand_name')
#             min_price = i.get('min_price')
#             max_price = i.get('max_price')
#             cursor.execute(sql, (series_name, image, rank, count, brand, t, sub_brand_name, min_price, max_price, m))
#         conn.commit()
#         print(f"{time.asctime()}数据插入完毕")
#     except:
#         traceback.print_exc()
#     finally:
#         close_conn(conn, cursor)
#
# if __name__ == "__main__":
#     months = ['202305', '202304', '202303', '202302', '202301']
#     data = {
#         '轿车': {
#             'start': 0,
#             'end': 6,
#             'car_type': ['微型车', '小型车', '紧凑型车', '中型车', '中大型车', '大型车']
#         },
#         'SUV': {
#             'start': 10,
#             'end': 15,
#             'car_type': ['小型SUV', '紧凑型SUV', '中型SUV', '中大型SUV', '大型SUV']
#         },
#         'MPV': {
#             'start': 20,
#             'end': 25,
#             'car_type': ['小型MPV', '紧凑型MPV', '中型MPV', '中大型MPV', '大型MPV']
#         }
#     }
#     for month in months:
#         for d in data:
#             item = data.get(d)
#             for index, value in enumerate([i for i in range(item.get('start'), item.get('end'))]):
#                 url = f'https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&energy_type=1&app_name=auto_web_pc&count=100000&month={month}&rank_data_type=11&outter_detail_type={value}&nation=0'
#                 print(month, d, item.get('car_type')[index])
#                 insert_hotsearch(url, item.get('car_type')[index], month)
#
#

import requests
from bs4 import BeautifulSoup
import mysql.connector
import json
import traceback
import time

def get_conn():
    # 建立连接
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="cars",
        auth_plugin='mysql_native_password'
    )
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor

def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def get_data(url):
    response = requests.get(url)
    res = json.loads(response.text)
    return res['data']['list']

def get_energy_type(series_id):
    search_url = f'https://www.dongchedi.com/auto/params-carIds-x-{series_id}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # energy_type_div = soup.find('div', {'data-search-id': 'fuel_form'})
    energy_type_div = soup.select_one("div[data-row-anchor='fuel_form'] > div:nth-of-type(2) > div")
    if energy_type_div:
        return energy_type_div.text.strip()
    return '未知'

def insert_hotsearch(url, t, m):
    cursor = None
    conn = None
    try:
        conn, cursor = get_conn()
        print(f"{time.asctime()}开始插入数据")
        sql = """
            INSERT INTO cardata_with_energytype(
                `series_name`, `image`, `rank`, `count`, `brand_name`,
                `type`, `energy_type`, `sub_brand_name`, `min_price`, `max_price`, `month`
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        for i in get_data(url):
            series_id = i.get('series_id')
            series_name = i.get('series_name')
            image = i.get('image')
            rank = i.get('rank')
            count = i.get('count')
            brand = i.get('brand_name')
            sub_brand_name = i.get('sub_brand_name')
            min_price = i.get('min_price')
            max_price = i.get('max_price')
            energy_type = get_energy_type(series_id)
            cursor.execute(sql, (series_name, image, rank, count, brand, t, energy_type, sub_brand_name, min_price, max_price, m))
        conn.commit()
        print(f"{time.asctime()}数据插入完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)

if __name__ == "__main__":
    months = ['202406', '202405', '202404', '202403', '202402', '2024901']
    data = {
        '轿车': {
            'start': 0,
            'end': 6,
            'car_type': ['微型车', '小型车', '紧凑型车', '中型车', '中大型车', '大型车']
        },
        'SUV': {
            'start': 10,
            'end': 15,
            'car_type': ['小型SUV', '紧凑型SUV', '中型SUV', '中大型SUV', '大型SUV']
        },
        'MPV': {
            'start': 20,
            'end': 25,
            'car_type': ['小型MPV', '紧凑型MPV', '中型MPV', '中大型MPV', '大型MPV']
        }
    }
    for month in months:
        for d in data:
            item = data.get(d)
            for index, value in enumerate([i for i in range(item.get('start'), item.get('end'))]):
                # self.spiderUrl = 'https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E5%8C%97%E4%BA%AC&count=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0'
                url = f'https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&count=100000&month={month}&rank_data_type=11&outter_detail_type={value}&nation=0'
                print(month, d, item.get('car_type')[index])
                insert_hotsearch(url, item.get('car_type')[index], month)






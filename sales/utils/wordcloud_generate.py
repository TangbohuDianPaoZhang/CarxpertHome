import json
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from .get_data_by_month import *


def generate_img():
    cars = list(get_cars_by_month())
    car_brand = ''
    for i in cars:
        car_brand += i.brand + ' '
    words = jieba.lcut(car_brand)
    words = ' '.join(words)
    mask = np.array(Image.open('i8.png'))
    wc = WordCloud(
        font_path='C:\\Windows\\Fonts\\msyh.ttc',
        background_color='rgba(255, 255, 255, 0)',
        max_words=100,
        mask=mask,
        width=400,
        height=300,
        mode='RGBA'
    )
    wc.generate(words)
    wc.to_file('wordcloud-img/car_wordcloud.png')
    return json.dumps({'status': 'success'})

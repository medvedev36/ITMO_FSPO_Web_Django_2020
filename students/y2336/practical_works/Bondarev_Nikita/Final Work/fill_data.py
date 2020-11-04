from random import randint, uniform, choice

from django.core.files import File


import io

from PIL import Image

import string

import json
from bs4 import BeautifulSoup
from urllib.parse import quote
from fake_headers import Headers
import requests

from cars.models import *


TAG = '[DEBUG]: --->'


def fill_car_class():
    classes = ['A', 'B', 'C', 'D', 'E', 'F', 'J', 'M', 'S']
    names = ['Mini cars',  # A
             'Small cars',  # B
             'Medium cars',  # C
             'Larger cars',  # D
             'Executive cars',  # E
             'Luxury cars',  # F
             'Sport utility',  # J
             'Multi purpose cars',  # M
             'Sport coupe'  # S
             ]
    min_prices = [
        200000,  # A
        400000,  # B
        600000,  # C
        800000,  # D
        2000000,  # E
        4000000,  # F
        500000,  # J
        700000,  # M
        6000000,  # S
    ]
    descriptions = [
        'Особо малый класс (“mini cars”) или компакт-класс. Автомобили класса А также называют “микролитражками“. Это очень маленькие машинки длиной до 3,6 м, чаще считаются дамскими. Идеально подойдут для неспешного передвижения в условиях города. Очень экономичны – бензин они скорее “нюхают”, в среднем расход 4-6 литров на сотню.',
        'Малый класс (“small cars”) . Пожалуй, самый многочисленный и популярный класс автомобилей. Данные авто отличаются компактными габаритами (до 4,2 м длиной), небольшой ценой и экономичностью. Идеальны для передвижения в черте города. Практически все машины российского автопрома принадлежат именно этой категории.',
        'Малый средний класс (“medium cars”) или гольф-класс. Среднеразмерные автомобили класса С (по европейской системе классификации) выпускаются длиной до 4,5 метров. Хорошо подходят в качестве основного средства передвижения для семьи с детьми. Имеют довольно большой багажник и просторный салон при небольших габаритах.',
        'Второй средний класс (“larger cars”) или семейный. Сюда относятся полноразмерные транспортные средства длиной корпуса до 4,6 м. Д-класс отлично подойдет для семейных людей, отличается большим комфортным салонным пространством и емким багажным отделением. В этом классе представлены и семейные авто, и дорогие элитные, “нафаршированные” полезными опциями.',
        'Бизнес-класс (“executive cars”). Машины этой категории выпускают не длиннее 5 м. Такие автомобили выбирают состоятельные люди, чтобы подтвердить свой социальный статус. Для обычных семейных поездок слишком много “наворотов”, больше подходят для рабочих поездок.',
        'Бизнес-класс (“executive cars”). Машины этой категории выпускают не длиннее 5 м. Такие автомобили выбирают состоятельные люди, чтобы подтвердить свой социальный статус. Для обычных семейных поездок слишком много “наворотов”, больше подходят для рабочих поездок.',
        'Кроссоверы, паркетники и внедорожники (SUV – “sport utility”). Очень просторные авто увеличенной проходимости. Обладают повышенным дорожным просветом и вместительным багажником. Также имеют полный привод. Внедорожники имеют в основе рамную конструкцию, а паркетники и кроссоверы только несущий кузов.',
        'Отдельная категория минивэнов, компактвэнов и микровэнов (“multi purpose cars”). Очень вместительные автомобили, идеально подходят для большой семьи. Отличаются увеличенной высотой – от 1,5 метров, и большим количеством посадочных мест – до 9 штук.',
        'Спорткары и суперкары (“sport coupe”). Такие авто выбирают молодые охотники за адреналином. Благодаря отличной аэродинамике и мощному двигателю автомобили этого класса способны развивать высокую скорость. Обладают отличным сцеплением с дорогой и легко управляются.',
    ]
    for name, min_car_price, description in zip(names, min_prices, descriptions):
        CarClass.objects.create(name=name, min_car_price=min_car_price, description=description,
                                rent_price=min_car_price // 100)


def fill_pick_up_points():
    city = 'г. Санкт-Петербург'
    street_prefix = 'ул. '
    addresses = ['Пушкина',
                 'Лермонтова',
                 'Красная',
                 'Малая заборная',
                 'Роговая',
                 'Подзаборная',
                 'Малиновая',
                 'Генерала Плюшкина',
                 'Колотушкина',
                 'Кустовая']
    phone_form = '+7({}){}-{}-{}'
    min_lat, min_lon = 59.854265, 30.000063
    max_lat, max_lon = 60.036394, 30.521640
    for address in addresses:
        address = city + ', ' + street_prefix + address + ', д. ' + str(randint(1, 50))
        phone = phone_form.format(randint(100, 999),
                                  randint(100, 999),
                                  randint(10, 99),
                                  randint(10, 99))
        lat = uniform(min_lat, max_lat)
        lon = uniform(min_lon, max_lon)
        PickUpPoint.objects.create(address=address, phone_number=phone, latitude=lat, longitude=lon)


def get_brand_models(brand):
    url = 'https://auto.vercity.ru/catalog/auto/{}/'
    resp = requests.get(url.format(brand), verify=False)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'lxml')
        all_models = []
        try:
            car_tag_list = soup.find(class_='page_model-ranges').find_all('li')
            for tag in car_tag_list:
                all_models.append(tag.find('a').get_text(strip=True))
        except AttributeError as exc:
            print(TAG, f'Can\'t find models for brand "{brand}", got exception: {exc}')
        return all_models
    print(TAG, f'Can\'t extract models for brand "{brand}"')
    return []


def fill_cars():
    brands = ['bmw', 'audi', 'citroen', 'ford', 'mini', 'peugeot', 'opel']
    colors = ['белый',
              'красный',
              'черный',
              'серый',
              'сиреневый',
              'малиновый',
              'лазурный',
              'розовый',
              'зеленый',
              'фиолетовый',
              'оранжевый',
              'голубой']
    number_form = '{}{}{}'
    i = 0
    for brand in brands:
        all_models = get_brand_models(brand)[::12]
        for model in all_models:
            i += 1
            img_filename = 'yandex/' + f'{i}.jpg'

            plate = number_form.format(choice(string.ascii_uppercase),
                                       randint(100, 999),
                                       choice(string.ascii_uppercase) + choice(string.ascii_uppercase))
            rindex = randint(0, len(CarClass.objects.all()) - 1)
            car_class = CarClass.objects.all()[rindex]

            car = Car(model=model,
                      brand=brand.capitalize(),
                      color=choice(colors),
                      number_plate=plate,
                      sits_number=5,
                      car_class=car_class,
                      car_price=car_class.min_car_price + randint(0, 70) * 1000)
            car.car_image.save(f'{i}.jpg', File(open(img_filename, 'rb')))
            car.save()
            # print(TAG, f'{img_filename} uploaded: SUCCESSFULLY')
        # print(all_models)
        # print('hello')

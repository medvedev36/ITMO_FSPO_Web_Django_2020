from os import listdir
from os.path import isfile, join
from random import randint
from PIL import Image

from tickets.models import *


def fill_bus_type():
    names = ['Пригородный одноэтажный', 'Пригородный полутораэтажный', 'Междугородный', 'Туристический']
    people_cap = [60, 70, 80, 75]
    engine_cap = [randint(100, 150) for _ in people_cap]
    for name, people, engine in zip(names, people_cap, engine_cap):
        BusType.objects.create(name=name, people_capacity=people, engine_capacity=engine)

def fill_station():
    names = [
        'г. Москва',
        'г. Санкт-Петербург',
        'г. Новосибирск',
        'г. Екатеринбург',
        'г. Казань',
        'г. Нижний',
        'г. Челябинск',
        'г. Самара',
        'г. Омск',
        'г. Ростов-на-Дону',
        'г. Уфа',
        'г. Красноярск',
        'г. Воронеж'
    ]
    phone = '+7({}){}-{}-{}'
    streets = [
        'ул. Центральная',
        'ул. Молодежная',
        'ул. Школьная',
        'ул. Лесная',
        'ул. Советская',
        'ул. Новая',
        'ул. Садовая',
        'ул. Набережная',
        'ул. Заречная',
        'ул. Зеленая',
        'ул. Мира',
        'ул. Полевая',
        'ул. Луговая',
    ]
    for city, street in zip(names, streets):
        nphone = phone.format(randint(100, 999), randint(100, 999), randint(10, 99), randint(10, 99))
        Station.objects.create(
            name=city, 
            phone=nphone, 
            address='{}, {}, д. {}'.format(city, street, randint(1, 99))
        )

def fill_drivers():
    mypath = './media/pic_drivers'
    names = ['Иван', 'Василий', 'Татьяна', 'Маруся', 'Денис', 'Тори']
    surnames = ['Иванов', 'Петров', 'Денисова', 'Шушарская', 'Михин', 'Разумихина']
    phone = '+7({}){}-{}-{}'
    images = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
    del images[0]
    images.sort()
    for image, name, last_name in zip(images, names, surnames):
        nphone = phone.format(randint(100, 999), randint(100, 999), randint(10, 99), randint(10, 99))
        Driver.objects.create(
            first_name=name,
            last_name=last_name,
            passport_number=randint(1000000000, 9999999999),
            phone=nphone,
            bio='Водитель'
        )

def fill_bus():
    number = '{}{}{}{}{}{}{}'
    date = '200{}-{}-{}'
    for i, type_ in enumerate(BusType.objects.all()):
        for _ in range(2):
            n_number = number.format(
                randint(10, 99),
                chr(randint(65, 90)),
                chr(randint(65, 90)),
                randint(10, 99),
                chr(randint(65, 90)),
                chr(randint(65, 90)),
                randint(10, 99),
            )
            n_date = date.format(i + 1, i + 10, i * 3 + 5)
            Bus.objects.create(
                number=n_number, 
                bus_type=type_, 
                usage_start_date=n_date
            )

def fill_rides():
    drivers = Driver.objects.all()
    buses = Bus.objects.all()
    stations = Station.objects.all()
    date = '2020-{}-{}'
    for i in range(len(stations)):
        for j in range(len(stations)):
            if i != j:
                ndate = date.format(randint(1, 12), randint(1, 28)) + ' {}:00'
                dep_date = ndate.format(randint(1, 12))
                arr_date = ndate.format(randint(13, 23))
                Ride.objects.create(
                    driver=Driver.objects.get(pk=randint(1, 6)),
                    bus=Bus.objects.get(pk=randint(1, 8)),
                    departure_datetime=dep_date,
                    arrival_datetime=arr_date,
                    where_from=Station.objects.get(pk=i + 1),
                    where=Station.objects.get(pk=j + 1),
                    price=randint(5, 40) * 100,
                )

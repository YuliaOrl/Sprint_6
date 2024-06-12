import random as r
import datetime as d

street = ['Новая 1', 'Прямой проезд 2', 'Проспект дружбы 2']

metro = ['Бульвар Рокоссовского', 'Речной вокзал', 'Пятницкое шоссе', 'Кунцевская', 'Медведково', 'Планерная',
         'Раменки', 'Алтуфьево', 'Петровско-Разумовская', 'Каширская', 'Битцевский парк', 'Окружная']

period = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']

color = ['чёрный жемчуг', 'серая безысходность']

def tomorrow():
    today = d.date.today()
    tomorrow = today + d.timedelta(days=1)
    return tomorrow.strftime('%d.%m.%y')


class OrderData:
    name = 'Ольга'
    surname = 'Петрова'
    address = r.choice(street)
    metro = r.choice(metro)
    phone = r.randint(80000000000, 89999999999)
    day = tomorrow()
    period = r.choice(period)
    color = r.choice(color)
    comment = 'Очень жду'

import requests, sys, json
from datetime import datetime

class OpenWeatherMap():
    """simple class for openweathermap.org"""
    def __init__(self, key = 'you_key_from_openweathermap.org', city = 'Saint Petersburg', path = ''):
        self.key = key
        self.path = path
        self.city = city
    
    @staticmethod
    def get_emoji(dw):
        emoji = {
                "Clear": "Ясно \U00002600",
                "Clouds": "Облачно \U00002601",
                "Rain": "Дождь \U00002614",
                "Drizzle": "Дождь \U00002614",
                "Thunderstorm": "Гроза \U000026A1",
                "Snow": "Снег \U0001F328",
                "Mist": "Туман \U0001F32B"
        }
        return emoji[dw] if dw in emoji else 'Посмотри в окно, не пойму что там за погода!'
    
    def get_print(self, r):            
        if r is False:
            return 'Проверте название города'
        # the text fields for weather
        description_w = r["weather"][0]["main"]
        wd = self.get_emoji(description_w)
        city_w = r['name']
        temp_w = r['main']['temp']
        humidity_w = r["main"]["humidity"]
        pressure_w = r['main']['pressure']
        wind_w = r['wind']['speed']

        sunrise_time = datetime.fromtimestamp(r['sys']['sunrise'])
        sunset_time = datetime.fromtimestamp(r['sys']['sunset'])
        length_day = sunset_time - sunrise_time

        return (f"*** {datetime.now().strftime('%d.%m.%Y %H:%M')} ***\n"
              f"Погода в городе: {city_w}\nТемпература: {temp_w} C° {wd}\n"
              f"Влажность: {humidity_w} %\nДавление: {pressure_w} мм.рт.ст\nВетер: {wind_w} м/с\n"
              f"Восход солнца: {sunrise_time.strftime('%d.%m.%Y %H:%M')}\nЗакат солнца: {sunset_time.strftime('%d.%m.%Y %H:%M')}\nПродолжительность дня: {length_day}\n"
              f"Хорошего дня!"
        )

    def get_open_weather(self, city = None, key = None):
        city = self.city if city is None else city
        key = self.key if key is None else key
        # return json from openweathermap.org
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
            r = requests.get(url, timeout = 10).json()
            return r if 'cod' in r and r['cod'] == 200 else False
        except Exception as ex:
            # print(ex)
            return False

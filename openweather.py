from datetime import datetime
from key import *
from openweathermap import OpenWeatherMap

""" http://bulk.openweathermap.org/sample/ """

def p(text, *args):
    print(text, *args, sep=' / ', end='\n')

def main():
    start = datetime.now()
    # ---- 
    city = input('(Например Москва) Введите город: ')    
    wm = OpenWeatherMap(key = key, city = city)
    r = wm.get_open_weather()
    p(wm.get_print(r))
    # ----
    end = datetime.now()
    print(str(end-start))

if __name__ == '__main__':
    main()
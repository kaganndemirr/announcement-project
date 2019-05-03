from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.http import JsonResponse

from time import strftime, localtime
import requests

@method_decorator(cache_page(60 * 10), name='dispatch') # 10 minutes
class AjaxWeather(View):
    def get(self, request):
        payload = {
            'q': settings.WEATHER['CITY'],
            'lang': 'tr',
            'APPID': settings.WEATHER['APIKEY'],
        }
        response = requests.get(settings.WEATHER['URL'], params=payload)
        wdata = response.json()

        if wdata['cod'] != 200:
            logger.error(wdata)
            return "{'error': 'Internal Server Error!'}"

        icon = 'http://openweathermap.org/img/w/%s.png' % wdata['weather'][0]['icon']
        text = wdata['weather'][0]['description']
        temperature = '%d °C' % (wdata['main']['temp'] - 273.15)
        humidity = '%%%d' % wdata['main']['humidity']
        wind = '%.1f m/s' % wdata['wind']['speed']
        sunrise = strftime("%H:%M:%S", localtime(wdata['sys']['sunrise']))
        sunset = strftime("%H:%M:%S", localtime(wdata['sys']['sunset']))

        data = {
            'icon': icon, # 04d -> http://openweathermap.org/img/w/04d.png
            'text': text, # parçalı bulutlu
            'temperature': temperature, # 287.09 -> 14 °C
            'humidity': humidity, # 87 -> %87
            'wind': wind, # 3.6 -> 3.6 m/s
            'sunrise': sunrise, # 1556849832 -> 05:17:12
            'sunset': sunset, # 1556900324 -> 19:18:44
        }

        return JsonResponse(data)

from django.shortcuts import render
from .utils import unit_conversion
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import json
import urllib.request
import logging

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        post = json.loads(request.body.decode('utf-8'))
        city = post.get('city')
        temp_unit = post.get('temp_unit', "C")
        wind_unit = post.get('wind_unit', "kmh")
        logging.basicConfig(level=logging.INFO)
        logging.info(request.POST)
        logging.info(city)
        logging.info(temp_unit)
        logging.info(wind_unit)
        logging.info(request.body)

        #I can probably do this with the requests moduleS
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+str(city)+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        #logging.info(res)
        json_data = json.loads(res)
        
        data = {
            "country_code": str(json_data['sys']['country']),
            "main" : json_data["weather"][0]["description"],
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": unit_conversion(json_data['main']['temp'], temp_unit), #TRY TO MAKE AN OPTION TO CHANGE THE UNIT
            "wind" : unit_conversion(json_data['wind']['speed'], wind_unit),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        } 
        logging.info(data)

    else:
        city = ''
        data = {}
    return  JsonResponse(data) #render(request, 'index.html', {'city': city, 'data': data})
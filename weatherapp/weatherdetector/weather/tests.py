from django.test import TestCase
from utils import unit_conversion
import urllib.request
import json
# Create your tests here.

res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+str("canterbury")+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        
json_data = json.loads(res)
print(unit_conversion(json_data['main']['temp'], "F"))
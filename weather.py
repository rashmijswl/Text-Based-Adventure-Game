import urllib.request
import json

api = "31f11bc73507f9b64497055e3a37b063"
celsius_temps = []
cities = ["vaughn","kitchener","waterloo","guelph","toronto","missisauga","sudbury","maple","london","cambridge","tottenham","sarnia","thunder+bay","scarborough","ottawa","hamilton","markham","north+york","east+york","whitby"]

def city_temp():
  with open("current_player.json", "r") as game:
    details = json.load(game)
  api = "31f11bc73507f9b64497055e3a37b063"
  city = details['city']
  url = f"https://api.openweathermap.org/data/2.5/weather?q={cities[city]}&appid={api}"
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
    
    #print(result['main']['temp'])
  celsius_temp = result["main"]["temp"] - 273.15
  celsius_temps.append(celsius_temp)
  return celsius_temps
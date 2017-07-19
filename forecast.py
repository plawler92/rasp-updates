import requests
from geopy.geocoders import Nominatim

class Forecast():
    forecast_request = "https://api.darksky.net/forecast/{0}/{1:.8f},{2:.8f}"
    geolocator = Nominatim()

    def __init__(self, key, address):
        self.dark_sky_key = key
        self.forecast_json = self.__set_forecast_usingaddress(address)
    
    #leaving both these in case want to expand to handle taking in lat/long in constructor
    def __set_forecast_usingaddress(self, address):
        loc = self.geolocator.geocode(address)
        return self.__set_forecast(loc.latitude, loc.longitude)
    
    #todo: what if request unsuccesful
    def __set_forecast(self, lat, lon):
        response = requests.get(self.forecast_request.format(self.dark_sky_key, lat, lon))
        return response.json()
        
    def get_today_precip_chance(self):
        return self.forecast_json["daily"]["data"][0]["precipProbability"]
        
    #This should really use hourly data and maybe not the mean.
    def get_average_apparent_temp(self):
        min_apparent = self.forecast_json["daily"]["data"][0]["apparentTemperatureMin"]
        max_apparent = self.forecast_json["daily"]["data"][0]["apparentTemperatureMax"]
        avg = (min_apparent + max_apparent) / 2
        return avg
        
    def get_uvindex(self):
        return self.forecast_json["daily"]["data"][0]["uvIndex"]
        
    def get_precip_type(self):
        return self.forecast_json["daily"]["data"][0]["precipType"]
import requests
from geopy.geocoders import Nominatim

DARK_SKY_KEY = "8df4cedf9c2ec63bb059fbfd5039c9cd"
forecast_request = "https://api.darksky.net/forecast/{0}/{1:.8f},{2:.8f}"
geolocator = Nominatim()
    
    #currently, minutely, hourly, daily, alerts, flags
def get_forecast_address(address):
    loc = geolocator.geocode(address)
    return get_forecast(loc.latitude, loc.longitude)
    
def get_forecast(lat, lon):
    response = requests.get(forecast_request.format(DARK_SKY_KEY, lat, lon))
    return response.json()
    
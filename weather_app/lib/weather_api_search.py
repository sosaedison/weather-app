from flask import current_app
import requests


class SearchWeatherAPI:
    def __init__(self):
        self.API_KEY = current_app.config["WEATHER_API_KEY"]
        self.base_url = "api.openweathermap.org/data/2.5/find?"

    def search_by_city(self, city_name):
        requests.get(f"{self.base_url}q={city_name}")

    def _search_by_city_string(self, city_name):
        return self.base_url

    def search_by_zip_code(self):
        pass

    def search_by_coord(self):
        pass

    def search_by_cityID(self):
        pass

    def search_by_radius(self):
        pass
import requests


class SearchWeatherAPI:
    def __init__(self):
        self.API_ARG = "&appid=376944731769fe3b16fb7cb9d65da026"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def search_by_city(self, city_name):
        return requests.get(self._search_by_city_string(city_name))

    def _search_by_city_string(self, city_name):
        return f"{self.base_url}q={city_name}{self.API_ARG}"

    def search_by_zip_code(self, zip_code):
        return requests.get(self._search_by_zip_code_string(zip_code))

    def _search_by_zip_code_string(self, zip_code):
        return f"{self.base_url}zip={zip_code}{self.API_ARG}"

    def search_by_coord(self, lat, lon):
        return requests.get(self._search_by_coord_string(lat, lon))

    def _search_by_coord_string(self, lat, lon):
        return f"{self.base_url}lat={lat}&lon={lon}{self.API_ARG}"

    def search_by_cityID(self, cityID):
        return requests.get(self._search_by_cityID_string(cityID))

    def _search_by_cityID_string(self, cityID):
        return f"{self.base_url}id={cityID}{self.API_ARG}"

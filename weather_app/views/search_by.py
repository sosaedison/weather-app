import json
from flask import Blueprint, json, request, make_response
from weather_app.lib.weather_api_search import SearchWeatherAPI

mod = Blueprint("search_by", __name__)

weather = SearchWeatherAPI()


@mod.route("/city", methods=["POST"])
def search_by_city():

    city_name = request.form.get("city_name")

    return make_response(json.loads(weather.search_by_city(city_name).text), 200)


@mod.route("/zip_code", methods=["POST"])
def search_by_zip_code():

    zip_code = request.form.get("zip_code")
    return json.loads(weather.search_by_zip_code(zip_code.strip()).text)


@mod.route("/lat_lon", methods=["POST"])
def search_by_coord():

    lat = request.form.get("lat")
    lon = request.form.get("lon")
    return json.loads(weather.search_by_coord(lat, lon).text)


@mod.route("/id", methods=["POST"])
def search_by_id():

    city_id = request.form.get("id")
    return json.loads(weather.search_by_cityID(city_id).text)
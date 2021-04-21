import json
from flask import Blueprint, json, request
from weather_app.lib.weather_api_search import SearchWeatherAPI

mod = Blueprint("search_by", __name__)

weather = SearchWeatherAPI()


@mod.route("/city", methods=["POST"])
def search_by_city():

    city_name = request.args.get("city_name")
    return json.loads(weather.search_by_city(city_name).text)


@mod.route("/zip_code", methods=["POST"])
def search_by_zip_code():

    zip_code = request.args.get("zip_code")
    return json.loads(weather.search_by_zip_code(zip_code).text)


@mod.route("/lat_lon", methods=["POST"])
def search_by_coord():

    lat = request.args.get("lat")
    lon = request.args.get("lon")
    return json.loads(weather.search_by_coord(lat, lon).text)


@mod.route("/id", methods=["POST"])
def search_by_id():

    city_id = request.args.get("id")
    return json.loads(weather.search_by_cityID(city_id).text)
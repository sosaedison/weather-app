from flask import Blueprint, current_app, jsonify, request
from weather_app.lib.weather_api_search import SearchWeatherAPI as weather

mod = Blueprint("search_by", __name__)


@mod.route("/city", methods=["GET", "POST"])
def search_by_city():
    API_KEY = current_app.config["WEATHER_API_KEY"]
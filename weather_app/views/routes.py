from flask import Blueprint, render_template, jsonify, request

mod = Blueprint("routes", __name__)


@mod.route("/", methods=["GET"])
def index():
    return render_template("home.html")
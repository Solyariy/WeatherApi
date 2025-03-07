from flask import Flask, jsonify, request

from src.error_handler import InvalidUsage
from src.models import WeatherGetRequest, WeatherResponse
from src.consts import API_TOKEN
from src.weather_manager import WeatherApi
import requests
import json

app = Flask(__name__)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.get("/api/v1/answer")
def get_weather():
    json_data = request.get_json()

    token = json_data.get("token")

    if not token:
        raise InvalidUsage("token is required", status_code=400)
    if token != API_TOKEN:
        raise InvalidUsage("wrong API token", status_code=403)
    weather_obj = WeatherGetRequest(json_data)
    weather_api = WeatherApi(weather_obj)
    print(weather_api.__str__())
    response = requests.get(weather_api.__str__())
    if response.status_code == requests.codes.ok:
        res = json.loads(response.text)
    else:
        raise InvalidUsage(response.text, status_code=response.status_code)
    weather_response = WeatherResponse(json_data, res)

    return weather_response.__dict__()


app.run()

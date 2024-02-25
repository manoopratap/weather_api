from flask import request, make_response,jsonify
from weather_api_service import app, db, secret_key, getResponseHeaders
from weather_api_service.models.HttpResponse import HttpResponse
import json
from weather_api_service.utils import read_json_file
import jwt
import chardet
from pathlib import Path
import requests
from weather_api_service.models.Forcast import Forcast

@app.route('/forecast', methods=['GET'])
def forecast():
    try:
        city = request.args.get('q')
        api = request.args.get('no')
        days = request.args.get('days')
        forecastData = requests.get("http://api.weatherapi.com/v1/forecast.json?key=8e6bd750bd7d414c979171732242302&q={}&aqi={}&days={}".format(city, api, days))
        forecastDataValue = forecastData.json()
        token = request.headers.get('Authorization')
        actual_token = token.split(' ')[1]
        userData = jwt.decode(jwt=actual_token,key=secret_key,algorithms='HS256')
        userProcessData = Forcast(username=userData["user_name"], full_name=userData["first_name"], country=forecastDataValue["location"]["country"], citi_name=forecastDataValue["location"]["name"],region=forecastDataValue["location"]["region"])
        db.session.add(userProcessData)
        db.session.commit()
        response = HttpResponse(message="country list feteched", status=200, data=forecastDataValue)
    except Exception as e:
        db.session.rollback()
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())

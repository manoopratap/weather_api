from flask import request, make_response,jsonify
from weather_api_service import app, db, secret_key, getResponseHeaders
from weather_api_service.models.HttpResponse import HttpResponse
import json
from weather_api_service.utils import read_json_file
import jwt
import chardet
from pathlib import Path


@app.route('/countries', methods=['GET'])
def country():
    try:
        current_folder = Path(__file__).resolve().parent
        data_folder = current_folder.parent / 'data'
        data_file_path = data_folder / 'country_data.json'
        json_data = read_json_file(data_file_path)
        response = HttpResponse(message="country list feteched", status=200, data=json_data)
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())

@app.route('/cities', methods=['GET'])
def list_cities():
    try:
        country_param = request.args.get('country', None)
        geo_name_id_param = request.args.get('geonameid', None)
        citi_name_param = request.args.get('name', None)
        sub_country_param = request.args.get('subcountry', None)
        print(country_param)
        current_folder = Path(__file__).resolve().parent
        data_folder = current_folder.parent / 'data'
        data_file_path = data_folder / 'country_data.json'
        json_data = read_json_file(data_file_path)
        if country_param:
            filtered_data = [entry for entry in json_data if entry["country"] == country_param]
            response = HttpResponse(message="citi list feteched based on country", status=200, data=filtered_data)
        elif geo_name_id_param:
            filtered_data = [entry for entry in json_data if entry["geonameid"] == int(geo_name_id_param)]
            response = HttpResponse(message="citi list feteched based on geonameid", status=200, data=filtered_data)
        elif citi_name_param:
            filtered_data = [entry for entry in json_data if entry["name"] == citi_name_param]
            response = HttpResponse(message="citi list feteched based on name", status=200, data=filtered_data)
        elif sub_country_param:
            filtered_data = [entry for entry in json_data if entry["subcountry"] == sub_country_param]       
            response = HttpResponse(message="citi list  feteched based on subcountry", status=200, data=filtered_data)
        else:
            response = HttpResponse(message="one filter parameter expected", status=404, data=[])
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())
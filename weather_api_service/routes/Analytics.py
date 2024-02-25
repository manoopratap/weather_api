from flask import request, make_response,jsonify
from weather_api_service import app, db, secret_key, getResponseHeaders ,encrypt, decrypt
from weather_api_service.models.HttpResponse import HttpResponse
import json
from weather_api_service.utils import decrypt
import jwt
import chardet
from pathlib import Path
import requests
from weather_api_service.models.Forcast import Forcast



@app.route('/analytics', methods=['GET'])
def analytics():
    try:
        
        filterByData = request.args.get('filter')
        topData = request.args.get('top')
        
        if filterByData== "country":
            result = db.session.query(Forcast.country).distinct().limit(topData).all()
            countries_list = [country[0] for country in result]
            response = HttpResponse(message="Top country list feteched", status=200, data=countries_list)
        elif filterByData== "city":
            result = db.session.query(Forcast.cities).distinct().limit(topData).all()
            countries_list = [country[0] for country in result]
            response = HttpResponse(message="Top city list feteched", status=200, data=countries_list)
        elif filterByData== "user":
            result = db.session.query(Forcast.username).group_by(Forcast.username).order_by(db.desc('username')).limit(3).all()
            countries_list = [country[0] for country in result]
            response = HttpResponse(message="Top user list feteched", status=200, data=countries_list)
        else:
            response = HttpResponse(message="Please enter valid filter", status=400, data=[])
    except Exception as e:
        exception_str = str(e)
        response = HttpResponse(message='Exception Occured - ' + exception_str, status=500)

    return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())

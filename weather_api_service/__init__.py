from flask import Flask , request ,make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from weather_api_service.config import *
from weather_api_service.utils import *

app = Flask(__name__)
app.config.update(app_config_dict)
CORS(app)
app.app_context().push()

db = SQLAlchemy(app)
db.init_app(app)

from weather_api_service.models.User import User as UserModel

from weather_api_service.routes import User
from weather_api_service.routes import Countries
from weather_api_service.routes import Forecast
from weather_api_service.routes import Analytics
from weather_api_service.services import User as user_service
from weather_api_service import  getResponseHeaders
from weather_api_service.models.HttpResponse import HttpResponse

with app.app_context():
    db.create_all()

print('Adding Users')
try:
    import csv

    file = './weather_api_service/data/username.csv'
    dict_from_csv = {}

    with open(file, mode='r') as infile:
        reader = csv.reader(infile)
        for i, line in enumerate(reader):
            if i is not 0:
                try:
                    row = list(line)
                    enc_pass = encrypt(secret_key=secret_key, plain_text=row[2])
                    user = UserModel(username=row[1], password=enc_pass, full_name=row[3])
                    db.session.add(user)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
except Exception as e:
    pass
print('Users Added')

@app.before_request
def before_request():
    if request.endpoint == "login":
        pass
    elif request.headers.get('Authorization'):
        user_service.validate_user_token(request.headers.get('Authorization'))
    else:
        response = HttpResponse(message="'Bearer Token missing'", status=401)
        return make_response(json.dumps(response.__dict__), response.status, getResponseHeaders())

@app.route('/')
def ping():  # put application's code here
    return 'pong'

if __name__ == "main":
    app = create_app()
    app.run(debug=True)

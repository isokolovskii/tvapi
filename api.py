from flask import Flask
from flask_restful import Api
from models import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Channels, '/api/channels', endpoint='channels')
api.add_resource(Categories, '/api/categories', endpoint='categories')
api.add_resource(Programme, '/api/programme', endpoint='programme')
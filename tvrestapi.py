from flask import Flask
from flask.ext.restful import Api

from config import config
from resources import *

app = Flask(__name__)
api = Api(app)

api.add_resource(ChannelsResources, '/api/channels', endpoint='channels')
api.add_resource(CategoriesResources, '/api/categories', endpoint='categories')
api.add_resource(ProgrammeResources, '/api/programme', endpoint='programme')

if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'])

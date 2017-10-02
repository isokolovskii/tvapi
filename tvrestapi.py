from flask import Flask
from flask.ext.restful import Api

from config import config
from resources import *

app = Flask(__name__)
api = Api(app)

api.add_resource(ChannelsResources, '/api/channels')
api.add_resource(ProgrammeResources, '/api/programme')
api.add_resource(CategoriesResources, '/api/categories')


if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'], debug=True)

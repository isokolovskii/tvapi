from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine

config = {
    'dms': 'mysql',
    'driver': 'pymysql',
    'user': 'tvapi',
    'password': 'ndfgb2017',
    'server': 'localhost',
    'database': 'tvservice',
    'charset': 'utf8'
}

e = create_engine('{dms}+{driver}://{user}:{password}@{server}/{database}?charset={charset}'.format(**config))
app = Flask(__name__)
api = Api(app)


class Channels(Resource):
    @staticmethod
    def get():
        conn = e.connect()
        query = conn.execute("SELECT * FROM channels")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result


class Channel(Resource):
    @staticmethod
    def get(channel_id):
        conn = e.connect()
        query = conn.execute("SELECT * FROM channels WHERE id={}".format(channel_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result


class Categories(Resource):
    @staticmethod
    def get():
        conn = e.connect()
        query = conn.execute("SELECT * FROM categories")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result


api.add_resource(Channel, '/channel/<string:channel_id>')
api.add_resource(Channels, '/channels')
api.add_resource(Categories, '/categories')

if __name__ == '__main__':
    app.run(host='tv.isokol-dev.ru', port=8085)

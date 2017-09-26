from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine

# TODO Fix programme requests

config = {
    'dms': 'mysql',
    'driver': 'pymysql',
    'user': 'tvapi',
    'password': 'ndfgb2017',
    'server': 'localhost',
    'database': 'tvservice',
    'charset': 'utf8',
    'host': 'tv.isokol-dev.ru',
    'port': 8085
}

e = create_engine('{dms}+{driver}://{user}:{password}@{server}/{database}?charset={charset}'.format(**config))
app = Flask(__name__)
api = Api(app)


def parse_query(query):
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return result


class Channels(Resource):
    def __init__(self):
        self.__args = request.args

    def get(self):
        conn = e.connect()
        if 'id' in self.__args.keys():
            query = conn.execute("SELECT * FROM channels WHERE id={id}".format(**self.__args))
        else:
            query = conn.execute("SELECT * FROM channels")
        return parse_query(query)


class Categories(Resource):
    def __init__(self):
        self.__args = request.args

    def get(self):
        conn = e.connect()
        if 'programme-id' in self.__args.keys():
            query = conn.execute("SELECT * FROM categories WHERE id IN (SELECT category_id FROM programme_category "
                                 "WHERE programme_id={programme-id})".format(**self.__args))
        else:
            query = conn.execute("SELECT * FROM categories")
        return parse_query(query)


class Programme(Resource):
    def __init__(self):
        self.__args = request.args

    def get(self):
        conn = e.connect()
        if 'channel-id' in self.__args.keys():
            query = conn.execute("SELECT * FROM programme WHERE channel_id={channel-id}".format(**self.__args))
        elif 'category-id' in self.__args.keys():
            query = conn.execute("SELECT * FROM programme WHERE id IN (SELECT programme_id FROM programme_category "
                                 "WHERE category_id={category-id})".format(**self.__args))
        else:
            query = conn.execute("SELECT * FROM programme")
        return parse_query(query)


api.add_resource(Channels, '/api/channels', endpoint='channels')
api.add_resource(Categories, '/api/categories', endpoint='categories')
api.add_resource(Programme, '/api/programme', endpoint='programme')

if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'])

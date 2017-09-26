from flask import request
from flask_restful import Resource

from database import engine as e
from utils import parse_query


# TODO Add pages to request
# TODO Add results per page property
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

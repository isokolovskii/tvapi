from flask import request
from flask_restful import Resource
from utils import parse_query
from database import engine as e


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

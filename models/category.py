from flask import request
from flask_restful import Resource

from database import engine as e
from utils import parse_query


# TODO Add pages to request
# TODO Add results per page property
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

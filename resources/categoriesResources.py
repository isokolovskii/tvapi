from flask import request
from flask.ext.restful import Resource, fields

from models import Categories
from resources.paginator import Paginator

categories_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'lang': fields.String(10)
}


class CategoriesResources(Resource, Paginator):
    def get(self):
        return self.get_paginated_list(Categories, '/api/categories', start=request.args.get(
            'start', 1), maxResults=request.args.get('maxResults', 20),
                                       table_schema=categories_fields)

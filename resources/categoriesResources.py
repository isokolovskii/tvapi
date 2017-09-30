from flask import request
from flask.ext.restful import Resource, fields, abort
from webargs.flaskparser import use_kwargs, parser

from models import Categories
from resources.paginator import Paginator

categories_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'lang': fields.String(10)
}


@parser.error_handler
def handle_request_parsing_error(err):
    abort(422, errors=err.messages)


class CategoriesResources(Resource, Paginator):
    @use_kwargs(Paginator.args)
    def get(self, start, maxResults):
        parser.parse(self.args, request)
        return self.get_paginated_list(Categories, '/api/categories', start=start,
                                       maxResults=maxResults, table_schema=categories_fields)

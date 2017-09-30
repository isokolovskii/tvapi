from flask import request
from flask.ext.restful import Resource, fields

from models import Programme
from resources.paginator import Paginator

programme_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'title_lang': fields.String(10),
    'start': fields.DateTime('iso8601'),
    'end': fields.DateTime('iso8601'),
    'duration': fields.DateTime('iso8601'),
    'description': fields.String,
    'description_lang': fields.String(10),
    'channel_id': fields.Integer
}


class ProgrammeResources(Resource, Paginator):
    def get(self):
        return self.get_paginated_list(Programme, '/api/programme', start=request.args.get(
            'start', 1), maxResults=request.args.get('maxResults', 20),
                                       table_schema=programme_fields)

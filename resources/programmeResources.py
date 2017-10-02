from flask import request
from flask.ext.restful import Resource, fields, abort
from webargs.flaskparser import use_kwargs, parser

from models import Programme
from resources.paginator import Paginator

programme_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'title_lang': fields.String(10),
    'begin': fields.DateTime('iso8601'),
    'end': fields.DateTime('iso8601'),
    'duration': fields.DateTime('iso8601'),
    'description': fields.String,
    'description_lang': fields.String(10),
    'channel_id': fields.Integer
}


@parser.error_handler
def handle_request_parsing_error(err):
    abort(422, errors=err.messages)


class ProgrammeResources(Resource, Paginator):
    @use_kwargs(Paginator.args)
    def get(self, maxResults, pageToken):
        parser.parse(self.args, request)
        return self.get_paginated_list(Programme, maxResults, programme_fields, pageToken)

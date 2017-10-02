from flask import request
from flask.ext.restful import Resource, fields, abort
from webargs.flaskparser import use_kwargs, parser

from models import Channels
from resources.paginator import Paginator

channels_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'lang': fields.String(10),
    'icon': fields.String(255)
}


@parser.error_handler
def handle_request_parsing_error(err):
    abort(422, errors=err.messages)


class ChannelsResources(Resource, Paginator):
    @use_kwargs(Paginator.args)
    def get(self, maxResults, pageToken):
        parser.parse(self.args, request)
        return self.get_paginated_list(Channels, maxResults, channels_fields, pageToken)

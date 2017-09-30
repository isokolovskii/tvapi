from flask import request
from flask.ext.restful import Resource, fields
from webargs.flaskparser import use_kwargs, parser

from models import Channels
from resources.paginator import Paginator

channels_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'lang': fields.String(10),
    'icon': fields.String(255)
}


class ChannelsResources(Resource, Paginator):
    @use_kwargs(Paginator.args)
    def get(self, start, maxResults):
        parser.parse(self.args, request)
        return self.get_paginated_list(Channels, '/api/channels', start=start,
                                       maxResults=maxResults, table_schema=channels_fields)

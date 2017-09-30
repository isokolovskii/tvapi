from flask import request
from flask.ext.restful import Resource, fields

from models import Channels
from resources.paginator import Paginator

channels_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'lang': fields.String(10),
    'icon': fields.String(255)
}


class ChannelsResources(Resource, Paginator):
    def get(self):
        return self.get_paginated_list(Channels, '/api/channels', start=request.args.get(
            'start', 1), maxResults=request.args.get('maxResults', 20),
                                       table_schema=channels_fields)

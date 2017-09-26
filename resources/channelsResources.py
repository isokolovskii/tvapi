from flask.ext.restful import reqparse, abort, Resource, fields, marshal_with

from database import session
from models import Channels

channels_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'lang': fields.String(10),
    'icon': fields.String(255)
}

parser = reqparse.RequestParser()
parser.add_argument('channels', type=str)


class ChannelsResources(Resource):
    @marshal_with(channels_fields)
    def get(self):
        channels = session.query(Channels).all()
        if not channels:
            abort(404, message="Channels table is empty")
        else:
            return channels

from flask.ext.restful import reqparse, abort, Resource, fields, marshal_with

from database import session
from models import Programme

programme_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'title_lang': fields.String(10),
    'start': fields.DateTime('iso8601'),
    'end': fields.DateTime('iso8601'),
    'duration': fields.DateTime('iso8601'),
    'channel_id': fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('programme', type=str)


class ProgrammeResources(Resource):
    @marshal_with(programme_fields)
    def get(self):
        programme = session.query(Programme).all()
        if not programme:
            abort(404, message="Programme table is empty")
        else:
            return programme

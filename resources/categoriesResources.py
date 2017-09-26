from flask.ext.restful import reqparse, abort, Resource, fields, marshal_with

from database import session
from models import Categories

categories_fields = {
    'id': fields.Integer,
    'title': fields.String(255),
    'lang': fields.String(10)
}

parser = reqparse.RequestParser()
parser.add_argument('categories', type=str)


class CategoriesResources(Resource):
    @marshal_with(categories_fields)
    def get(self):
        categories = session.query(Categories).all()
        if not categories:
            abort(404, message="Categories table is empty")
        else:
            return categories

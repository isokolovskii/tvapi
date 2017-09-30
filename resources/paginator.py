import webargs
from flask_restful import abort, marshal
from marshmallow.validate import Range

from database import session


class Paginator:
    args = {
        'maxResults': webargs.fields.Int(required=False, missing=20,
                                         validate=Range(min=1, max=100)),
        'start': webargs.fields.Int(required=False, missing=1,
                                    validate=Range(min=1))
    }

    @staticmethod
    def get_paginated_list(model, url, start, maxResults, table_schema):
        # check if page exists
        items = marshal(session.query(model).all(), table_schema)
        total = len(items)
        if total < start:
            abort(404)
        # make URLs
        nextPage = ''
        prevPage = ''
        # make previous url
        if start > 1:
            start_copy = max(1, start - maxResults)
            limit_copy = start - 1
            prevPage = url + '?start=%d&maxResults=%d' % (start_copy, limit_copy)
        # make next url
        if start + maxResults < total:
            start_copy = start + maxResults
            nextPage = url + '?start=%d&maxResults=%d' % (start_copy, maxResults)
        # make response
        obj = {
            'maxResults': maxResults,
            'total': total,
            'content': model.__name__,
            'prevPage': prevPage,
            'nextPage:': nextPage,
            'items': items[(start - 1):(start - 1 + maxResults)]
        }
        return obj

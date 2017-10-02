import base64

import webargs
from flask import json
from flask_restful import marshal, abort
from marshmallow.validate import Range
from Crypto.Cipher import AES

from database import session


class Paginator:
    args = {
        'maxResults': webargs.fields.Int(required=False, missing=20,
                                         validate=Range(min=1, max=100)),
        'pageToken': webargs.fields.Str(required=False, missing=None)
    }

    __secret = 'mysixteenbytekey'

    def get_paginated_list(self, model, maxResults, table_schema, pageToken):
        # get request and page info, check if page exists
        start = 0
        maxResults = maxResults
        total = session.query(model.id).count()
        if pageToken is not None:
            token_string = self.decode(pageToken)
            d = json.loads(token_string)
            start = d['start']
            maxResults = d['maxResults']
        if start > total:
            abort(404)

        # generate next and previous page
        prevPage = ''
        nextPage = ''
        if start + maxResults <= total:
            d = {'start': start + maxResults, 'maxResults': maxResults}
            token_string = json.dumps(d)
            nextPage = self.encode(token_string)
        if start - maxResults >= 0:
            d = {'start': start - maxResults, 'maxResults': maxResults}
            token_string = json.dumps(d)
            prevPage = self.encode(token_string)

        # query items from table
        q = session.query(model).limit(maxResults)
        q = q.offset(start)
        q = q.all()
        items = marshal(q, table_schema)

        # make response
        obj = {
            'content': model.__name__,
            'results': maxResults,
            'total': total,
            'prevPage': prevPage,
            'nextPage:': nextPage,
            'items': items
        }
        return obj

    def encode(self, plaintext):
        cipher = AES.new(self.__secret, AES.MODE_ECB)
        encoded = base64.b64encode(cipher.encrypt(plaintext.rjust(32)))
        return str(encoded.decode('utf-8'))

    def decode(self, ciphertext):
        cipher = AES.new(self.__secret, AES.MODE_ECB)
        decoded = cipher.decrypt(base64.b64decode(ciphertext))
        return decoded.strip()

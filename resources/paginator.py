import base64
import binascii
import hashlib

import webargs
from Crypto.Cipher import AES
from flask import json
from flask_restful import marshal, abort
from marshmallow.validate import Range

from database import session
from secretpassphrase import pass_phrase


# token validation function
def check_token(token):
    if token is None or token == "":
        return True
    try:
        decoded = Paginator.cipher.decrypt(base64.b64decode(token))
    except binascii.Error:
        raise webargs.ValidationError("Wrong page token")
    try:
        d = json.loads(decoded)
    except ValueError:
        raise webargs.ValidationError('Wrong page token')
    if type(d) is not type({}):
        raise webargs.ValidationError('Wrong page token')


class Paginator:
    # webargs
    args = {
        'maxResults': webargs.fields.Int(required=False, missing=20,
                                         validate=Range(min=1, max=99)),
        'pageToken': webargs.fields.Str(required=False, missing=None,
                                        validate=check_token)
    }

    # secret key and cipher for encryption
    key = pass_phrase.encode('utf-8')
    secret = hashlib.sha256(key).digest()
    cipher = AES.new(secret, AES.MODE_ECB)

    def get_paginated_list(self, model, maxResults, table_schema, pageToken):
        # get request and page info, check if page exists
        start = 0
        maxResults = maxResults
        total = session.query(model.id).count()
        if pageToken is not None:
            token_string = self.__parse_token(pageToken)
            d = json.loads(token_string)
            start = d['start']
            maxResults = d['maxResults']
        if start > total:
            abort(404)

        # generate next and previous page tokens
        prevPage = ''
        nextPage = ''
        if start + maxResults <= total:
            d = {'start': start + maxResults, 'maxResults': maxResults}
            token_string = json.dumps(d)
            nextPage = self.__generate_token(token_string)
        if start - maxResults >= 0:
            d = {'start': start - maxResults, 'maxResults': maxResults}
            token_string = json.dumps(d)
            prevPage = self.__generate_token(token_string)

        # query items from table
        q = session.query(model).limit(maxResults)
        q = q.offset(start)
        q = q.all()
        items = marshal(q, table_schema)

        # make response
        obj = {
            'content': model.__name__.lower(),
            'results': min(maxResults, len(items)),
            'total': total,
            'prevPage': prevPage,
            'nextPage:': nextPage,
            'items': items
        }
        return obj

    # generate next page token
    def __generate_token(self, token_string):
        encoded = base64.b64encode(self.cipher.encrypt(token_string.rjust(32)))
        return encoded.decode('utf-8')

    # parse token into python object for use
    def __parse_token(self, token):
        decoded = self.cipher.decrypt(base64.b64decode(token))
        return decoded.strip()

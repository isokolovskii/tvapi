import datetime
import decimal
import json


def parse_query(res):
    d = json.dumps([dict(r) for r in res], default=encoder)
    return {"data": json.loads(d)}


def encoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
    elif isinstance(obj, datetime.timedelta):
        return obj.total_seconds()

def parse_query(query):
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return result

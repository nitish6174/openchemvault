import json
from bson import ObjectId


def jsonify_mongo(d):
    if isinstance(d, list):
        d = [jsonify_mongo(x) for x in d]
        return d
    elif isinstance(d, dict):
        for k in d:
            d[k] = jsonify_mongo(d[k])
        return d
    elif isinstance(d, ObjectId):
        return str(d)
    else:
        return d


def show(d):
    print(json.dumps(d, indent=4))

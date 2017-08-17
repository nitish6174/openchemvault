import json
import simplejson
from flask import jsonify
from bson import ObjectId


# Recursively find for MongoId object and convert it to string
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


# Handle NaN -> null conversion and return "application/json" object
def api_jsonify(d):
    return jsonify(json.loads(simplejson.dumps(d, ignore_nan=True)))


# Pretty-print JSON object
def show(d):
    print(json.dumps(d, indent=4))

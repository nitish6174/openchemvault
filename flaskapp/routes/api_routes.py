import os
import json
import simplejson
import urllib.parse

from flask import request, jsonify
from bson import ObjectId

from flaskapp.routes import routes_module
from flaskapp.process.file_handle import make_new_file_name
from flaskapp.process.chem_process import parse_file, XYZ_data
from flaskapp.process.json_util import jsonify_mongo, show
import flaskapp.shared_variables as var

# Directory where uploaded files will be saved temporarily
dir_path = "flaskapp/uploads/"


# Upload a log file and view parsed info from it
@routes_module.route("/api/upload", methods=["POST"])
def upload_file_api():
    f = request.files["file"]
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    new_log_file_name = make_new_file_name()
    f.save(new_log_file_name)
    d = parse_file(new_log_file_name)
    os.remove(new_log_file_name)
    return json.dumps(d, sort_keys=True)


# List molecules in database
@routes_module.route("/api/browse/molecules", methods=["GET", "POST"])
def browse_mols_api():
    try:
        db = var.mongo.db
        mols = db.molecule.find({}).sort("formula")
        mols = jsonify_mongo(list(mols))
        d = {
            "success": 1,
            "results": mols
        }
    except Exception as e:
        d = {
            "success": 0,
            "results": [],
            "message": type(e).__name__ + ":" + str(e)
        }
    return api_jsonify(d)


# List parsed files in database
@routes_module.route("/api/browse/files", methods=["GET", "POST"])
def browse_docs_api():
    try:
        db = var.mongo.db
        docs = db.parsed_file.find({})
        docs = jsonify_mongo(list(docs))
        d = {
            "success": 1,
            "results": docs
        }
    except Exception as e:
        d = {
            "success": 0,
            "results": [],
            "message": type(e).__name__ + ":" + str(e)
        }
    return api_jsonify(d)


# List files for a molecule in database
@routes_module.route("/api/browse/<formula>", methods=["GET", "POST"])
def browse_molecule_api(formula):
    try:
        formula = urllib.parse.unquote(formula)
    except Exception as e:
        d = {
            "success": 0,
            "formula": "",
            "results": [],
            "message": type(e).__name__ + ":" + str(e)
        }
        return api_jsonify(d)
    try:
        db = var.mongo.db
        mol_doc = db.molecule.find_one({"formula": formula})
    except Exception as e:
        d = {
            "success": 0,
            "formula": formula,
            "results": [],
            "message": type(e).__name__ + ":" + str(e)
        }
        return api_jsonify(d)
    docs = []
    try:
        if mol_doc is not None:
            ids = mol_doc["parsed_files"]
            docs = db.parsed_file.find({"_id": {"$in": ids}})
            docs = jsonify_mongo(list(docs))
            d = {
                "success": 1,
                "formula": formula,
                "results": docs
            }
            return api_jsonify(d)
        else:
            d = {
                "success": 1,
                "formula": formula,
                "results": [],
                "message": "No file corresponds to this formula"
            }
            return api_jsonify(d)
    except Exception as e:
        d = {
            "success": 0,
            "formula": formula,
            "results": [],
            "message": type(e).__name__ + ":" + str(e)
        }
        return api_jsonify(d)


# Get data of a particular parsed file
@routes_module.route("/api/file/<doc_id>", methods=["GET", "POST"])
def get_file_api(doc_id):
    try:
        db = var.mongo.db
        doc = db.parsed_file.find_one({"_id": ObjectId(doc_id)})
    except Exception as e:
        d = {
            "success": 0,
            "message": type(e).__name__ + ":" + str(e)
        }
        if type(e).__name__ == 'InvalidId':
            d["message"] = "Invalid Id"
        return api_jsonify(d)
    if doc is not None:
        try:
            xyz_data = XYZ_data(doc["attributes"])
            if xyz_data != "":
                doc["xyz_data"] = xyz_data
            doc = jsonify_mongo(doc)
            d = {
                "success": 1,
                "file": doc
            }
            return api_jsonify(d)
        except Exception as e:
            d = {
                "success": 0,
                "message": type(e).__name__ + ":" + str(e)
            }
            return api_jsonify(d)
    else:
        d = {
            "success": 0,
            "message": "This record does not exist"
        }
        return api_jsonify(d)


# Handle NaN -> null conversion and return "application/json" object
def api_jsonify(d):
    return jsonify(json.loads(simplejson.dumps(d, ignore_nan=True)))

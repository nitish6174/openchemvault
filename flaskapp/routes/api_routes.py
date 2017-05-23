import os
import json

from flask import request, jsonify

from flaskapp.routes import routes_module
from flaskapp.routes.api_process import newLogFileName

from flaskapp.process import process_file
import flaskapp.shared_variables as var

# Directory where uploaded files will be saved temporarily
dir_path = "flaskapp/uploads/"


# Search for molecules in database
@routes_module.route("/api/search", methods=["POST"])
def search_api():
    if request.method == "POST":
        query_type = request.form["query_type"]
        query_text = request.form["query_text"]
        d = {"success": 1, "results": []}
        return jsonify(d)


# Upload a log file and view parsed info from it
@routes_module.route("/api/upload", methods=["POST"])
def upload_file_api():
    if request.method == "POST":
        f = request.files["file"]
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        new_log_file_name = newLogFileName()
        f.save(new_log_file_name)
        d = process_file(new_log_file_name)
        os.remove(new_log_file_name)
        return json.dumps(d, sort_keys=True)

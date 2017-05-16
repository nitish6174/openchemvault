import os
import json
import random
import string

from flask import Blueprint, request, render_template, redirect, jsonify

from process import processFile

# Define blueprint
routes_module = Blueprint("routes_module", __name__)

# Directory where uploaded files will be saved temporarily
dir_path = "uploads/"


# Redirect to non-trailing slash path
@routes_module.before_request
def clear_trailing():
    rp = request.path
    if rp != "/" and rp.endswith("/"):
        return redirect(rp[:-1], code=301)


# Home page
@routes_module.route("/", methods=["GET"])
def homePage():
    return redirect("/upload")


# Search for molecules in database
@routes_module.route("/search", methods=["GET", "POST"])
def searchPage():
    if request.method == "GET":
        return render_template("search.html")
    elif request.method == "POST":
        query_type = request.form["query_type"]
        query_text = request.form["query_text"]
        d = {"success": 1, "results": []}
        return jsonify(d)


# Upload a log file and view parsed info from it
@routes_module.route("/upload", methods=["GET", "POST"])
def uploadLogfile():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        f = request.files["file"]
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        new_log_file_name = newLogFileName()
        f.save(new_log_file_name)
        d = processFile(new_log_file_name)
        os.remove(new_log_file_name)
        return json.dumps(d, sort_keys=True)


# Standalone 3Dmol viewer
@routes_module.route("/3Dviewer", methods=["GET"])
def viewerPage():
    if request.method == "GET":
        return render_template("3Dviewer.html")


# Utility to store uploaded file with a unique random name
def newLogFileName():
    log_file_name = randomString()
    while os.path.isfile(dir_path+log_file_name+".log"):
        log_file_name = randomString()
    return dir_path+log_file_name+".log"


# Utility to get a random
def randomString():
    s = string.ascii_uppercase+string.ascii_lowercase+string.digits
    filekey = "".join(random.sample(s,20))
    return filekey

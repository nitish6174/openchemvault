from flask import request, render_template, redirect

from flaskapp.routes import routes_module
import flaskapp.shared_variables as var
import flaskapp.config as config


# Home page
@routes_module.route("/", methods=["GET"])
def home_page():
    return redirect("/upload")


# List entries in database
@routes_module.route("/browse", methods=["GET"])
def list_page():
    if request.method == "GET":
        count = var.mongo.db[config.mongo_collection].count({})
        return render_template("browse.html", count=count)


# Search for molecules in database
@routes_module.route("/search", methods=["GET"])
def search_page():
    if request.method == "GET":
        return render_template("search.html")


# Upload a log file and view parsed info from it
@routes_module.route("/upload", methods=["GET"])
def upload_file_page():
    if request.method == "GET":
        return render_template("upload.html")


# Standalone 3Dmol viewer
@routes_module.route("/3Dviewer", methods=["GET"])
def viewer_page():
    if request.method == "GET":
        return render_template("3Dviewer.html")

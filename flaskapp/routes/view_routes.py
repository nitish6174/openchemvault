import urllib.parse

from flask import request, render_template, redirect
from bson import ObjectId

from flaskapp.routes import routes_module
import flaskapp.shared_variables as var
from flaskapp.process import XYZ_data


# Home page
@routes_module.route("/", methods=["GET"])
def home_page():
    return redirect("/upload")


# List molecules in database
@routes_module.route("/browse", methods=["GET"])
def browse_home_page():
    if request.method == "GET":
        mols = var.mongo.db.molecule.find({}).sort("formula")
        return render_template("browse.html", mode="home", mols=mols)


# List files for a molecule in database
@routes_module.route("/browse/<formula>", methods=["GET"])
def browse_molecule_page(formula):
    if request.method == "GET":
        formula = urllib.parse.unquote(formula)
        db = var.mongo.db
        mol_doc = db.molecule.find_one({"formula": formula})
        docs = []
        if mol_doc is not None:
            ids = mol_doc["parsed_files"]
            docs = db.parsed_file.find({"_id": {"$in": ids}})
        return render_template("browse.html",
                               mode="molecule",
                               formula=formula,
                               docs=docs)


# View a particular parsed file
@routes_module.route("/view/<doc_id>", methods=["GET"])
def view_file_page(doc_id):
    if request.method == "GET":
        db = var.mongo.db
        doc = db.parsed_file.find_one({"_id": ObjectId(doc_id)})
        success = 0
        if doc is not None:
            success = 1
            xyz_data = XYZ_data(doc["attributes"])
            if xyz_data != "":
                doc["xyz_data"] = xyz_data
            return render_template("view.html", success=success, doc=doc)
        else:
            return render_template("view.html", success=success)


# Search for molecules in database
@routes_module.route("/search", methods=["GET"])
def search_page():
    if request.method == "GET":
        return render_template("search.html")


# Search results
@routes_module.route("/search/type=<search_type>:query=<query>", methods=["GET"])
def search_results_page(search_type, query):
    if request.method == "GET":
        allowed_search_types = ["formula"]
        if search_type in allowed_search_types:
            query = urllib.parse.unquote(query)
            db = var.mongo.db
            temp = query.split()
            elems = [temp[i] for i in range(len(temp)) if i%2==0]
            mol_docs = db.molecule.find({"elements": {"$all": elems}})
            if mol_docs.count() > 0:
                return render_template("search.html",
                                       search_status=1,
                                       query=query,
                                       search_type=search_type,
                                       molecules=mol_docs)
            else:
                message = "No results found for this query"
                return render_template("search.html",
                                       search_status=0,
                                       query=query,
                                       search_type=search_type,
                                       message=message)
        else:
            message = "No results found for this query"
            return render_template("search.html",
                                   search_status=0,
                                   query=query,
                                   search_type=search_type,
                                   message=message)


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

import urllib.parse

from flask import request, render_template, redirect
from bson import ObjectId

from flaskapp.routes import routes_module
import flaskapp.shared_variables as var
from flaskapp.process.chem_process import XYZ_data
import flaskapp.process.formula_util as util


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
            q_formula_d = util.formula_query_parsing(query)
            if q_formula_d is not None:
                elems, counts = util.formula_dict_to_array(q_formula_d)
                db = var.mongo.db
                mol_docs = db.molecule.find({"elements": {"$all": elems}})
                if mol_docs.count() > 0:
                    mol_docs = [x for x in mol_docs]
                    for x in mol_docs:
                        x_formula_d = util.formula_array_to_dict(x["elements"],
                                                                 x["element_counts"])
                        x["dist"] = util.formula_distance(q_formula_d, x_formula_d)
                    mol_docs.sort(key=lambda x: x["dist"])
                    return render_template("search.html",
                                           search_status=1,
                                           query=query,
                                           search_type=search_type,
                                           molecules=mol_docs)
                else:
                    message = "No results found for this query"
            else:
                message = "Invalid formula"
        else:
            message = "Invalid search type"
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

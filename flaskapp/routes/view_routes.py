import urllib.parse

from flask import render_template, redirect
from bson import ObjectId

from flaskapp.routes import routes_module
import flaskapp.shared_variables as var
from flaskapp.process.chem_process import XYZ_data
from flaskapp.process.search_filter import apply_search_filter
from flaskapp.process.db_process import get_attribute_stats


# Home page
@routes_module.route("/", methods=["GET"])
def home_page():
    return redirect("/upload")


# List molecules in database
@routes_module.route("/browse", methods=["GET"])
def browse_home_page():
    db = var.mongo.db
    mols = db.molecule.find({}).sort("formula")
    return render_template("browse.html", mode="home", mols=mols)


# List files for a molecule in database
@routes_module.route("/browse/<formula>", methods=["GET"])
def browse_molecule_page(formula):
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
    stats = get_attribute_stats(True)
    return render_template("search.html", stats=stats)


# Search results
@routes_module.route("/search/<search_params>", methods=["GET"])
def search_results_page(search_params):
    stats = get_attribute_stats(True)
    try:
        param_list = search_params.split(":")
        search_key_val = [x.split("=") for x in param_list]
        search_keys = [x[0] for x in search_key_val]
        for x in search_key_val:
            x[1] = urllib.parse.unquote(x[1])
    except:
        message = "Invalid search query"
        return render_template("search.html",
                               stats=stats,
                               status=-1,
                               message=message)
    # This list is also defined in setup_db.py, search.html
    allowed_search_keys = [
        "charge",
        "enthalpy",
        "entropy",
        "formula",
        "freeenergy",
        "mult",
        "natom",
        "nbasis",
        "nmo",
        "package",
        "temperature"
    ]
    if not set(search_keys) <= set(allowed_search_keys):
        unsupported_keys = set(search_keys) - set(allowed_search_keys)
        unsupported_keys = ", ".join(unsupported_keys)
        d = {
            "status": 0,
            "message": "Unsupported search type : " + unsupported_keys
        }
    else:
        db = var.mongo.db
        docs = list(db.parsed_file.find({}))
        for x in search_key_val:
            docs = apply_search_filter(docs, x[0], x[1])
            if docs is None:
                invalid_key = x[0]
                break
        if docs is None:
            d = {
                "status": 0,
                "message": "Invalid value given for : " + invalid_key
            }
        else:
            d = {
                "status": 1,
                "docs": docs
            }
        d["params"] = {}
        for x in search_key_val:
            d["params"][x[0]] = x[1]
    d["stats"] = stats
    return render_template("search.html", **d)


# Upload a log file and view parsed info from it
@routes_module.route("/upload", methods=["GET"])
def upload_file_page():
    return render_template("upload.html")


# Standalone 3Dmol viewer
@routes_module.route("/3Dviewer", methods=["GET"])
def viewer_page():
    return render_template("3Dviewer.html")

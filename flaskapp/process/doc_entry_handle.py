import os

import numpy as np
from cclib.bridge.cclib2openbabel import makeopenbabel
import openbabel as ob

from flaskapp.process.chem_process import parse_file
from flaskapp.shared_variables import mongo, search_attrs


# Parse a file and continue to adding parsed data to data repository
def add_file_to_database(db=None, file_path=None, store_file_path=False):
    print("Processing file : ", file_path, ". . . ", end="")
    res = parse_file(file_path)
    if res["success"]:
        if "formula_string" not in res:
            print("  Failed: Unable to determine molecular formula")
        else:
            add_data_to_database(res, db, file_path, store_file_path)
            print("  Done!")
    else:
        print("  Failed: Unable to parse the file")


# Add parsed data to database if parsing was successful
def add_data_to_database(res, db=None, file_path=None, store_file_path=False):
    if db is None:
        db = mongo.db
    if res["success"] is True:
        if "formula_string" not in res:
            return {
                "success": False,
                "message": "Unable to determine molecular formula"
            }
        else:
            inserted_id = insert_data(res, db, file_path, store_file_path)
            if inserted_id is not None:
                generate_svg(res, inserted_id)
                update_stats(res, db)
                return {
                    "success": True,
                    "message": "File added to data repository",
                    "inserted_id": inserted_id
                }
            else:
                return {
                    "success": False,
                    "message": "Unable to insert parsed data"
                }
    else:
        return {
            "success": False,
            "message": "Unable to parse the file"
        }


# Insert given parsed data in database
def insert_data(data, db, file_path, store_file_path):
    formula = data["formula_string"]
    new_parsed_file_doc = {
        "attributes": data["attributes"],
        "formula_string": formula,
        "formula_dict": data["formula"]
    }
    if store_file_path is True:
        new_parsed_file_doc["file_path"] = file_path
    if "InChI" in data:
        new_parsed_file_doc["InChI"] = data["InChI"]
    res = db.molecule.find_one({"formula": formula}, {"_id": 1})
    try:
        if res is None:
            temp = formula.split()
            elems = [temp[i] for i in range(len(temp)) if i % 2 == 0]
            elem_counts = [temp[i] for i in range(len(temp)) if i % 2 == 1]
            new_molecule_doc = {
                "formula": formula,
                "elements": elems,
                "element_counts": elem_counts,
                "parsed_files": []
            }
            db.molecule.insert_one(new_molecule_doc)
        res = db.parsed_file.insert_one(new_parsed_file_doc)
        db.molecule.update_one({"formula": formula},
                               {"$push": {"parsed_files": res.inserted_id}})
        return str(res.inserted_id)
    except Exception as e:
        print("Error in inserting document")
        print("-" * 50)
        print(e)
        print("-" * 50)
        return None


# Generate SVG file for each inserted document
def generate_svg(res, inserted_id):
    dir_path = "flaskapp/static/svg/"
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    try:
        params = {
            "atomcoords": np.asarray(res["atomcoords"]),
            "atomnos": np.asarray(res["atomnos"]),
            "charge": res["charge"],
            "mult": res["mult"]
        }
    except:
        pass
    try:
        # Save the SVG file with filename same as mongodb document id
        file_path = dir_path + inserted_id + ".svg"
        print("Creating SVG : " + file_path)
        mol = makeopenbabel(**params)
        obconversion = ob.OBConversion()
        obconversion.SetOutFormat("svg")
        ob.obErrorLog.StopLogging()
        obconversion.WriteFile(mol, file_path)
    except:
        pass


# Find min and max value for each applicable attribute
def update_stats(res, db):
    stats_attrs = [x["key"] for x in search_attrs if x["range"] == 1]
    count = db.attr_stats.count({})
    if count == 0:
        new_stats = {}
        for x in stats_attrs:
            if x in res["attributes"]:
                new_stats[x] = {}
                new_stats[x]["min"] = res["attributes"][x]
                new_stats[x]["max"] = res["attributes"][x]
        db.attr_stats.insert_one(new_stats)
    else:
        doc = list(db.attr_stats.find({}))[0]
        for x in stats_attrs:
            if x in res["attributes"]:
                if x not in doc:
                    doc[x] = {}
                    doc[x]["min"] = res["attributes"][x]
                    doc[x]["max"] = res["attributes"][x]
                else:
                    doc[x]["min"] = min(doc[x]["min"], res["attributes"][x])
                    doc[x]["max"] = max(doc[x]["max"], res["attributes"][x])
        db.attr_stats.find_one_and_replace({"_id": doc["_id"]}, doc)

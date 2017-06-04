import flaskapp.process.formula_util as util


def apply_search_filter(docs, key, value):
    filtered_docs = []
    range_check = {
        "charge": "int",
        "enthalpy": "float",
        "entropy": "float",
        "freeenergy": "float",
        "mult": "int",
        "natom": "int",
        "nbasis": "int",
        "nmo": "int",
        "temperature": "float"
    }
    if key == "formula":
        d = util.formula_query_parsing(value)
        if d is not None:
            formula_s = util.make_formula_string(d)
            filtered_docs = list(filter(
                lambda x: (
                    ("formula_string" in x) and
                    (x["formula_string"] == formula_s)
                ), docs
            ))
        else:
            return None
    elif key in range_check:
        try:
            if range_check[key] == "int":
                min_val, max_val = map(int, value.split(","))
            else:
                min_val, max_val = map(float, value.split(","))
            filtered_docs = list(filter(
                lambda x: (
                    (key in x["attributes"]) and
                    (x["attributes"][key] >= min_val) and
                    (x["attributes"][key] <= max_val)
                ), docs
            ))
        except:
            return None
    elif key == "package":
        try:
            filtered_docs = list(filter(
                lambda x: (
                    ("metadata" in x["attributes"]) and
                    ("package" in x["attributes"]["metadata"]) and
                    (x["attributes"]["metadata"]["package"] == value)
                ), docs
            ))
        except:
            return None
    return filtered_docs

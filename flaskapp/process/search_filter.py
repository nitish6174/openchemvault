import flaskapp.process.formula_util as util


def apply_search_filter(docs, key, value):
    filtered_docs = []
    if key == "formula":
        d = util.formula_query_parsing(value)
        if d is not None:
            formula_s = util.make_formula_string(d)
            filtered_docs = list(filter(
                lambda x: x["formula_string"] == formula_s, docs
            ))
        else:
            return None
    return filtered_docs

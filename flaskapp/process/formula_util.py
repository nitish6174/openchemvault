from cclib.parser.utils import PeriodicTable


def formula_query_parsing(query):
    query = query.replace(" ", "")
    if query.isalnum() and query[0].isupper():
        formula_dict = {}
        elem, count = "", ""
        for c in query:
            if c.isupper():
                update_dict(formula_dict, elem, count)
                elem = c
                count = ""
            elif c.islower():
                elem = elem + c
            else:
                count = count + c
        update_dict(formula_dict, elem, count)
        return formula_dict
    return None


def update_dict(d, elem, count):
    if elem != "":
        if count == "":
            count = 1
        if elem in d:
            d[elem] += int(count)
        else:
            d[elem] = int(count)


def formula_dict_to_array(formula_dict):
    elems, counts = [], []
    for k in formula_dict:
        elems.append(k)
        counts.append(int(formula_dict[k]))
    return elems, counts


def formula_array_to_dict(elems, counts):
    formula_dict = {}
    for (k, v) in zip(elems, counts):
        formula_dict[k] = int(v)
    return formula_dict


def formula_distance(query_formula, data_record_formula):
    dist = 0
    for k in data_record_formula:
        if k not in query_formula:
            dist += 1000
        else:
            dist += abs(data_record_formula[k] - query_formula[k])
    return dist


def make_formula_string(elems, elem_counts=[]):
    periodic_obj = PeriodicTable()
    formula_arr = []
    if type(elems) is dict:
        for x in elems:
            formula_arr.append({
                "atomno": periodic_obj.number[x],
                "symbol": x,
                "count": elems[x]
            })
    else:
        for (x, y) in zip(elems, elem_counts):
            formula_arr.append({
                "atomno": periodic_obj.number[x],
                "symbol": x,
                "count": y
            })
    formula_arr.sort(key=lambda x: x["atomno"])
    formula_arr = [x["symbol"] + " " + str(x["count"]) for x in formula_arr]
    formula_string = " ".join(formula_arr)
    return formula_string

from cclib.parser.utils import PeriodicTable
from cclib.io import ccopen, ccread
from cclib.bridge.cclib2openbabel import makeopenbabel
try:
    import openbabel as ob
    ob_import = True
except:
    ob_import = False


def process_file(file_path):
    logfile_type = ccopen(file_path)
    if logfile_type is not None:
        try:
            parsed_data = ccread(file_path)
            parsed_data.listify()
            res = {
                "success": True,
                "attributes": {}
            }
            for x in parsed_data._attributes:
                try:
                    val = getattr(parsed_data, x)
                    res["attributes"][x] = val
                except:
                    pass
            if ob_import is True:
                inchi = get_InChI(res["attributes"])
                if inchi is not None:
                    res["InChI"] = inchi
        except:
            res = {"success": False}
    else:
        res = {"success": False}
    if res["success"]:
        chemical_formula(res["attributes"])
        res["xyz_data"] = XYZ_data(res["attributes"])
    return res


def chemical_formula(d):
    periodic_obj = PeriodicTable()
    try:
        atom_dict = {}
        for x in d["atomnos"]:
            if x in atom_dict:
                atom_dict[x] += 1
            else:
                atom_dict[x] = 1
        atom_arr = []
        for x in atom_dict:
            atom_arr.append({"atomno": x, "count": atom_dict[x]})
        atom_arr.sort(key=lambda x: x["atomno"])
        formula_dict = {}
        formula_str = ""
        for x in atom_arr:
            elem = periodic_obj.element[x["atomno"]]
            formula_dict[elem] = x["count"]
            formula_str = formula_str + elem + " " + str(x["count"]) + " "
        d["formula"] = formula_dict
        d["formula_string"] = formula_str[:-1]
    except:
        pass


def XYZ_data(d):
    periodic_obj = PeriodicTable()
    xyz_data = ""
    try:
        xyz_data += str(d["natom"]) + "\n\n"
        for atom_row in list(zip(d["atomnos"], d["atomcoords"][0])):
            elem = periodic_obj.element[atom_row[0]]
            coords_text = " ".join(list(map(str, atom_row[1])))
            xyz_data += elem + " " + coords_text + "\n"
    except:
        xyz_data = ""
    return xyz_data


def get_InChI(attr):
    try:
        params = {
            "atomcoords": getattr(attr, "atomcoords"),
            "atomnos": getattr(attr, "atomnos"),
            "charge": getattr(attr, "charge"),
            "mult": getattr(attr, "mult")
        }
        mol = makeopenbabel(**params)
        obconversion = ob.OBConversion()
        obconversion.SetOutFormat("inchi")
        ob.obErrorLog.StopLogging()
        return obconversion.WriteString(mol).strip()
    except:
        return None

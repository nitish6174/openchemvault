import numpy as np

from cclib.parser.utils import PeriodicTable
from cclib.io import ccopen, ccread
from cclib.bridge.cclib2openbabel import makeopenbabel
try:
    import openbabel as ob
    ob_import = True
except:
    ob_import = False


def parse_file(file_path):
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
                except Exception as e:
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
        make_chemical_formula(res)
        res["xyz_data"] = XYZ_data(res["attributes"])
    return res


def make_chemical_formula(d):
    periodic_obj = PeriodicTable()
    try:
        atom_dict = {}
        atomsymbols = []
        for x in d["attributes"]["atomnos"]:
            atomsymbols.append(periodic_obj.element[x])
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
        d["attributes"]["atomsymbols"] = atomsymbols
        massnos = [round(x) for x in d["attributes"]["atommasses"]]
        d["attributes"]["massnos"] = massnos
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
            "atomcoords": np.asarray(attr["atomcoords"]),
            "atomnos": attr["atomnos"],
            "charge": attr["charge"],
            "mult": attr["mult"]
        }
        mol = makeopenbabel(**params)
        obconversion = ob.OBConversion()
        obconversion.SetOutFormat("inchi")
        ob.obErrorLog.StopLogging()
        inchi = obconversion.WriteString(mol).strip()
        if inchi.startswith("InChI="):
            inchi = inchi.replace("InChI=", "")
        return inchi
    except:
        return None

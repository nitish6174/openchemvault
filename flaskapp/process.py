from cclib.parser import *
from cclib.parser.utils import PeriodicTable
from cclib.io.ccio import ccopen, ccread

def processFile(file_path):
    logfile_type = ccopen(file_path)
    if logfile_type!=None:
        parsed_data = ccread(file_path)
        parsed_data.listify()
        res = {
            "success":True,
            "attributes":{}
        }
        for x in parsed_data._attributes:
            try:
                val = getattr(parsed_data,x)
                res["attributes"][x] = val
            except:
                pass
    else:
        res = {"success":False}
    if res["success"]:
        chemicalFormula(res["attributes"])
        res["xyz_data"] = XYZdata(res["attributes"])
    return res


def chemicalFormula(d):
    periodic_obj = PeriodicTable()
    try:
        atom_dict = {}
        for x in d["atomnos"]:
            if x in atom_dict:
                atom_dict[x] += 1
            else:
                atom_dict[x] = 1
        formula_dict = {}
        for x in atom_dict:
            elem = periodic_obj.element[x]
            formula_dict[elem] = atom_dict[x]
        d["formula"] = formula_dict
    except:
        pass

def XYZdata(d):
    periodic_obj = PeriodicTable()
    xyz_data = ""
    try:
        xyz_data += str(d["natom"])+"\n\n"
        for atom_row in list(zip(d["atomnos"],d["atomcoords"][0])):
            elem = periodic_obj.element[atom_row[0]]
            coords_text = " ".join(list(map(str,atom_row[1])))
            xyz_data += elem + " " + coords_text + "\n"
    except:
        xyz_data = ""
    return xyz_data

# This function is redundant as it is already been implemented in cclib
# 
# def convertToList(a):
#     try:
#         a = a.tolist()
#     except:
#         pass
#     if isinstance(a,list):
#         try:
#             b = a[0].tolist()
#             d = [ x.tolist() for x in a ]
#         except:
#             d = a
#         return d
#     elif isinstance(a,dict):
#         for k in a:
#             try:
#                 a[k] = a[k].tolist()
#             except:
#                 a[k] = a[k]
#     return a

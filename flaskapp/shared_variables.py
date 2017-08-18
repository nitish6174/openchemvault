from flask_pymongo import PyMongo

# MongoDB client
mongo = PyMongo()

# Search attributes. Ones with range key value of 1 are used in database stats
search_attrs = [
    {"key": "formula"     , "range": 0, "title": "Molecular formula"},
    {"key": "package"     , "range": 0, "title": "Package"},
    {"key": "natom"       , "range": 1, "title": "No of atoms" , "int": 1},
    {"key": "charge"      , "range": 1, "title": "Charge"      , "int": 1},
    {"key": "enthalpy"    , "range": 1, "title": "Enthalpy"    , "int": 0},
    {"key": "entropy"     , "range": 1, "title": "Entropy"     , "int": 0},
    {"key": "freeenergy"  , "range": 1, "title": "Free energy" , "int": 0},
    {"key": "mult"        , "range": 1, "title": "Mult"        , "int": 1},
    {"key": "nbasis"      , "range": 1, "title": "nbasis"      , "int": 1},
    {"key": "nmo"         , "range": 1, "title": "nmo"         , "int": 1},
    {"key": "temperature" , "range": 1, "title": "Temperature" , "int": 0}
]

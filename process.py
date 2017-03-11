from cclib.parser import *
import numpy as np

def processFile(file_path,mode):
    if mode=="ADF":
        p = ADF(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="DALTON":
        p = DALTON(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="Gaussian":
        p = Gaussian(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="Jaguar":
        p = Jaguar(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="Molpro":
        p = Molpro(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="NWChem":
        p = NWChem(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="ORCA":
        p = ORCA(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="Psi":
        p = Psi(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    elif mode=="Q-Chem":
        p = Q-Chem(file_path)
        d = p.parse()
        res = {
            "atombasis" : d.atombasis,
            "atomcoords" : d.atomcoords.tolist(),
            "atomnos" : d.atomnos.tolist(),
            "charge" : d.charge,
            "coreelectrons" : d.coreelectrons.tolist(),
            "natom" : d.natom
        }
    else:
        res = {}
    return res

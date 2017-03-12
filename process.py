from cclib.parser import *
from cclib.parser.utils import PeriodicTable

def processFile(file_path,mode):
    if mode=="ADF":
        p = ADF(file_path)
        res = parseData(p)
    elif mode=="DALTON":
        p = DALTON(file_path)
        res = parseData(p)
    elif mode=="Gaussian":
        p = Gaussian(file_path)
        res = parseData(p)
    elif mode=="Jaguar":
        p = Jaguar(file_path)
        res = parseData(p)
    elif mode=="Molpro":
        p = Molpro(file_path)
        res = parseData(p)
    elif mode=="NWChem":
        p = NWChem(file_path)
        res = parseData(p)
    elif mode=="ORCA":
        p = ORCA(file_path)
        res = parseData(p)
    elif mode=="Psi":
        p = Psi(file_path)
        res = parseData(p)
    elif mode=="QChem":
        p = QChem(file_path)
        res = parseData(p)
    else:
        res = {"success":False}
    if res["success"]:
        chemicalFormula(res["data"])
    return res

def parseData(p):
    try:
        d = p.parse()
        try:
            aonames = d.aonames
            aonames = convertToList(aonames)
        except:
            aonames = "N/A"
        try:
            aooverlaps = d.aooverlaps
            aooverlaps = convertToList(aooverlaps)
        except:
            aooverlaps = "N/A"
        try:
            atombasis = d.atombasis
            atombasis = convertToList(atombasis)
        except:
            atombasis = "N/A"
        # try:
        #     atomcharges = d.atomcharges
        #     atomcharges = convertToList(atomcharges)
        # except:
        #     atomcharges = "N/A"
        try:
            atomcoords = d.atomcoords
            atomcoords = convertToList(atomcoords)
        except:
            atomcoords = "N/A"
        # try:
        #     atommasses = d.atommasses
        #     atommasses = convertToList(atommasses)
        # except:
        #     atommasses = "N/A"
        try:
            atomnos = d.atomnos
            atomnos = convertToList(atomnos)
        except:
            atomnos = "N/A"
        # try:
        #     atomspins = d.atomspins
        #     atomspins = convertToList(atomspins)
        # except:
        #     atomspins = "N/A"
        try:
            ccenergies = d.ccenergies
            ccenergies = convertToList(ccenergies)
        except:
            ccenergies = "N/A"
        try:
            charge = d.charge
            charge = convertToList(charge)
        except:
            charge = "N/A"
        try:
            coreelectrons = d.coreelectrons
            coreelectrons = convertToList(coreelectrons)
        except:
            coreelectrons = "N/A"
        # try:
        #     enthalpy = d.enthalpy
        #     enthalpy = convertToList(enthalpy)
        # except:
        #     enthalpy = "N/A"
        # try:
        #     entropy = d.entropy
        #     entropy = convertToList(entropy)
        # except:
        #     entropy = "N/A"
        # try:
        #     etenergies = d.etenergies
        #     etenergies = convertToList(etenergies)
        # except:
        #     etenergies = "N/A"
        # try:
        #     etoscs = d.etoscs
        #     etoscs = convertToList(etoscs)
        # except:
        #     etoscs = "N/A"
        # try:
        #     etrotats = d.etrotats
        #     etrotats = convertToList(etrotats)
        # except:
        #     etrotats = "N/A"
        # try:
        #     etsecs = d.etsecs
        #     etsecs = convertToList(etsecs)
        # except:
        #     etsecs = "N/A"
        # try:
        #     etsyms = d.etsyms
        #     etsyms = convertToList(etsyms)
        # except:
        #     etsyms = "N/A"
        # try:
        #     fonames = d.fonames
        #     fonames = convertToList(fonames)
        # except:
        #     fonames = "N/A"
        # try:
        #     fooverlaps = d.fooverlaps
        #     fooverlaps = convertToList(fooverlaps)
        # except:
        #     fooverlaps = "N/A"
        # try:
        #     fragnames = d.fragnames
        #     fragnames = convertToList(fragnames)
        # except:
        #     fragnames = "N/A"
        # try:
        #     frags = d.frags
        #     frags = convertToList(frags)
        # except:
        #     frags = "N/A"
        # try:
        #     freeenergy = d.freeenergy
        #     freeenergy = convertToList(freeenergy)
        # except:
        #     freeenergy = "N/A"
        try:
            gbasis = d.gbasis
            gbasis = convertToList(gbasis)
        except:
            gbasis = "N/A"
        try:
            geotargets = d.geotargets
            geotargets = convertToList(geotargets)
        except:
            geotargets = "N/A"
        try:
            geovalues = d.geovalues
            geovalues = convertToList(geovalues)
        except:
            geovalues = "N/A"
        # try:
        #     grads = d.grads
        #     grads = convertToList(grads)
        # except:
        #     grads = "N/A"
        # try:
        #     hessian = d.hessian
        #     hessian = convertToList(hessian)
        # except:
        #     hessian = "N/A"
        try:
            homos = d.homos
            homos = convertToList(homos)
        except:
            homos = "N/A"
        # try:
        #     metadata = d.metadata
        #     metadata = convertToList(metadata)
        # except:
        #     metadata = "N/A"
        try:
            mocoeffs = d.mocoeffs
            mocoeffs = convertToList(mocoeffs)
        except:
            mocoeffs = "N/A"
        try:
            moenergies = d.moenergies
            moenergies = convertToList(moenergies)
        except:
            moenergies = "N/A"
        try:
            moments = d.moments
            moments = convertToList(moments)
        except:
            moments = "N/A"
        try:
            mosyms = d.mosyms
            mosyms = convertToList(mosyms)
        except:
            mosyms = "N/A"
        try:
            mpenergies = d.mpenergies
            mpenergies = convertToList(mpenergies)
        except:
            mpenergies = "N/A"
        try:
            mult = d.mult
            mult = convertToList(mult)
        except:
            mult = "N/A"
        try:
            natom = d.natom
            natom = convertToList(natom)
        except:
            natom = "N/A"
        try:
            nbasis = d.nbasis
            nbasis = convertToList(nbasis)
        except:
            nbasis = "N/A"
        try:
            nmo = d.nmo
            nmo = convertToList(nmo)
        except:
            nmo = "N/A"
        # try:
        #     nocoeffs = d.nocoeffs
        #     nocoeffs = convertToList(nocoeffs)
        # except:
        #     nocoeffs = "N/A"
        # try:
        #     nooccnos = d.nooccnos
        #     nooccnos = convertToList(nooccnos)
        # except:
        #     nooccnos = "N/A"
        try:
            optdone = d.optdone
            optdone = convertToList(optdone)
        except:
            optdone = "N/A"
        # try:
        #     optstatus = d.optstatus
        #     optstatus = convertToList(optstatus)
        # except:
        #     optstatus = "N/A"
        # try:
        #     polarizabilities = d.polarizabilities
        #     polarizabilities = convertToList(polarizabilities)
        # except:
        #     polarizabilities = "N/A"
        # try:
        #     scancoords = d.scancoords
        #     scancoords = convertToList(scancoords)
        # except:
        #     scancoords = "N/A"
        # try:
        #     scanenergies = d.scanenergies
        #     scanenergies = convertToList(scanenergies)
        # except:
        #     scanenergies = "N/A"
        # try:
        #     scannames = d.scannames
        #     scannames = convertToList(scannames)
        # except:
        #     scannames = "N/A"
        # try:
        #     scanparm = d.scanparm
        #     scanparm = convertToList(scanparm)
        # except:
        #     scanparm = "N/A"
        try:
            scfenergies = d.scfenergies
            scfenergies = convertToList(scfenergies)
        except:
            scfenergies = "N/A"
        try:
            scftargets = d.scftargets
            scftargets = convertToList(scftargets)
        except:
            scftargets = "N/A"
        try:
            scfvalues = d.scfvalues
            scfvalues = convertToList(scfvalues)
        except:
            scfvalues = "N/A"
        # try:
        #     temperature = d.temperature
        #     temperature = convertToList(temperature)
        # except:
        #     temperature = "N/A"
        # try:
        #     time = d.time
        #     time = convertToList(time)
        # except:
        #     time = "N/A"
        # try:
        #     vibanharms = d.vibanharms
        #     vibanharms = convertToList(vibanharms)
        # except:
        #     vibanharms = "N/A"
        try:
            vibdisps = d.vibdisps
            vibdisps = convertToList(vibdisps)
        except:
            vibdisps = "N/A"
        try:
            vibfreqs = d.vibfreqs
            vibfreqs = convertToList(vibfreqs)
        except:
            vibfreqs = "N/A"
        try:
            vibirs = d.vibirs
            vibirs = convertToList(vibirs)
        except:
            vibirs = "N/A"
        # try:
        #     vibramans = d.vibramans
        #     vibramans = convertToList(vibramans)
        # except:
        #     vibramans = "N/A"
        # try:
        #     vibsyms = d.vibsyms
        #     vibsyms = convertToList(vibsyms)
        # except:
        #     vibsyms = "N/A"
        data = {
            "aonames" : aonames,
            "aooverlaps" : aooverlaps,
            "atombasis" : atombasis,
            # "atomcharges" : atomcharges,
            "atomcoords" : atomcoords,
            # "atommasses" : atommasses,
            "atomnos" : atomnos,
            # "atomspins" : atomspins,
            "ccenergies" : ccenergies,
            "charge" : charge,
            "coreelectrons" : coreelectrons,
            # "enthalpy" : enthalpy,
            # "entropy" : entropy,
            # "etenergies" : etenergies,
            # "etoscs" : etoscs,
            # "etrotats" : etrotats,
            # "etsecs" : etsecs,
            # "etsyms" : etsyms,
            # "fonames" : fonames,
            # "fooverlaps" : fooverlaps,
            # "fragnames" : fragnames,
            # "frags" : frags,
            # "freeenergy" : freeenergy,
            "gbasis" : gbasis,
            "geotargets" : geotargets,
            "geovalues" : geovalues,
            # "grads" : grads,
            # "hessian" : hessian,
            "homos" : homos,
            # "metadata" : metadata,
            "mocoeffs" : mocoeffs,
            "moenergies" : moenergies,
            "moments" : moments,
            "mosyms" : mosyms,
            "mpenergies" : mpenergies,
            "mult" : mult,
            "natom" : natom,
            "nbasis" : nbasis,
            "nmo" : nmo,
            # "nocoeffs" : nocoeffs,
            # "nooccnos" : nooccnos,
            "optdone" : optdone,
            # "optstatus" : optstatus,
            # "polarizabilities" : polarizabilities,
            # "scancoords" : scancoords,
            # "scanenergies" : scanenergies,
            # "scannames" : scannames,
            # "scanparm" : scanparm,
            "scfenergies" : scfenergies,
            "scftargets" : scftargets,
            "scfvalues" : scfvalues,
            # "temperature" : temperature,
            # "time" : time,
            # "vibanharms" : vibanharms,
            "vibdisps" : vibdisps,
            "vibfreqs" : vibfreqs,
            "vibirs" : vibirs,
            # "vibramans" : vibramans,
            # "vibsyms" : vibsyms
        }
        res = {
            "success" : True,
            "data" : data
        }
    except:
        res = {
            "success" : False
        }
    return res

def chemicalFormula(d):
    if d["atomnos"]!="N/A":
        periodic_obj = PeriodicTable()
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

def convertToList(a):
    try:
        a = a.tolist()
    except:
        pass
    if isinstance(a,list):
        try:
            b = a[0].tolist()
            d = [ x.tolist() for x in a ]
        except:
            d = a
        return d
    elif isinstance(a,dict):
        for k in a:
            try:
                a[k] = a[k].tolist()
            except:
                a[k] = a[k]
    return a

# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys
import estructuras as table

#List of ids in dirFunc
dirFuncs = {}
#List of ids in varsTable
varTable = {}

#Variables globales
myType = None
isGlobal = True
func = None
funcType = None

#Func that defines which insert use
def insert(id, type):
    if isGlobal:
        dirInsert(id, type)
    else:
        varsInsert(id, type)

#Inserts globalvar or func in dirFunc
def dirInsert(id, type):
    temp = table.table(id, type)
    if len(dirFuncs) > 0 and not repeatedDirId(id):
        dirFuncs[id] = temp
    if not dirFuncs:
        dirFuncs[id] = temp

#Checks if repeated id in dirFunc
def repeatedDirId(id):
    for ids in dirFuncs:
        if id == ids:
            print('Id en uso: ', id)
            sys.exit()
            return True
    return False

#Insert varibles in local varTable
def varsInsert(id, type):
    temp = table.table(id, type)
    if len(varTable) > 0 and not repeatedVarId(id):
        varTable[id] = temp
    if not varTable:
        varTable[id] = temp

#Checks if repeated id in local varTable
def repeatedVarId(id):
    for ids in varTable:
        if id == ids:
            print('Id en uso: ', id)
            sys.exit()
            return True
    return False

def dirPrint():
    for ids in dirFuncs:
        print('ID: ', ids, ', Type: ', dirFuncs[ids].type)

def varsPrint():
    for ids in varTable:
        print('ID: ', ids, ', Type: ', varTable[ids].type)

def getIdType(id):
    tipo = None
    for ids in varTable:
        if id == ids:
            tipo = varTable[ids].type
    if (tipo == None):
        for ids in dirFuncs:
            if id == ids:
                tipo = dirFuncs[ids].type
    return tipo



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
#List of cte
cteTable = []

#Variables globales
myType = None
isGlobal = True
func = None
funcType = None

#Variables de funciones
params = ''

#Func that defines which insert use
def insert(id, type, dir):
    if isGlobal:
        dirInsert(id, type, dir)
    else:
        varsInsert(id, type, dir)

#Inserts globalvar or func in dirFunc
def dirInsert(id, type, dir):
    temp = table.table(id, type, dir, None, None, None)
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
def varsInsert(id, type, dir):
    temp = table.table(id, type, dir, None, None, None)
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
        print('ID: ', ids, ', Type: ', dirFuncs[ids].type, ' Dir: ', dirFuncs[ids].dir, ' Params:', dirFuncs[ids].params, ' Size:', dirFuncs[ids].size, ' Quad:', dirFuncs[ids].quad)

def varsPrint():
    for ids in varTable:
        print('ID: ', ids, ', Type: ', varTable[ids].type, ' Dir: ', varTable[ids].dir)

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

#Table de constantes
def cteInsert(id, type, dir):
    cte = id
    temp = table.table(cte, type, dir, None, None, None)
    if len(cteTable) > 0 and not repeatedCte(cte):
        cteTable.append(temp)
        return True
    if not cteTable:
        cteTable.append(temp)
        return True
    return False

def repeatedCte(id):
    leng = len(cteTable)
    for ids in range(leng):
        if str(cteTable[ids].id) == str(id):
            return True
    return False

def ctePrint():
    leng = len(cteTable)
    for ids in range(leng):
        print('ID: ', cteTable[ids].id, ', Type: ', cteTable[ids].type, ' Dir: ', cteTable[ids].dir)

#Find associated memory
def findVM(id):
    for ids in varTable:
        if id == ids:
            return varTable[id].dir
    for ids in dirFuncs:
        if id == ids:
            return dirFuncs[id].dir

#Find associtaed memory of constants
def findCteVM(id):
    leng = len(cteTable)
    for ids in range(leng):
        if str(cteTable[ids].id) == str(id):
            return cteTable[ids].dir

def insertFuncParams(params, func):
    #print(func)
    for ids in dirFuncs:
        print(ids)
        if ids == func:
            dirFuncs[ids].params = params

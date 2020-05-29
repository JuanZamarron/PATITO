# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys
import estructuras as table

#List of global variables
gvarTable = {}
#List of ids in dirFunc
dirFuncs = {}
#List of ids in varsTable
varTable = {}
#List of cte
cteTable = []

#Tablas vectores y matrices
vectLTable = {}
vectGTable = {}

#Variables globales
myType = None
isGlobal = True
func = None
funcType = None
program = ''
vectSize = None
m = None
isVector = None

#Variables de funciones
func = ''
params = ''
#Contadores de variables locales
li = 0
lf = 0
lc = 0
lti = 0
ltf = 0
ltc = 0
ltb = 0
#Contadores de variables globales
gli = 0
glf = 0
glc = 0
glti = 0
gltf = 0
gltc = 0
gltb = 0
#Contador de cuadruplos
quad = 0

#Func insert in dirFunc
def insertDirFunc(id, type, dir):
    temp = table.table(id, type, dir, None, None, None)
    dirFuncs[id] = temp

#Func that defines which insert use
def insert(id, type, dir, salto):
    if isGlobal:
        dirInsert(id, type, dir, salto)
    else:
        varsInsert(id, type, dir, salto)

#Inserts globalvar
def dirInsert(id, type, dir, salto):
    temp = table.table(id, type, dir, None, None, None)
    if len(gvarTable) > 0 and not repeatedDirId(id):
        gvarTable[id] = temp
        gaddSize(type, salto)
    if not gvarTable:
        gvarTable[id] = temp
        gaddSize(type, salto)

#Checks if repeated id in gvarTable
def repeatedDirId(id):
    for ids in gvarTable:
        if id == ids:
            print('Id en uso: ', id)
            sys.exit()
            return True
    return False

#Insert varibles in local varTable
def varsInsert(id, type, dir, salto):
    temp = table.table(id, type, dir, None, None, None)
    if len(varTable) > 0 and not repeatedVarId(id):
        varTable[id] = temp
        addSize(type, salto)
    if not varTable:
        varTable[id] = temp
        addSize(type, salto)

def addSize(type, salto):
    global li
    global lf
    global lc
    if type == 'int':
        li += salto
    elif type == 'float':
        lf += salto
    elif type == 'char':
        lc += salto

def gaddSize(type, salto):
    global gli
    global glf
    global glc
    if type == 'int':
        gli += salto
    elif type == 'float':
        glf += salto
    elif type == 'char':
        glc += salto

def tempAddSize(type):
    global lti
    global ltf
    global ltc
    global ltb
    if type == 'int':
        lti += 1
    elif type == 'float':
        ltf += 1
    elif type == 'char':
        ltc += 1
    elif type == 'boolean':
        ltb += 1

def gtempAddSize(type):
    global glti
    global gltf
    global gltc
    global gltb
    if type == 'int':
        glti += 1
    elif type == 'float':
        gltf += 1
    elif type == 'char':
        gltc += 1
    elif type == 'boolean':
        gltb += 1

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
        print('ID: ', ids, ', Type: ', dirFuncs[ids].type, 'Dir: ', dirFuncs[ids].dir,' Params:', dirFuncs[ids].params, ' Size:', dirFuncs[ids].size, ' Quad:', dirFuncs[ids].quad)

def gvarPrint():
    for ids in gvarTable:
        print('ID: ', ids, ', Type: ', gvarTable[ids].type, ' Dir: ', gvarTable[ids].dir)

def varsPrint():
    for ids in varTable:
        print('ID: ', ids, ', Type: ', varTable[ids].type, ' Dir: ', varTable[ids].dir)

def getIdType(id):
    tipo = None
    for ids in varTable:
        if id == ids:
            tipo = varTable[ids].type
    if (tipo == None):
        for ids in gvarTable:
            if id == ids:
                tipo = gvarTable[ids].type
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
    for ids in gvarTable:
        if id == ids:
            return gvarTable[id].dir

#Find associtaed memory of constants
def findCteVM(id):
    leng = len(cteTable)
    for ids in range(leng):
        if str(cteTable[ids].id) == str(id):
            return cteTable[ids].dir
    return False

def insertFuncParams(params, func):
    #print(func)
    for ids in dirFuncs:
        if ids == func:
            dirFuncs[ids].params = params

def insertFuncSize(size, func):
    for ids in dirFuncs:
        if ids == func:
            dirFuncs[ids].size = size

def clearVarSize():
    global li
    global lf
    global lc
    global lti
    global ltf
    global ltc
    global ltb
    li = 0
    lf = 0
    lc = 0
    lti = 0
    ltf = 0
    ltc = 0
    ltb = 0
    
def insertFuncQuad(quad, func):
    for ids in dirFuncs:
        if ids == func:
            dirFuncs[ids].quad = quad

def gVectPrint():
    for ids in vectGTable:
        print('ID: ', ids, ', Lim1: ', vectGTable[ids].lim1, ' Lim2:', vectGTable[ids].lim2, ' M:', vectGTable[ids].m, ' Size:', vectGTable[ids].size)

def dirlVect():
    for ids in dirFuncs:
        print('ID: ', ids, ', Type: ', dirFuncs[ids].type, ' Params:', dirFuncs[ids].params, ' Size:', dirFuncs[ids].size, ' Quad:', dirFuncs[ids].quad)

def findLVector(dir):
    for ids in vectLTable:
        if ids == dir:
            return True
    return False
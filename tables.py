# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys
import estructuras as table

# List of ids in dirFunc
dirFuncs = {}
# List of ids in varsTable
varTable = {}  # simbolos

# Array of pa
# ramethers
paramArray = []

# Variables globales
myType = None

isGlobal = True
func = None
funcType = None
funcParam = None
isParam = False
isGlobal = False
contParams = 0
existLocal = False
existGlobal = False

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

# Checks if repeated id in local varTable
def repeatedVarId(id):
    for ids in varTable:
        if id == ids:
            print('ERROR: Var Id en uso: ', id)
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


# Función que retorna una lista con las variables que son parámetros dentro de la función.
def getidParam(idFunc):
    temp = []
    for id in varTable[idFunc].value:
        if varTable[idFunc].value[id].param:
            temp.append(id)
    return temp


# Función que actualiza el valor de una variable.
def updateIdOfFun(id, idOfFunc, valor):
     print('updateIdOfFun')
     if validate(valor, id, idOfFunc):
        temp = str(type(valor))
        if temp == "<class 'str'>":
            valor = valor.replace('"', '')
            varTable[idOfFunc].value[id].value = valor
        else:
            varTable[idOfFunc].value[id].value = valor


# Función que valida que el valor ingresado y el tipo de la variable
# sean iguales.
def validate(dato, id, idOfFunc):
    temp = volverFloat(dato, id, idOfFunc)
    aux = None
    existLocal = False
    existGlobal = False
    if id in varTable[idOfFunc].value:
        aux = varTable[idOfFunc].value[id].type_data
        existLocal = True
    if "global" in varTable.keys():
        if id in varTable["global"].value:
            aux = varTable["global"].value[id].type_data
            existGlobal = True
    if not existLocal and not existGlobal:
        print('ERROR: ID no declarado:', id)
        sys.exit()

    if dato == 'true' or dato == 'false':
        temp = "<class 'bool'>"
    if temp == "<class 'float'>" and aux == 'float':
        return True
    if temp == "<class 'int'>" and aux == 'int':
        return True
    if temp == "<class 'str'>" and aux == 'string':
        return True
    if temp == "<class 'bool'>" and aux == 'bool':
        return True
    if temp == None:
        print(id, "Debes Asignar un Valor")
        sys.exit()
    else:
        print("ERROR: Dato no válido.", dato, id, idOfFunc)
        sys.exit()


def volverFloat(dato, id, idOfFunc):
    temp = str(type(dato))
    if varTable[idOfFunc].value[id].type_data == 'float' and temp == "<class 'int'>":
        temp = "<class 'float'>"
    return temp

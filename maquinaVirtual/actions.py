# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

import sys
import memoria as memo
import fileReader
import numpy as np

#Directorio de funciones
dirFuncs = fileReader.dirFuncs
#Tabla de constantes
cteTable = fileReader.cteTable
#Cuadrulos
quad = fileReader.Quad

fileReader.readFile()
#Memoria Global
tam = dirFuncs[0].size
tam = (tam.split(','))
glob = memo.memoria(tam[0], tam[1], tam[2], 0)
globTemp = memo.memoria(tam[3], tam[4], tam[5], tam[6])
#Memoria Local
local = None
localTemp = None
local2 = None
localTemp2 = None
#Variables of function calls
numParams = None
funcParams = None
funcQuad = []
funcId = []
intP = 0
floatP = 0
charP = 0
returnQuad = []


#Regresa la constante
def findCte(dir):
    for i in range(len(cteTable)):
        if dir == int(cteTable[i].dir):
            if cteTable[i].type == 'int':
                return int(cteTable[i].id)
            elif cteTable[i].type == 'float':
                return float(cteTable[i].id)
            return cteTable[i].id

#Verifica si la memoria es un apuntador
def apuntador(dir):
    if dir[0] == '(':
        dir = dir.rstrip(')')
        dir = dir.lstrip('(')
        dir = int(dir)
        return memo.get(glob, globTemp, local, localTemp, dir)
    else:
        if dir == None:
            return dir
        else:
            return int(dir)

#Crea matriz
def createMat(dir):
    dir1 = int(dir[0])
    lim1 = findCte(int(dir[1])) + 1
    matrix = []
    if (len(dir) == 2):
        for c in range(lim1):
            space = dir1 + c
            matrix.append(memo.get(glob, globTemp, local, localTemp, space))
        return matrix
    else:
        lim2 = findCte(int(dir[2])) + 1
        for r in range(0,lim1):
            a = []
            for c in range(0,lim2):
                space = (r*lim1) + c + dir1
                val = memo.get(glob, globTemp, local, localTemp, space)
                a.append(val)
            matrix.append(a)
        return matrix

#Inserta resultados de operaciones de matrices a matriz correspondiente
def createMatRes(dir, res):
    dir1 = int(dir[0])
    lim1 = findCte(int(dir[1])) + 1
    if (len(dir) == 2):
        for c in range(lim1):
            space = dir1 + c
            memo.assign(glob, globTemp, local, localTemp, space, res[c])
    else:
        lim2 = findCte(int(dir[2])) + 1
        for r in range(lim1):
            for c in range(lim2):
                space = (r*lim1) + c + dir1
                memo.assign(glob, globTemp, local, localTemp, space, res[r][c])

#Funcion que identifica el tipo de la constante
def gettipo(cte):
    tipo = str(type(cte))
    temp = None
    if tipo == "<class 'float'>":
        temp = 2
        return temp
    elif tipo == "<class 'int'>":
        temp = 1
        return temp
    elif len(cte) == 1:
        temp = 3
        return temp
    elif tipo == "<class 'str'>":
        print('Error: Valor ingresado no valido')
        sys.exit()

#Funciones de cuadruplos
def goto(cuad, i):
    return int(cuad.result)

def sum(cuad, i):
    dir1 = (cuad.dir1.split('['))
    dir2 = (cuad.dir2.split('['))
    len1 = len(dir1)
    len2 = len(dir2)
    if (len1 < 2 and len2 < 2):
        dir1 = apuntador(cuad.dir1)
        dir2 = apuntador(cuad.dir2)
        result = apuntador(cuad.result)
        if dir1>=8000 and dir1<13000:
            left_op = findCte(dir1)
        else:
            left_op = memo.get(glob, globTemp, local, localTemp, dir1)
        if dir2>=8000 and dir2<13000:
            right_op = findCte(dir2)
        else:
            right_op = memo.get(glob, globTemp, local, localTemp, dir2)
        res = left_op + right_op
        memo.assign(glob, globTemp, local, localTemp, result, res)
        return i + 1
    else:
        result = (cuad.result.split('['))
        if (len1 < 2):
            dir1 = apuntador(cuad.dir1)
            if dir1>=8000 and dir1<13000:
                left_op = findCte(dir1)
            else:
                left_op = memo.get(glob, globTemp, local, localTemp, dir1)
            mat2 = createMat(dir2)
            res = np.add(left_op, mat2)
            createMatRes(result, res)
        elif (len2 < 2):
            mat1 = createMat(dir1)
            dir2 = apuntador(cuad.dir2)
            if dir2>=8000 and dir2<13000:
                right_op = findCte(dir2)
            else:
                right_op = memo.get(glob, globTemp, local, localTemp, dir2)
            res = np.add(mat1, right_op)
            createMatRes(result, res)
        else:
            mat1 = createMat(dir1)
            mat2 = createMat(dir2)
            res = np.add(mat1, mat2)
            createMatRes(result, res)
    return i + 1

def rest(cuad, i):
    dir1 = (cuad.dir1.split('['))
    dir2 = (cuad.dir2.split('['))
    len1 = len(dir1)
    len2 = len(dir2)
    if (len1 < 2 and len2 < 2):
        dir1 = apuntador(cuad.dir1)
        dir2 = apuntador(cuad.dir2)
        result = apuntador(cuad.result)
        if dir1>=8000 and dir1<13000:
            left_op = findCte(dir1)
        else:
            left_op = memo.get(glob, globTemp, local, localTemp, dir1)
        if dir2>=8000 and dir2<13000:
            right_op = findCte(dir2)
        else:
            right_op = memo.get(glob, globTemp, local, localTemp, dir2)
        res = left_op - right_op
        memo.assign(glob, globTemp, local, localTemp, result, res)
        return i + 1
    else:
        result = (cuad.result.split('['))
        if (len1 < 2):
            dir1 = apuntador(cuad.dir1)
            if dir1>=8000 and dir1<13000:
                left_op = findCte(dir1)
            else:
                left_op = memo.get(glob, globTemp, local, localTemp, dir1)
            mat2 = createMat(dir2)
            res = np.subtract(left_op, mat2)
            createMatRes(result, res)
        elif (len2 < 2):
            mat1 = createMat(dir1)
            dir2 = apuntador(cuad.dir2)
            if dir2>=8000 and dir2<13000:
                right_op = findCte(dir2)
            else:
                right_op = memo.get(glob, globTemp, local, localTemp, dir2)
            res = np.subtract(mat1, right_op)
            createMatRes(result, res)
        else:
            mat1 = createMat(dir1)
            mat2 = createMat(dir2)
            res = np.subtract(mat1, mat2)
            createMatRes(result, res)
    return i + 1

def div(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = apuntador(cuad.dir2)
    result = apuntador(cuad.result)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    res = left_op / right_op
    memo.assign(glob, globTemp, local, localTemp, result, res)
    return i + 1

def mult(cuad, i):
    dir1 = (cuad.dir1.split('['))
    dir2 = (cuad.dir2.split('['))
    len1 = len(dir1)
    len2 = len(dir2)
    if (len1 < 2 and len2 < 2):
        dir1 = apuntador(cuad.dir1)
        dir2 = apuntador(cuad.dir2)
        result = apuntador(cuad.result)
        if dir1>=8000 and dir1<13000:
            left_op = findCte(dir1)
        else:
            left_op = memo.get(glob, globTemp, local, localTemp, dir1)
        if dir2>=8000 and dir2<13000:
            right_op = findCte(dir2)
        else:
            right_op = memo.get(glob, globTemp, local, localTemp, dir2)
        res = left_op * right_op
        memo.assign(glob, globTemp, local, localTemp, result, res)
        return i + 1
    else:
        result = (cuad.result.split('['))
        if (len1 < 2):
            dir1 = apuntador(cuad.dir1)
            if dir1>=8000 and dir1<13000:
                left_op = findCte(dir1)
            else:
                left_op = memo.get(glob, globTemp, local, localTemp, dir1)
            mat2 = createMat(dir2)
            res = np.multiply(left_op, mat2)
            createMatRes(result, res)
        elif (len2 < 2):
            mat1 = createMat(dir1)
            dir2 = apuntador(cuad.dir2)
            if dir2>=8000 and dir2<13000:
                right_op = findCte(dir2)
            else:
                right_op = memo.get(glob, globTemp, local, localTemp, dir2)
            res = np.multiply(mat1, right_op)
            createMatRes(result, res)
        else:
            mat1 = createMat(dir1)
            mat2 = createMat(dir2)
            res = np.dot(mat1, mat2)
            if (str(res)[0] != '['):
                result = apuntador(cuad.result)
                memo.assign(glob, globTemp, local, localTemp, result, res)
            else:
                createMatRes(result, res)
    return i + 1
        
def greater(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = apuntador(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op > right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def lesser(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = apuntador(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op < right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def lesser_e(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = apuntador(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op <= right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def greater_e(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = apuntador(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op >= right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def equal(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = apuntador(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op == right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def different(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = apuntador(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op != right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def andOp(cuad, i):
    dir1 = int(cuad.dir1)
    dir2 = int(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op and right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def orOp(cuad, i):
    dir1 = int(cuad.dir1)
    dir2 = int(cuad.dir2)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        right_op = findCte(dir2)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir2)
    if (left_op or right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def gotofalse(cuad, i):
    dir1 = int(cuad.dir1)
    left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    if(left_op):
        return i + 1
    else:
        return int(cuad.result)

def lee(cuad, i):
    valor = input()
    try:
        valor = int(valor)
    except ValueError:
        try:
            valor = float(valor)
        except ValueError:
            pass
    tipo1 = gettipo(valor)
    result = apuntador(cuad.result)
    tipo2 = memo.indentifyType(result)
    if tipo1 != tipo2:
        print('Error: Valor ingresado no es valido')
        sys.exit()
    memo.assign(glob, globTemp, local, localTemp, result, valor)
    return i + 1

def escribe(cuad, i):
    dir1 = apuntador(cuad.result)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    print(left_op)
    return i + 1

def asigna(cuad, i):
    dir1 = (cuad.dir1.split('['))
    result = (cuad.result.split('['))
    len1 = len(dir1)
    len2 = len(result)
    if (len1 < 2 and len2 < 2):
        dir1 = apuntador(cuad.dir1)
        result = apuntador(cuad.result)
        if dir1>=8000 and dir1<13000:
            right_op = findCte(dir1)
        else:
            right_op = memo.get(glob, globTemp, local, localTemp, dir1)
        memo.assign(glob, globTemp, local, localTemp, result, right_op)
        return i + 1
    else:
        mat1 = createMat(dir1)
        createMatRes(result, mat1)
        return i + 1

def regresa(cuad, i):
    global local
    global localTemp
    dir1 = apuntador(cuad.result)
    reQuad = returnQuad.pop()
    dir = funcId.pop()
    if dir != None:
        dir = int(dir)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    memo.assign(glob, globTemp, local, localTemp, dir, left_op)
    local = memo.memStack.pop()
    localTemp = memo.memTStack.pop()
    return reQuad + 1

def gosub(cuad, i):
    global local
    global localTemp
    global local2
    global localTemp2
    global returnQuad
    gosu = funcQuad.pop()
    local = local2
    localTemp = localTemp2
    local2 = None
    localTemp2 = None
    returnQuad.append(i)
    return gosu
    
def era(cuad, i):
    global local2
    global localTemp2
    global funcParams
    global funcQuad
    global numParams
    func = cuad.result
    exist = 0
    if local2 != None:
        memo.memStack.append(local2)
        memo.memTStack.append(localTemp2)
        local2 = None
        localTemp2 = None
    else:
        memo.memStack.append(local)
        memo.memTStack.append(localTemp)
    for x in range(len(dirFuncs)):
        if func == dirFuncs[x].id:
            tam = dirFuncs[x].size
            tam = (tam.split(','))
            funcParams = dirFuncs[x].params
            #funcParams =(funcParams.split(','))
            numParams = len(funcParams)
            funcQuad.append(int(dirFuncs[x].quad))
            funcId.append(dirFuncs[x].dir)
            local2 = memo.memoria(tam[0], tam[1], tam[2], 0)
            localTemp2 = memo.memoria(tam[3], tam[4], tam[5], tam[6])
            exist = 1
    if exist == 0:
        print('Error: La funcion no existe')
        sys.exit()
    return i + 1

def param(cuad, i):
    global numParams
    global intP
    global floatP
    global charP
    dir1 = apuntador(cuad.dir1)
    space = int(cuad.result) - 1
    memT = memo.indentifyType(dir1)
    if numParams > 0:
        if funcParams[space] == 'i' and memT == 1:
            dir = 13000 + intP
            intP += 1
        elif funcParams[space] == 'f' and memT == 2:
            dir = 14000 + floatP
            floatP += 1
        elif funcParams[space] == 'c' and memT == 3:
            dir = 15000 + charP
            charP += 1
        else:
            print('Error: Parametros no compatibles')
            sys.exit()
        if dir1>=8000 and dir1<13000:
            left_op = findCte(dir1)
        else:
            left_op = memo.get(glob, globTemp, local, localTemp, dir1)
        memo.assign(glob, globTemp, local2, localTemp2, dir, left_op)
        numParams -= 1
        if numParams == 0:
            intP = 0
            floatP = 0
            charP = 0
        return i + 1
    else:
        print('Error: Se esperaban menos parametros')
        sys.exit()

def endfunc(cuad, i):
    global local
    global localTemp
    reQuad = returnQuad.pop()
    dir = funcId.pop()
    local = memo.memStack.pop()
    localTemp = memo.memTStack.pop()
    return reQuad + 1

def ver(cuad, i):
    dir1 = apuntador(cuad.dir1)
    dir2 = int(cuad.dir2)
    dir3 = int(cuad.result)
    if dir1>=8000 and dir1<13000:
        val = findCte(dir1)
    else:
        val = memo.get(glob, globTemp, local, localTemp, dir1)
    if dir2>=8000 and dir2<13000:
        lim_inf = findCte(dir2)
    else:
        lim_inf = memo.get(glob, globTemp, local, localTemp, dir2)
    if dir3>=8000 and dir3<13000:
        lim_sup = findCte(dir3)
    else:
        lim_sup = memo.get(glob, globTemp, local, localTemp, dir3)
    if val >= lim_inf and val <= lim_sup:
        return i + 1
    else:
        print('Error: Varibale dimensionada fuera de rango')

def deter(cuad, i):
    dir1 = (cuad.dir1.split('['))
    result = apuntador(cuad.result)
    mat1 = createMat(dir1)
    res = np.linalg.det(mat1)
    memo.assign(glob, globTemp, local, localTemp, result, res)
    return i + 1

def trans(cuad, i):
    dir1 = (cuad.dir1.split('['))
    result = (cuad.result.split('['))
    mat1 = createMat(dir1)
    res = np.transpose(mat1)
    createMatRes(result, res)
    return i + 1

def inver(cuad, i):
    dir1 = (cuad.dir1.split('['))
    result = (cuad.result.split('['))
    mat1 = createMat(dir1)
    res = np.linalg.inv(mat1)
    createMatRes(result, res)
    return i + 1

#Switch que selecciona que funcion ejecutar segun la accion de cuadruplo
def switch(cuadr, i):
    dict = {
        '+' : sum,
        '-' : rest,
        '/' : div,
        '*' : mult,
        '>' : greater,
        '<' : lesser,
        '<=' : lesser_e,
        '>=' : greater_e,
        '==' : equal,
        '!=' : different,
        '&&' : andOp,
        '||' : orOp,
        'GotoF' : gotofalse,
        'Goto' : goto,
        'lee' : lee,
        'escribe' : escribe,
        '=' : asigna,
        'regresa' : regresa,
        'Gosub' : gosub,
        'Era' : era,
        'Param' : param,
        'Endfunc' : endfunc,
        'Ver' : ver,
        '$' : deter,
        '¡' : trans,
        '?' : inver,
    }
    func = dict.get(cuadr.action, 'null')
    if func != 'null':
        position = func(cuadr, i)
        return position
    return i+1

i = 0
while quad[i].action != 'End':
    i = switch(quad[i], i)
#print("Dejó el programa.")
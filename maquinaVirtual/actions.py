# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

import sys
import memoria as memo
import fileReader

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
local = memo.memoria(0,0,0,0)
localTemp = memo.memoria(0,0,0,0)

def findCte(dir):
    for i in range(len(cteTable)):
        if dir == int(cteTable[i].dir):
            if cteTable[i].type == 'int':
                return int(cteTable[i].id)
            elif cteTable[i].type == 'float':
                return float(cteTable[i].id)
            return cteTable[i].id

def goto(cuad, i):
    return int(cuad.result)

def sum(cuad, i):
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
    #print(left_op,'+',right_op)
    res = left_op + right_op
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def rest(cuad, i):
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
    #print(left_op,'-',right_op)
    res = left_op - right_op
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def div(cuad, i):
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
    #print(left_op,'/',right_op)
    res = left_op / right_op
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def mult(cuad, i):
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
    #print(left_op,'*',right_op)
    res = left_op * right_op
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def greater(cuad, i):
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
    #print(left_op,'>',right_op)
    if (left_op > right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def lesser(cuad, i):
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
    #print(left_op,'<',right_op)
    if (left_op < right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def lesser_e(cuad, i):
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
    #print(left_op,'<=',right_op)
    if (left_op <= right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def greater_e(cuad, i):
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
    #print(left_op,'>=',right_op)
    if (left_op >= right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def equal(cuad, i):
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
    #print(left_op,'==',right_op)
    if (left_op == right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def different(cuad, i):
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
    #print(left_op,'!=',right_op)
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
    #print(left_op,'&&',right_op)
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
    #print(left_op,'||',right_op)
    if (left_op or right_op):
        res = True
    else:
        res = False
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), res)
    return i + 1

def gotofalse(cuad, i):
    dir1 = int(cuad.dir1)
    left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    #print('Gotof',left_op,' ',cuad.result)
    if(left_op):
        return i + 1
    else:
        return int(cuad.result)

def lee(cuad, i):
    valor = input()
    dir = int(cuad.result)
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), valor)
    return i + 1

def escribe(cuad, i):
    dir1 = int(cuad.result)
    if dir1>=8000 and dir1<13000:
        left_op = findCte(dir1)
    else:
        left_op = memo.get(glob, globTemp, local, localTemp, dir1)
    print(left_op)
    return i + 1

def asigna(cuad, i):
    dir1 = int(cuad.dir1)
    if dir1>=8000 and dir1<13000:
        right_op = findCte(dir1)
    else:
        right_op = memo.get(glob, globTemp, local, localTemp, dir1)
    #print(cuad.result,'=',right_op)
    memo.assign(glob, globTemp, local, localTemp, int(cuad.result), right_op)
    return i + 1

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
        #'regresa' : regresa,
        #'Gosub' : gosub,
        #'Era' : era,
        #'Param' : param,
        #'Endfunc' : endfunc,
        #'Ver' : ver,
    }
    func = dict.get(cuadr.action, 'null')
    if func != 'null':
        position = func(cuadr, i)
        return position
    return i+1

i = 0
while quad[i].action != 'End':
    i = switch(quad[i], i)
# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys
import estructuras as cuadruplo
import SemanticCube as semantic
import memoriaVirtual as mv
import tables as Tabla

#Stacks
Poper = []
Pjumps = []
Ptypes = []
PilaO = []
avail = []
Quad = []
desde = []

#Variables globales
count = 1
semantic_cube = semantic.SemanticCube().cube
param = 1

#Funcione que inserta un cuadruplo
def quadInsert(action, dir1, dir2, result):
    temp = cuadruplo.cuadruplo(count-1, action, dir1, dir2, result)
    Quad.append(temp)

#Funcion que agrega el cuadruplo donde empieza al funcion pricipla al Goto del inicio
def gotoMain():
    Quad[0].result = count-1

#Funcion que agrega memoria asociada de variable a la pila de operadores
def pushPilaO(id):
    PilaO.append(id)

#Funcion que agrega el tipo de variable a la pila de tipos
def pushType(type):
    Ptypes.append(type)

#Funcion que agrega la operacion a la pila de operaciones
def pushPoper(action):
    Poper.append(action)

#Funcion que agrega cuadruplos de lee y escribe
def popIO():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == 'escribe' or Poper[size-1] == 'lee':
            right_operand = PilaO.pop()
            Ptypes.pop()
            operator = Poper.pop()
            #result_type = semantic_cube[operator][left_type][right_type]
            temp = cuadruplo.cuadruplo(count-1, operator, None, None, right_operand)
            Quad.append(temp)
            return True
    return False

#Funcion que agrega cuadruplo de regresa
def popRet():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == 'regresa':
            right_operand = PilaO.pop()
            Ptypes.pop()
            operator = Poper.pop()
            #result_type = semantic_cube[operator][left_type][right_type]
            temp = cuadruplo.cuadruplo(count-1, operator, None, None, right_operand)
            Quad.append(temp)
            return True
    return False

#Funcion que agrega cuadruplo de =
def popAssign():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == '=':
            right_operand = PilaO.pop()
            right_operand = right_operand if right_operand == opMat(right_operand) else opMat(right_operand)
            right_type = Ptypes.pop()
            left_operand = PilaO.pop()
            left_operand = left_operand if left_operand == opMat(left_operand) else opMat(left_operand)
            left_type = Ptypes.pop()
            operator = Poper.pop()
            if(left_type == right_type and asignaCompMat(str(right_operand), str(left_operand))):
                #result = 't' + str(count)
                temp = cuadruplo.cuadruplo(count-1, operator, right_operand, None, left_operand)
                Quad.append(temp)
                PilaO.append(left_operand)
                Ptypes.append(left_type)
                return True
            else:
                print("ERROR: type mismatch")
                sys.exit()
                return False
    return False

#Funcion que agrega cuadruplos de and(&&) y or(||)
def popLog(glob):
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == '||' or Poper[size-1] == '&&':
            right_operand = PilaO.pop()
            right_type = Ptypes.pop()
            left_operand = PilaO.pop()
            left_type = Ptypes.pop()
            operator = Poper.pop()
            result_type = semantic_cube[operator][left_type][right_type]
            if(result_type != 'err'):
                result = mv.getMemoTemp(result_type, glob,1)
                if (glob):
                    Tabla.gtempAddSize(result_type,1)
                else:
                    Tabla.tempAddSize(result_type,1)
                temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                Quad.append(temp)
                PilaO.append(result)
                Ptypes.append(result_type)
                return True
            else:
                print("ERROR: type mismatch")
                sys.exit()
    return False

#Funcion que agrega cuadruplos de comparaciones
def popRel(glob):
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == '>' or Poper[size-1] == '<' or Poper[size-1] == '>=' or Poper[size-1] == '<=' or Poper[size-1] == '==' or Poper[size-1] == '!=':
            right_operand = PilaO.pop()
            right_type = Ptypes.pop()
            left_operand = PilaO.pop()
            left_type = Ptypes.pop()
            operator = Poper.pop()
            result_type = semantic_cube[operator][left_type][right_type]
            if(result_type != 'err'):
                result = mv.getMemoTemp(result_type, glob,1)
                if (glob):
                    Tabla.gtempAddSize(result_type,1)
                else:
                    Tabla.tempAddSize(result_type,1)
                temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                Quad.append(temp)
                PilaO.append(result)
                Ptypes.append(result_type)
                return True
            else:
                print("ERROR: type mismatch")
                sys.exit()
    return False

#Funcion que agrega cuadruplos de suma(+) y resta(-)
def popTerm(glob):
    size = len(Poper)
    if size > 0:
        if Poper[size-1] != '(':
            if Poper[size-1] == '+' or Poper[size-1] == '-':
                tempR = right_operand = PilaO.pop()
                right_operand = right_operand if right_operand == opMat(right_operand) else opMat(right_operand)
                right_type = Ptypes.pop()
                tempL = left_operand = PilaO.pop()
                left_operand = left_operand if left_operand == opMat(left_operand) else opMat(left_operand)
                left_type = Ptypes.pop()
                operator = Poper.pop()
                result_type = semantic_cube[operator][left_type][right_type]
                tam = compMatSize(right_operand, tempR, left_operand, tempL, operator)
                salto = tamMat(tam)
                if(result_type != 'err'):
                    result = mv.getMemoTemp(result_type, glob, salto)
                    if (salto > 1 and len(tam) == 1):
                        result = str(result) + '[' + tam[0]
                    elif(salto >1 and len(tam) == 2):
                        result = str(result) + '[' + tam[0] + '[' + tam[1]
                    if (glob):
                        Tabla.gtempAddSize(result_type,salto)
                    else:
                        Tabla.tempAddSize(result_type,salto)
                    temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                    Quad.append(temp)
                    PilaO.append(result)
                    Ptypes.append(result_type)
                    return True
                else:
                    print("Error: type mismatch")
                    sys.exit()
    return False

#Funcion que agrega cuadruplos de multiplicacion(*) y division(/)
def popFact(glob):
    size = len(Poper)
    if size > 0:
        if Poper[size-1] != '(':
            if Poper[size-1] == '*' or Poper[size-1] == '/':
                tempR = right_operand = PilaO.pop()
                right_operand = right_operand if right_operand == opMat(right_operand) else opMat(right_operand)
                right_type = Ptypes.pop()
                tempL = left_operand = PilaO.pop()
                left_operand = left_operand if left_operand == opMat(left_operand) else opMat(left_operand)
                left_type = Ptypes.pop()
                operator = Poper.pop()
                result_type = semantic_cube[operator][left_type][right_type]
                tam = compMatSize(right_operand, tempR, left_operand, tempL, operator)
                salto = tamMat(tam)
                if(result_type != 'err'):
                    result = mv.getMemoTemp(result_type, glob, salto)
                    if (salto > 1 and len(tam) == 1):
                        result = str(result) + '[' + tam[0]
                    elif(salto >1 and len(tam) == 2):
                        result = str(result) + '[' + tam[0] + '[' + tam[1]
                    if (glob):
                        Tabla.gtempAddSize(result_type,salto)
                    else:
                        Tabla.tempAddSize(result_type,salto)
                    temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                    Quad.append(temp)
                    PilaO.append(result)
                    Ptypes.append(result_type)
                    return True
                else:
                    print("ERROR: type mismatch")
                    sys.exit()
    return False

#Funcion que agrega cuadruplo de funciones especiales de matrices
def popMat(glob):
    size = len(Poper)
    if size > 0:
        if Poper[size-1] != '(':
            if Poper[size-1] == '$' or Poper[size-1] == '¡' or Poper[size-1] == '?':
                temp = operand = PilaO.pop()
                operand = operand if operand == opMat(operand) else opMat(operand)
                o_type = Ptypes.pop()
                operator = Poper.pop()
                if operator == '¡':
                    result_type = o_type
                elif operator == '$':
                    if (o_type == 'char'):
                        print('Error: No se puede el determinante de una matriz de chars')
                        sys.exit()
                    else:
                        result_type = o_type
                else:
                    result_type = semantic_cube['/'][o_type]['float']
                tam = compMatSize(operand, temp, operand, temp, operator)
                if tam == 0:
                    print('Error: Esta es una funcion especial para solo matrices')
                    sys.exit()
                elif tam == 1:
                    salto = 1
                else:
                    salto = tamMat(tam)
                if(result_type != 'err'):
                    result = mv.getMemoTemp(result_type, glob, salto)
                    if (salto > 1 and len(tam) == 1):
                        result = str(result) + '[' + tam[0]
                    elif(salto > 1 and len(tam) == 2):
                        result = str(result) + '[' + tam[0] + '[' + tam[1]
                    if (glob):
                        Tabla.gtempAddSize(result_type,salto)
                    else:
                        Tabla.tempAddSize(result_type,salto)
                    temp = cuadruplo.cuadruplo(count-1, operator, operand, None, result)
                    Quad.append(temp)
                    PilaO.append(result)
                    Ptypes.append(result_type)
                    return True
                else:
                    print('Error: type mismatch')
                    sys.exit()
    return False

#Funcion que identifica el tipo de la constante
def gettipo(cte):
    tipo = str(type(cte))
    temp = None
    if cte == 'true' or cte == 'false':
        temp = 'boolean'
        return temp
    if tipo == "<class 'float'>":
        temp = 'float'
        return temp
    if tipo == "<class 'int'>":
        temp = 'int'
        return temp
    if tipo == "<class 'str'>":
        temp = 'string'
        return temp
    if tipo == "<class 'char'>":
        temp = 'char'
        return temp

#Funcion que imprime los cuadruplos generados
def imprime():
    for i in range(0, len(Quad)):
        print(Quad[i].count, Quad[i].action, Quad[i].dir1, Quad[i].dir2, Quad[i].result)

#Funcion que quita el fondo falso de la pila de operaciones
def popFalseBottom():
    Poper.pop()

#Punto neural 1 de si
def GotoF_SI():
    exp_type = Ptypes.pop()
    if (exp_type != 'boolean'):
        print('Error: type mismatch')
        sys.exit()
        return False
    else:
        result = PilaO.pop()
        temp = cuadruplo.cuadruplo(count-1, 'GotoF', result, None, None)
        Quad.append(temp)
        Pjumps.append(count-1)
        return True

#Punto neural 2 de si
def fillGoto():
    end = Pjumps.pop()
    Quad[end].result = count-1

#Punto neural 1 de sino
def Goto_SI():
    temp = cuadruplo.cuadruplo(count-1, 'Goto', None, None, None)
    Quad.append(temp)
    false = Pjumps.pop()
    Pjumps.append(count-1)
    Quad[false].result = count
    return True

#Punto neural 1 de mientras
def pushJumps():
    Pjumps.append(count-1)

#Punto neural 2 de mientras
def GotoF_While():
    exp_type = Ptypes.pop()
    if (exp_type != 'boolean'):
        print('Error: type mismatch')
        sys.exit()
        return False
    else:
        result = PilaO.pop()
        temp = cuadruplo.cuadruplo(count-1, 'GotoF', result, None, None)
        Quad.append(temp)
        Pjumps.append(count-1)
        return True

#Punto neural 3 de mientras
def Goto_While():
    end = Pjumps.pop()
    retur = Pjumps.pop()
    temp = cuadruplo.cuadruplo(count-1, 'Goto', None, None, retur)
    Quad.append(temp)
    Quad[end].result = count
    return True

#Punto neural 1 de desde es igual al punto neural 1 de mientras

#Punto neural 2 de desde
def compareFor(glob):
    right_operand = PilaO.pop()
    right_type = Ptypes.pop()
    left_operand = PilaO.pop()
    left_type = Ptypes.pop()
    result_type = semantic_cube['<='][left_type][right_type]
    if(result_type != 'err'):
        desde.append(left_operand)
        result = mv.getMemoTemp(result_type, glob,1)
        if (glob):
            Tabla.gtempAddSize(result_type,1)
        else:
            Tabla.tempAddSize(result_type,1)
        temp = cuadruplo.cuadruplo(count-1, '<=', left_operand, right_operand, result)
        Quad.append(temp)
        PilaO.append(result)
        Ptypes.append(result_type)
        return True
    else:
        print("ERROR: type mismatch")
        sys.exit()
    return False

#Punto neural 3 de desde es igual al punto neural 2 de mientras

#Punto neural 4 de desde
def addToFor(glob):
    result_type = 'int'
    result = mv.getMemoTemp(result_type, glob,1)
    if (glob):
        Tabla.gtempAddSize(result_type,1)
    else:
        Tabla.tempAddSize(result_type,1)
    left_operand = desde.pop()
    dir = mv.getMemoCte('int')
    temp = Tabla.cteInsert(1, 'int', dir)
    if (temp == False):
        mv.restMemo('int')
    right_operand = Tabla.findCteVM(1)
    temp = cuadruplo.cuadruplo(count-1, '+', left_operand, right_operand, result)
    desde.append(left_operand)
    desde.append(result)
    Quad.append(temp)
    return True

#Punto neural 5 de desde
def assignToFor():
    right_operand = desde.pop()
    left_operand = desde.pop()
    temp = cuadruplo.cuadruplo(count-1, '=', right_operand, None, left_operand)
    Quad.append(temp)
    return True

#Punto neural 6 de desde es igual al punto neural 3 de mientras

#Funcion que agrega el cuadruplo de Param
def paramInsert():
    params = PilaO.pop()
    tipo = Ptypes.pop()
    num = param
    temp = cuadruplo.cuadruplo(count-1, 'Param', params, None, num)
    Quad.append(temp)

#Funcion que agrega el cuadruplo de Gosub
def gosub(func):
    temp = cuadruplo.cuadruplo(count-1, 'Gosub', None, None, func)
    Quad.append(temp)

#Funcion que asigna el valor de retorno de una funcion a una variable local
def parcheguad(func, glob):
    gvarTable = Tabla.gvarTable
    for ids in gvarTable:
        if ids == func:    
            dir = gvarTable[func].dir
            tipo = gvarTable[func].type
            if (dir == None):
                return False
            else:
                result = mv.getMemoTemp(tipo, glob,1)
                if (glob):
                    Tabla.gtempAddSize(tipo,1)
                else:
                    Tabla.tempAddSize(tipo,1)
                temp = cuadruplo.cuadruplo(count-1, '=', dir, None, result)
                Quad.append(temp)
                PilaO.append(result)
                Ptypes.append(tipo)
            return True

#Funcione que verifica que las operaciones de matrices
def opMat(dir):
    dir1 = dir
    if dir1 in Tabla.vectLTable:
        vect = Tabla.vectLTable[dir1]
        if vect.lim2 == None:
            dir1 = str(dir1) + '[' + str(vect.lim1)
        else:
            dir1 = str(dir1) + '[' + str(vect.lim1) + '[' + str(vect.lim2)
    elif dir1 in Tabla.vectGTable:
        vect = Tabla.vectGTable[dir1]
        if vect.lim2 == None:
            dir1 = str(dir1) + '[' + str(vect.lim1)
        else:
            dir1 = str(dir1) + '[' + str(vect.lim1) + '[' + str(vect.lim2)
    return dir1

#Verifica las operaciones entre matrices y regresa el tamaño del resultado esperado
def compMatSize(rO,rT,lO,lT,op):
    if (rT != rO and lT != lO):
        sR = (rO.split('['))
        sL = (lO.split('['))
        if (len(sR) != len(sL)):
            print('Error: Matrices de diferentes dimensiones')
            sys.exit()
        elif op == '$':
            return 1
        elif op == '¡':
            return [sR[2], sR[1]]
        elif op == '?':
            return [sR[1], sR[2]]
        elif (op == '+' or op == '-'):
            if (len(sR) == 2):
                if(sR[1] != sL[1]):
                    print('Error: Matrices de diferentes tamaños.')
                    sys.exit()
                else:
                    return [sR[1]]
            else:
                if(sR[1] != sL[1] or sR[2] != sL[2]):
                    print('Error: Matrices de diferentes tamaños.')
                    sys.exit()
                else:
                    return [sR[1], sR[2]]
        elif (op == '*'):
            if (len(sR) == 2):
                print('Error: No se puede multiplicar esta matriz.')
            else:
                if(sL[2] != sR[1]):
                    print('Error: No se puede multiplicar esta matriz.')
                    sys.exit()
                else:
                    return [sL[1], sR[2]]
    elif (rT != rO):
        sR = (rO.split('['))
        if (len(sR) == 2):
            return [sR[1]]
        else:
            return[sR[1], sR[2]]
    elif (lT != lO):
        sL = (lO.split('['))
        if (len(sL) == 2):
            return [sL[1]]
        else:
            return[sL[1], sL[2]]
    else:
        return 0

#Calcula el tamaño de matrices resultante
def tamMat(tam):
    if (tam == 0):
        return 1
    elif (len(tam) == 1):
        tam = int(tam[0])
        tam = findCte(tam) + 1
        return tam
    else:
        tam1 = int(tam[0])
        tam2 = int(tam[1])
        tam1 = findCte(tam1)
        tam2 = findCte(tam2)
        return (tam1+1)*(tam2+1)

#Regresa la constante
def findCte(dir):
    cteTable = Tabla.cteTable
    for i in range(len(cteTable)):
        if dir == int(cteTable[i].dir):
            if cteTable[i].type == 'int':
                return int(cteTable[i].id)
            elif cteTable[i].type == 'float':
                return float(cteTable[i].id)
            return cteTable[i].id

#Verifica que la asigancion sea entre variables de mismas dimensiones y tamaños
def asignaCompMat(rO, lO):
    sR = (rO.split('['))
    sL = (lO.split('['))
    if (len(sR) != len(sL)):
        print('Error: Matrices de diferentes dimensiones')
        sys.exit()
    elif (len(sR) == 2):
        if (sR[1] != sL[1]):
            print('Error: Matrices de diferentes tamaños')
            sys.exit()
        else:
            return True
    elif (len(sR) == 3):
        if (sR[1] != sL[1] or sR[2] != sL[2]):
            print('Error: Matrices de diferentes tamaños')
            sys.exit()
        else:
            return True
    elif (len(sR) == 1):
        return True
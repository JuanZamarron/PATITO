# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys
import estructuras as cuadruplo
import SemanticCube as semantic

#Stacks
Poper = []
Pjumps = []
Ptypes = []
PilaO = []
avail = []
Quad = []

#Variables globales
count = 1
semantic_cube = semantic.SemanticCube().cube

#Func that defines which insert use
def quadInsert(action, dir1, dir2, result):
    temp = cuadruplo.cuadruplo(count-1, action, dir1, dir2, result)
    Quad.append(temp)

def pushPilaO(id):
    PilaO.append(id)

def pushType(type):
    Ptypes.append(type)

def pushPoper(action):
    Poper.append(action)

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

def popAssign():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == '=':
            right_operand = PilaO.pop()
            right_type = Ptypes.pop()
            left_operand = PilaO.pop()
            left_type = Ptypes.pop()
            operator = Poper.pop()
            #result_type = semantic_cube[operator][left_type][right_type]
            if(left_type == right_type):
                #result = 't' + str(count)
                temp = cuadruplo.cuadruplo(count-1, operator, right_operand, None, left_operand)
                Quad.append(temp)
                #PilaO.append(result)
                #Ptypes.append(left_type)
                return True
            else:
                print("ERROR: type mismatch")
    return False

def popLog():
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
                result = 't' + str(count)
                temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                Quad.append(temp)
                PilaO.append(result)
                Ptypes.append(result_type)
                return True
            else:
                print("ERROR: type mismatch")
    return False

def popRel():
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
                result = 't' + str(count)
                temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                Quad.append(temp)
                PilaO.append(result)
                Ptypes.append(result_type)
                return True
            else:
                print("ERROR: type mismatch")
    return False

def popTerm():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] != '(':
            if Poper[size-1] == '+' or Poper[size-1] == '-':
                right_operand = PilaO.pop()
                right_type = Ptypes.pop()
                left_operand = PilaO.pop()
                left_type = Ptypes.pop()
                operator = Poper.pop()
                result_type = semantic_cube[operator][left_type][right_type]
                if(result_type != 'err'):
                    result = 't' + str(count)
                    temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                    Quad.append(temp)
                    PilaO.append(result)
                    Ptypes.append(result_type)
                    return True
                else:
                    print("ERROR: type mismatch")
    return False

def popFact():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] != '(':
            if Poper[size-1] == '*' or Poper[size-1] == '/':
                right_operand = PilaO.pop()
                right_type = Ptypes.pop()
                left_operand = PilaO.pop()
                left_type = Ptypes.pop()
                operator = Poper.pop()
                result_type = semantic_cube[operator][left_type][right_type]
                if(result_type != 'err'):
                    result = 't' + str(count)
                    temp = cuadruplo.cuadruplo(count-1, operator, left_operand, right_operand, result)
                    Quad.append(temp)
                    PilaO.append(result)
                    Ptypes.append(result_type)
                    return True
                else:
                    print("ERROR: type mismatch")
    return False

def gettipo(cte):
    tipo = str(type(cte))
    temp = None
    if cte == 'true' or cte == 'false':
        temp = 'bool'
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

def imprime():
    for i in range(0, len(Quad)):
        print(Quad[i].count, Quad[i].action, Quad[i].dir1, Quad[i].dir2, Quad[i].result)

def popFalseBottom():
    Poper.pop()

#Neural point 1 of if
def GotoF_SI():
    exp_type = Ptypes.pop()
    if (exp_type != 'boolean'):
        print('Error: type mismatch')
        return False
    else:
        result = PilaO.pop()
        temp = cuadruplo.cuadruplo(count-1, 'GotoF', result, None, None)
        Quad.append(temp)
        Pjumps.append(count-1)
        return True

#Neural point 2 of if
def fillGoto():
    end = Pjumps.pop()
    Quad[end].result = count-1

#Nueral point 3 of if-else
def Goto_SI():
    temp = cuadruplo.cuadruplo(count-1, 'Goto', None, None, None)
    Quad.append(temp)
    false = Pjumps.pop()
    Pjumps.append(count-1)
    Quad[false].result = count
    return True

#Neural point 1 of while
def pushJumps():
    Pjumps.append(count-1)

#Nueral point 2 of while
def GotoF_While():
    exp_type = Ptypes.pop()
    if (exp_type != 'boolean'):
        print('Error: type mismatch')
        return False
    else:
        result = PilaO.pop()
        temp = cuadruplo.cuadruplo(count-1, 'GotoF', result, None, None)
        Quad.append(temp)
        Pjumps.append(count-1)
        return True

#Nueral point 3 of while
def Goto_While():
    end = Pjumps.pop()
    retur = Pjumps.pop()
    temp = cuadruplo.cuadruplo(count-1, 'Goto', None, None, retur)
    Quad.append(temp)
    Quad[end].result = count
    return True
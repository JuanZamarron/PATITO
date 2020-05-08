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
    temp = cuadruplo.cuadruplo(action, dir1, dir2, result)
    Quad.append(temp)
    count = count + 1

def pushPilaO(id):
    PilaO.append(id)

def pushType(type):
    Ptypes.append(type)

def pushPoper(action):
    Poper.append(action)

def popTerm():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == '+' or Poper[size-1] == '-':
            right_operand = PilaO.pop()
            right_type = Ptypes.pop()
            left_operand = PilaO.pop()
            left_type = Ptypes.pop()
            operator = Poper.pop()
            result_type = semantic_cube[operator][left_type][right_type]
            if(result_type != 'err'):
                result = 'temp'
                temp = cuadruplo.cuadruplo(operator, left_operand, right_operand, result)
                Quad.append(temp)
                PilaO.append(result)
                Ptypes.append(result_type)
            else:
                print("ERROR: type mismatch")

def popFact():
    size = len(Poper)
    if size > 0:
        if Poper[size-1] == '*' or Poper[size-1] == '/':
            right_operand = PilaO.pop()
            right_type = Ptypes.pop()
            left_operand = PilaO.pop()
            left_type = Ptypes.pop()
            operator = Poper.pop()
            result_type = semantic_cube[operator][left_type][right_type]
            if(result_type != 'err'):
                result = 'temp'
                temp = cuadruplo.cuadruplo(operator, left_operand, right_operand, result)
                Quad.append(temp)
                PilaO.append(result)
                Ptypes.append(result_type)
            else:
                print("ERROR: type mismatch")

def gettipo(cte):
    tipo = str(type(cte))
    temp = None
    if cte == 'true' or cte == 'false':
        tipo = 'bool'
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
        print(Quad[i].action, Quad[i].dir1, Quad[i].dir2, Quad[i].result)
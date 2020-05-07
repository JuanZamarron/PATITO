# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys
import estructuras as cuadruplo

#Stacks
Poper = []
Pjumps = []
Ptypes = []
PilaO = []
avail = []
Quad = []

#Variables globales
count = 1

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
    if Poper[size-1] == '+' or Poper[size-1] == '-':
        right_operand = PilaO.pop()
        right_type = Ptypes.pop()
        left_operand = PilaO.pop()
        left_type = Ptypes.pop()
        operator = Poper.pop()




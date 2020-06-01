# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

#Direcciones Globales
gI = 1000
gF = 2000
gC = 3000

#Temporales Globales
gtI = 4000
gtF = 5000
gtC = 6000
gtB = 7000

#Direcciones Locales
lI = 13000
lF = 14000
lC = 15000

#Temporales Locales
ltI = 16000
ltF = 17000
ltC = 18000
ltB = 19000

#Stack de memoria
memStack = []
memTStack = []

class memoria(object):
    def __init__(self, integ, float, char, boolean):
        self.integers = []
        self.float = []
        self.char = []
        self.boolean = []
        for i in range(int(integ)):
            self.integers.append(None)
        for i in range(int(float)):
            self.float.append(None)
        for i in range(int(char)):
            self.char.append(None)
        for i in range(int(boolean)):
            self.boolean.append(None)
    
    def start(self, integ, float, char, boolean):
        for i in range(int(integ)):
            self.integers.append(None)
        for i in range(int(float)):
            self.float.append(None)
        for i in range(int(char)):
            self.char.append(None)
        for i in range(int(boolean)):
            self.boolean.append(None)


#Ingresa valor al espacio de memoria
def assign(mem1, mem2, mem3, mem4, dir, val):
    space = dir%1000
    mem = indentifyMem(dir)
    tipo = indentifyType(dir)
    if mem == 1:
        assignaux(mem1, space, tipo, val)
    elif mem == 2:
        assignaux(mem2, space, tipo, val)
    elif mem == 3:
        assignaux(mem3, space, tipo, val)
    else:
        assignaux(mem4, space, tipo, val)

def assignaux(mem,space,tipo,val):
    if tipo == 1:
        mem.integers[space] = val
    elif tipo == 2:
        mem.float[space] = val
    elif tipo == 3:
        mem.char[space] = val
    else:
        mem.boolean[space] = val

#Idetifica que memoria es
def indentifyMem(dir):
    if dir<gtI:
        return 1
    elif dir<lI:
        return 2
    elif dir<ltI:
        return 3
    else:
        return 4

#Identifica que tipo de dato es
def indentifyType(dir):
    if dir>=lI:
        dir = dir//1000-12
    else:
        dir = dir//1000
    if dir>=4:
        return dir-3
    else:
        return dir

#Consigue valor del espacio de memoria
def get(mem1, mem2, mem3, mem4, dir):
    space = dir%1000
    mem = indentifyMem(dir)
    tipo = indentifyType(dir)
    if mem == 1:
        return getaux(mem1, space, tipo)
    elif mem == 2:
        return getaux(mem2, space, tipo)
    elif mem == 3:
        return getaux(mem3, space, tipo)
    else:
        return getaux(mem4, space, tipo)

def getaux(mem,space,tipo):
    if tipo == 1:
        return int(mem.integers[space])
    elif tipo == 2:
        return float(mem.float[space])
    elif tipo == 3:
        return mem.char[space]
    else:
        return mem.boolean[space]
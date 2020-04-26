# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys

funciones = [] # Tabla de funciones

#constructor
#add
#idexist
#update

class VarGeneral: #Ojeto par almacenar una variable
    def __init__(self, tipo, id, scope):
        self.tipo = tipo
        self.id = id
        self.scope = scope


class FunGeneral:#Almacena funciones
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id


class TabVarG(): #Tabla de funciones
    def __init__(self):
        self.tabVG = []

    def add(self, VarGeneral):
        if not self.searchVarG(VarGeneral.id):
            self.tabVG.append(VarGeneral)

    def searchVarG(self, id):
        if id in self.tabVG:
            return True
        return False

    def printVars(self):
        for i in self.tabVG:
            print (i.tipo)


class TabFun(): #Directorio de funciones
    def __init__(self):
        self.tab_fun = []

    def add(self, FunGeneral):
        if not self.searchVarG(FunGeneral.id):
            self.tab_fun.append(FunGeneral)

    def searchVarG(self, id):
        if id in self.tab_fun:
            return True
        return False

x = VarGeneral('int', 'a', 'global')
y = VarGeneral('char', 'v', 'local')

a = FunGeneral('void', 'MarcaBien')

tablaGen = TabVarG()
tablaGen.add(x)
tablaGen.add(y)

x1 = TabFun()
x1.add(a)

tablaGen.printVars()
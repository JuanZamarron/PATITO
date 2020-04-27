# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import sys

listaNombresVar = []#Contiene los id de todas los nombres de variables
# Objeto Tabla
class Tabla(object):
#id -> nombre de la variable/funcion única
#tipoDato -> Data Type (Int, float, String ... etc)
#valor -> Lo que contiene la variable

    def __init__(self, id, tipoDato, valor):
        self.id = str(id)
        self.tipoDato = str(tipoDato)
        self.valor = valor

    def existe(self,id):
        aux = False
        for i in range(0, len(listaNombresVar)):
            if listaNombresVar[i].id == id:
                aux = True
                print("ERROR: ID ya definido: ", id)
                sys.exit()
        return aux

    # Funciones para modificar la Tabla
    def agrega(self, id, tipoDato):
        temp = Tabla(id, tipoDato, None)
        if len(listaNombresVar) >= 1 and not self.existe(id):
            listaNombresVar.append(temp)
        if len(listaNombresVar) == 0:
            listaNombresVar.append(temp)

    def actualizar(self,id, valor):
        if validar(valor, id):
            for i in range(0, len(listaNombresVar)):
                if listaNombresVar[i].id == id:
                    listaNombresVar[i].valor = valor

    def validar(self,dato, id):
        temp = str(type(dato))
        longitud = len(listaNombresVar)
        aux = None
        encontro = False
        for i in range(0, longitud):
            if listaNombresVar[i].id == id:
                aux = listaNombresVar[i].tipoDato
                encontro = True
        if not encontro:
            print('ERROR: ID no declarado:', id)
            sys.exit()
        if temp == "<class 'float'>" and aux == 'float':
            return True
        if temp == "<class 'int'>" and aux == 'int':
            return True
        if temp == "<class 'str'>" and aux == 'string':
            return True
        else:
            print("ERROR: Dato no válido.")
            sys.exit()

    def imprimir(self):
        longitud = len(listaNombresVar)
        i = 0
        for i in range(0, longitud):
            print(listaNombresVar[i].id, listaNombresVar[i].tipoDato, listaNombresVar[i].valor, sep=', ')
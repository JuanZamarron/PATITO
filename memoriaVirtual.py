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
#Constantes Globales
gcI = 8000
gcF = 9000
gcC = 10000
gcS = 11000
gcB = 12000

#Direcciones Locales
lI = 13000
lF = 14000
lC = 15000
#Temporales Locales
tlI = 16000
tlF = 17000
tlC = 18000
tlB = 19000
#Constantes Locales
clI = 20000
clF = 21000
clC = 22000
clS = 23000
clB = 24000

def getMemoGlob(cte):
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
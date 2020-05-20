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
#Constantes
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

def getMemoGlob(tipo):
    global gI
    global gF
    global gC
    if tipo == "float":
        temp = gF
        gF += 1
        return temp
    if tipo == "int":
        temp = gI
        gI +=1
        return temp
    if tipo == "char":
        temp = gC
        gC += 1
        return temp

def getMemoLoc(tipo):
    global lI
    global lF
    global lC
    if tipo == "float":
        temp = lF
        lF += 1
        return temp
    if tipo == "int":
        temp = lI
        lI += 1
        return temp
    if tipo == "char":
        temp = lC
        lC += 1
        return temp

def getMemoCte(tipo):
    global gcI
    global gcF
    global gcC
    global gcS
    global gcB
    if tipo == "float":
        temp = gcF
        gcF += 1
        return temp
    if tipo == "int":
        temp = gcI
        gcI += 1
        return temp
    if tipo == "char":
        temp = gcC
        gcC += 1
        return temp
    if tipo == "boolean":
        temp = gcB
        gcB += 1
        return temp
    if tipo == "string":
        temp = gcS
        gcS += 1
        return temp

def restMemo(tipo):
    global gcI
    global gcF
    global gcC
    global gcS
    global gcB
    if tipo == "float":
        gcF -= 1
    if tipo == "int":
        gcI -= 1
    if tipo == "char":
        gcC -= 1
    if tipo == "boolean":
        gcB -= 1
    if tipo == "string":
        gcS -= 1
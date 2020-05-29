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
ltI = 16000
ltF = 17000
ltC = 18000
ltB = 19000

#Funcione que regresa el siguiente espacio de memoria global disponible
def getMemoGlob(tipo, salto):
    global gI
    global gF
    global gC
    if tipo == "float":
        temp = gF
        gF += salto
        return temp
    if tipo == "int":
        temp = gI
        gI += salto
        return temp
    if tipo == "char":
        temp = gC
        gC += salto
        return temp

#Funcione que regresa el siguiente espacio de memoria lcoal disponible
def getMemoLoc(tipo, salto):
    global lI
    global lF
    global lC
    if tipo == "float":
        temp = lF
        lF += salto
        return temp
    if tipo == "int":
        temp = lI
        lI += salto
        return temp
    if tipo == "char":
        temp = lC
        lC += salto
        return temp

#Funcione que regresa el siguiente espacio de memoria de constantes disponible
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

#Funcion que resta 1 del contador de memoria de constantes correspondiente
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

#Funcion que regresa el siguiente espacio de memoria temporal dependiendo si es global o local
def getMemoTemp(tipo, glob):
    global gtI
    global gtF
    global gtC
    global gtB
    global ltI
    global ltF
    global ltC
    global ltB
    if glob == True:
        if tipo == "float":
            temp = gtF
            gtF += 1
            return temp
        if tipo == "int":
            temp = gtI
            gtI += 1
            return temp
        if tipo == "char":
            temp = gtC
            gtC += 1
            return temp
        if tipo == "boolean":
            temp = gtB
            gtB += 1
            return temp
    else:
        if tipo == "float":
            temp = ltF
            ltF += 1
            return temp
        if tipo == "int":
            temp = ltI
            ltI += 1
            return temp
        if tipo == "char":
            temp = ltC
            ltC += 1
            return temp
        if tipo == "boolean":
            temp = ltB
            ltB += 1
            return temp
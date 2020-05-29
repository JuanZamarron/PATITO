# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

#Estructura para directorio de funciones y tabla de variables
class table(object):
    def __init__(self, id, type, dir, params, size, quad):
        self.id = id
        self.type = type
        self.dir = dir
        self.params = params
        self.size = size
        self.quad = quad

#Estructura de cuadruplos
class cuadruplo(object):
    def __init__(self, count, action, dir1, dir2, result):
        self.count = count
        self.action = action
        self.dir1 = dir1
        self.dir2 = dir2
        self.result = result

#Estructura de tabla de variables dimensionadas
class vector(object):
    def __init__(self, id, lim1, lim2, m, size):
        self.id = id
        self.lim1 = lim1
        self.lim2 = lim2
        self.m = m
        self.size = size
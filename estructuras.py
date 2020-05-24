# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

# Estructura para dirFunc y varsTable
class table(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type


class cuadruplo(object):
    def __init__(self, count, action, dir1, dir2, result):
        self.count = count
        self.action = action
        self.dir1 = dir1
        self.dir2 = dir2
        self.result = result

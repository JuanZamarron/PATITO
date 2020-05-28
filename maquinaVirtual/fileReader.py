# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

dirFuncs = []
cteTable = []
Quad = []

class dir(object):
    def __init__(self, id, type, dir, params, size, quad):
        self.id = id
        self.type = type
        self.dir = dir
        self.params = params
        self.size = size
        self.quad = quad

class const(object):
    def __init__(self, id, type, dir):
        self.id = id
        self.type = type
        self.dir = dir

class cuadruplo(object):
    def __init__(self, count, action, dir1, dir2, result):
        self.count = count
        self.action = action
        self.dir1 = dir1
        self.dir2 = dir2
        self.result = result

def readFile():
    table = 1
    filename = 'compiled.txt'
    file = open('compiledCode/'+filename, 'r')
    compiled = file.readlines()
    leng = len(compiled)
    for i in range(leng):
        line = compiled[i].rstrip('\n')
        if line[0] == '/':
            table += 1
        else: 
            if table == 1 :
                func = (line.split('Ç'))
                temp = dir(func[0], func[1], func[2], func[3], func[4], func[5])
                dirFuncs.append(temp)
            elif table == 2:
                func = (line.split('Ç'))
                temp = const(func[0], func[1], func[2])
                cteTable.append(temp)
            elif table == 3:
                func = (line.split('Ç'))
                temp = cuadruplo(func[0], func[1], func[2], func[3], func[4])
                Quad.append(temp)
    file.close
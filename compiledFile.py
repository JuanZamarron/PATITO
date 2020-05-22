# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------


def export_txt(dirFunc, cte, Quad):
        filename = 'compiled.txt'
        leng = len(cte)
        file = open(filename, 'w')
        for ids in dirFunc:
            line = str(ids) + '|', str(dirFunc[ids].type) + '|', str(dirFunc[ids].params) + '|', str(dirFunc[ids].size) + '|', str(dirFunc[ids].quad) + '\n'
            file.writelines(line)
        file.write('/\n')
        for i in range(leng):
            line = str(cte[i].id) + '|', str(cte[i].type) + '|', str(cte[i].dir) + '\n'
            file.writelines(line)
        file.write('/\n')
        for i in range(0, len(Quad)):
            line = str(Quad[i].count) + '|', str(Quad[i].action) + '|', str(Quad[i].dir1) + '|', str(Quad[i].dir2) + '|', str(Quad[i].result) +'\n'
            file.writelines(line)
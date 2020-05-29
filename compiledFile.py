# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

from lex import archivo


def export_txt(dirFunc, cte, Quad):
    print(archivo)
    leng = len(cte)
    file = open('compiledCode/' + archivo, 'w')
    for ids in dirFunc:
        line = str(ids) + 'Ç', str(dirFunc[ids].type)+ 'Ç',str(dirFunc[ids].dir)  + 'Ç',str(dirFunc[ids].params) + 'Ç', str(
            dirFunc[ids].size) + 'Ç', str(dirFunc[ids].quad) + '\n'
        file.writelines(line)
    file.write('/\n')
    for i in range(leng):
        line = str(cte[i].id) + 'Ç', str(cte[i].type) + 'Ç', str(cte[i].dir) + '\n'
        file.writelines(line)
    file.write('/\n')
    for i in range(0, len(Quad)):
        line = str(Quad[i].count) + 'Ç', str(Quad[i].action) + 'Ç', str(Quad[i].dir1) + 'Ç', str(
            Quad[i].dir2) + 'Ç', str(Quad[i].result) + '\n'
        file.writelines(line)

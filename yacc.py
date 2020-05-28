# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import ply.yacc as yacc
from lex import archivo
import tables as Tablas
import cuadruplo as quad
import memoriaVirtual as mv
import compiledFile as cf
import estructuras as vect
import sys

Tablas.dirFuncs.clear()
Tablas.varTable.clear()
Tablas.gvarTable.clear()

#Obtains tokens
from lex import tokens

#Lee archivo de prueba
prueba = open(archivo, "r")
entrada = prueba.read()

#Creacion del programa
def p_programa(p):
    '''
    programa : PROGRAMA ID globfunc SEMICOLON gotomain vars funcs endprog
    '''

def p_globfunc(p):
    '''
    globfunc :
    '''
    Tablas.insertDirFunc(p[-1], None, None)
    Tablas.dirFuncs[p[-1]].quad = 0
    Tablas.program = p[-1]

def p_gotomain(p):
    '''
    gotomain :
    '''
    quad.quadInsert('Goto', None, None, None)
    quad.count += 1

def p_vars(p):
    '''
    vars : VAR varaux
         | empty
    '''
    
def p_varaux(p):
    '''
    varaux  : tipo varaux2 SEMICOLON varaux
            | tipo varaux2 SEMICOLON
    '''

def p_varaux2(p):
    '''
    varaux2 : varaux3
            | varaux3 COMMA varaux2
    '''

def p_varaux3(p):
    '''
    varaux3 : ID
            | ID LCORCH vardim CTE_I RCORCH tamvector
            | ID LCORCH vardim CTE_I RCORCH LCORCH CTE_I tammatriz RCORCH
    '''
    salto = 1
    if Tablas.isGlobal == True:
        if Tablas.isVector != None:
            if Tablas.isVector == 1:
                if p[4]<1:
                    print("ERROR: No se puede declarar una matriz o vector con tamaño 0.")
                    sys.exit()
                dir1 = Tablas.findCteVM(p[4])
                m = Tablas.findCteVM(Tablas.m)
                size = Tablas.findCteVM(Tablas.vectSize)
                temp = vect.vector(p[1],dir1,None, m, size)
                salto = Tablas.vectSize
                dir = mv.getMemoGlob(Tablas.myType, salto)
                Tablas.vectGTable[dir] = temp
                tipo = quad.gettipo(dir)
                dirTemp = mv.getMemoCte(tipo)
                temp = Tablas.cteInsert(dir, tipo, dirTemp)
                if (temp == False):
                    mv.restMemo(tipo)
            elif Tablas.isVector == 2:
                if p[4]<1 or p[7]<1:
                    print("ERROR: No se puede declarar una matriz o vector con tamaño 0.")
                    sys.exit()
                dir1 = Tablas.findCteVM(p[4])
                dir2 = Tablas.findCteVM(p[7])
                m = Tablas.findCteVM(Tablas.m)
                size = Tablas.findCteVM(Tablas.vectSize)
                temp = vect.vector(p[1],dir1,dir2, m, size)
                salto = Tablas.vectSize
                dir = mv.getMemoGlob(Tablas.myType, salto)
                Tablas.vectGTable[dir] = temp
                tipo = quad.gettipo(dir)
                dirTemp = mv.getMemoCte(tipo)
                temp = Tablas.cteInsert(dir, tipo, dirTemp)
                if (temp == False):
                    mv.restMemo(tipo)
        else:
            dir = mv.getMemoGlob(Tablas.myType, salto)
    else:
        if Tablas.isVector != None:
            if Tablas.isVector == 1:
                if p[4]<1:
                    print("ERROR: No se puede declarar una matriz o vector con tamaño 0.")
                    sys.exit()
                dir1 = Tablas.findCteVM(p[4])
                m = Tablas.findCteVM(Tablas.m)
                size = Tablas.findCteVM(Tablas.vectSize)
                temp = vect.vector(p[1],dir1,None, m, size)
                salto = Tablas.vectSize
                dir = mv.getMemoLoc(Tablas.myType, salto)
                Tablas.vectLTable[dir] = temp
                tipo = quad.gettipo(dir)
                dirTemp = mv.getMemoCte(tipo)
                temp = Tablas.cteInsert(dir, tipo, dirTemp)
                if (temp == False):
                    mv.restMemo(tipo)
            elif Tablas.isVector == 2:
                if p[4]<1 or p[7]<1:
                    print("ERROR: No se puede declarar una matriz o vector con tamaño 0.")
                    sys.exit()
                dir1 = Tablas.findCteVM(p[4])
                dir2 = Tablas.findCteVM(p[7])
                m = Tablas.findCteVM(Tablas.m)
                size = Tablas.findCteVM(Tablas.vectSize)
                temp = vect.vector(p[1],dir1,dir2, m, size)
                salto = Tablas.vectSize
                dir = mv.getMemoLoc(Tablas.myType, salto)
                Tablas.vectLTable[dir] = temp
                tipo = quad.gettipo(dir)
                dirTemp = mv.getMemoCte(tipo)
                temp = Tablas.cteInsert(dir, tipo, dirTemp)
                if (temp == False):
                    mv.restMemo(tipo)
        else:
            dir = mv.getMemoLoc(Tablas.myType, salto)
    Tablas.insert(p[1], Tablas.myType, dir, salto)
    Tablas.isVector = None

def p_vardim(p):
    '''
    vardim :
    '''
    Tablas.isVector = p[-2]
    tipo = quad.gettipo(0)
    dir = mv.getMemoCte(tipo)
    temp = Tablas.cteInsert(0, tipo, dir)
    if (temp == False):
        mv.restMemo(tipo)

def p_tamvector(p):
    '''
    tamvector :
    '''
    tipo = quad.gettipo(p[-2])
    #Memoria Virtual
    dir = mv.getMemoCte(tipo)
    temp = Tablas.cteInsert(p[-2], tipo, dir)
    if (temp == False):
        mv.restMemo(tipo)
    Tablas.vectSize = p[-2]
    Tablas.m = 1
    tipo = quad.gettipo(Tablas.vectSize)
    tipo2 = quad.gettipo(Tablas.m)
    dir = mv.getMemoCte(tipo)
    temp = Tablas.cteInsert(Tablas.vectSize, tipo, dir)
    if (temp == False):
        mv.restMemo(tipo)
    dir2 = mv.getMemoCte(tipo2)
    temp2 = Tablas.cteInsert(Tablas.m, tipo2, dir2)
    if (temp2 == False):
        mv.restMemo(tipo2)
    Tablas.isVector = 1

def p_tammatriz(p):
    '''
    tammatriz :
    '''
    tipo = quad.gettipo(p[-1])
    tipo2 = quad.gettipo(p[-4])
    #Memoria Virtual
    dir = mv.getMemoCte(tipo)
    temp = Tablas.cteInsert(p[-1], tipo, dir)
    if (temp == False):
        mv.restMemo(tipo)
    dir2 = mv.getMemoCte(tipo2)
    temp2 = Tablas.cteInsert(p[-4], tipo2, dir2)
    if (temp2 == False):
        mv.restMemo(tipo2)
    Tablas.vectSize = (p[-1]+1)*(p[-4]+1)
    Tablas.m = Tablas.vectSize/(p[-4]-0+1)
    tipo = quad.gettipo(Tablas.vectSize)
    tipo2 = quad.gettipo(Tablas.m)
    dir = mv.getMemoCte(tipo)
    temp = Tablas.cteInsert(Tablas.vectSize, tipo, dir)
    if (temp == False):
        mv.restMemo(tipo)
    dir2 = mv.getMemoCte(tipo2)
    temp2 = Tablas.cteInsert(Tablas.m, tipo2, dir2)
    if (temp2 == False):
        mv.restMemo(tipo2)
    Tablas.isVector = 2
def p_functipo(p):
    '''
    functipo : INT
             | FLOAT
             | CHAR
             | STRING
             | VOID
    '''
    Tablas.funcType = p[1]

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | CHAR
         | STRING
    '''
    Tablas.myType = p[1]

def p_funcs(p):
    '''
    funcs : setmain principal
          | funcsaux setmain principal
    '''

def p_setGotoMain(p):
    '''
    setmain :
    '''
    quad.gotoMain()

def p_principal(p):
    '''
    principal : PRINCIPAL LPARENT RPARENT bloque
    '''

def p_funcsaux(p):
    '''
    funcsaux : func insertparams endfunc
             | func insertparams endfunc funcsaux
    '''

def p_endfunc(p):
    '''
    endfunc :
    '''
    quad.quadInsert('Endfunc', None, None, None)
    quad.count += 1

def p_func(p):
    '''
    func : getquad FUNCION funcaux
    '''
    
def p_getquad(p):
    '''
    getquad :
    '''
    Tablas.quad = quad.count

def p_funcaux(p):
    '''
    funcaux : functipo funcaux2
    '''

def p_funcaux2(p):
    '''
    funcaux2 : ID dirfuncinsert LPARENT dirfuncfalse funcaux3 RPARENT vars bloque dirfunctrue
    '''

def p_dirfuncinsert(p):
    '''
    dirfuncinsert :
    '''
    Tablas.func = p[-1]
    if (Tablas.isGlobal == True):
        dir = mv.getMemoGlob(Tablas.funcType, 1)
    else:
        dir = mv.getMemoLoc(Tablas.funcType, 1)
    Tablas.insert(p[-1], Tablas.funcType, dir, 1)
    Tablas.insertDirFunc(p[-1], Tablas.funcType, dir)

def p_insertparams(p):
    '''
    insertparams :
    '''
    Tablas.insertFuncParams(Tablas.params, Tablas.func)
    Tablas.params = ''
    size = str(Tablas.li) + ',' + str(Tablas.lf) + ',' + str(Tablas.lc) + ',' + str(Tablas.lti) + ',' + str(Tablas.ltf) + ',' + str(Tablas.ltc) + ',' + str(Tablas.ltb)
    Tablas.insertFuncSize(size, Tablas.func)
    Tablas.clearVarSize()
    Tablas.insertFuncQuad(Tablas.quad-1, Tablas.func)
    Tablas.func = ''

def p_funcaux3(p):
    '''
    funcaux3 : funcaux4
             | empty
    '''

def p_funcaux4(p):
    '''
    funcaux4 : tipo funcaux5
             | tipo funcaux5 funcaux4
    '''

def p_funcaux5(p):
    '''
    funcaux5 : ID
             | ID COMMA
    '''
    if (Tablas.isGlobal == True):
        dir = mv.getMemoGlob(Tablas.myType, 1)
    else:
        dir = mv.getMemoLoc(Tablas.myType, 1)
    Tablas.insert(p[1], Tablas.myType, dir, 1)
    Tablas.params = str(Tablas.params) + Tablas.myType[0]

def p_bloque(p):
    '''
    bloque : LBRACE RBRACE
           | LBRACE bloqueaux RBRACE
    '''

def p_bloqueaux(p):
    '''
    bloqueaux : estatuto
              | estatuto bloqueaux
              | retorno
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
             | si si2
             | mientras
             | desde
             | lectura
             | fcall SEMICOLON
             | escritura
    '''

def p_si(p):
    '''
    si : siaux
       | siaux si3 SINO bloque
    '''

def p_si3(p):
    '''
    si3 :
    '''
    temp = quad.Goto_SI()
    if temp:
        quad.count += 1

def p_siaux(p):
    '''
    siaux : SI LPARENT expresion RPARENT si1 ENTONCES bloque
    '''

def p_si1(p):
    '''
    si1 :
    '''
    temp = quad.GotoF_SI()
    if temp:
        quad.count += 1

def p_si2(p):
    '''
    si2 :
    '''
    quad.fillGoto()

def p_asignacion(p):
    '''
    asignacion : ID pushpilaid asignacionaux popassign SEMICOLON
    '''

def p_popassign(p):
    '''
    popassign :
    '''
    temp = quad.popAssign()
    if temp:
        quad.count += 1

def p_asignacionaux(p):
    '''
    asignacionaux : IGUAL pushpoper expresion
                  | dimensiones IGUAL pushpoper expresion
    '''

def p_dimensiones(p):
    '''
    dimensiones : addfalsebottom LCORCH removeid addfalsebottom exp removefalsebottom ver1 RCORCH removefalsebottom
                | addfalsebottom LCORCH removeid addfalsebottom exp removefalsebottom ver2 COMMA addfalsebottom exp removefalsebottom ver3 RCORCH removefalsebottom
    '''

def p_ver1(p):
    '''
    ver1 :
    '''
    temp = quad.PilaO.pop()
    #quad.PilaO.append(temp)
    loc = Tablas.findLVector(Tablas.isVector)
    lim1 = Tablas.findCteVM(0)
    if loc == True:
        lim2 = Tablas.vectLTable[Tablas.isVector].lim1
    else:
        lim2 = Tablas.vectGTable[Tablas.isVector].lim1
    quad.quadInsert('Ver', temp, lim1, lim2)
    quad.count += 1
    result = mv.getMemoTemp('int', Tablas.isGlobal)
    dir = Tablas.findCteVM(Tablas.isVector)
    quad.quadInsert('+', temp, dir, result)
    quad.count += 1
    quad.PilaO.append('('+str(result)+')')

def p_ver2(p):
    '''
    ver2 :
    '''
    temp = quad.PilaO.pop()
    #quad.PilaO.append(temp)
    loc = Tablas.findLVector(Tablas.isVector)
    lim1 = Tablas.findCteVM(0)
    if loc == True:
        lim2 = Tablas.vectLTable[Tablas.isVector].lim1
        m = Tablas.vectLTable[Tablas.isVector].m
    else:
        lim2 = Tablas.vectGTable[Tablas.isVector].lim1
        m = Tablas.vectGTable[Tablas.isVector].m
    quad.quadInsert('Ver', temp, lim1, lim2)
    quad.count += 1
    result = mv.getMemoTemp('int',Tablas.isGlobal)
    quad.quadInsert('*', temp, m, result)
    quad.count += 1
    quad.PilaO.append(result)

def p_ver3(p):
    '''
    ver3 :
    '''
    temp = quad.PilaO.pop()
    loc = Tablas.findLVector(Tablas.isVector)
    lim1 = Tablas.findCteVM(0)
    if loc == True:
        lim2 = Tablas.vectLTable[Tablas.isVector].lim1
    else:
        lim2 = Tablas.vectGTable[Tablas.isVector].lim1
    quad.quadInsert('Ver', temp, lim1, lim2)
    quad.count += 1
    temp2 = quad.PilaO.pop()
    result = mv.getMemoTemp('int', Tablas.isGlobal)
    quad.quadInsert('+', temp, temp2, result)
    quad.count += 1
    result2 = mv.getMemoTemp('int', Tablas.isGlobal)
    dir = Tablas.findCteVM(Tablas.isVector)
    quad.quadInsert('+', result, dir, result2)
    quad.count += 1
    quad.PilaO.append('('+str(result2)+')')

def p_removeid(p):
    '''
    removeid :
    '''
    idDir = quad.PilaO.pop()
    tipo = quad.Ptypes.pop()
    temp = Tablas.findCteVM(idDir)
    if temp == False:
        print('Error: No es variable dimensionada')
        sys.exit()
    else:
        Tablas.isVector = idDir


def p_pos(p):
    '''
    pos : ID
        | CTE_I
    '''

def p_retorno(p):
    '''
    retorno : REGRESA pushpoper LPARENT exp RPARENT popret SEMICOLON
    '''

def p_popret(p):
    '''
    popret :
    '''
    temp = quad.popRet()
    if temp:
        quad.count += 1

def p_lectura(p):
    '''
    lectura : LEE pushpoper LPARENT lecturaaux RPARENT SEMICOLON
    '''

def p_lecturaaux(p):
    '''
    lecturaaux : ID pushpilaid popio
               | ID pushpilaid popio COMMA lequad lecturaaux
               | ID pushpilaid dimensiones popio
               | ID pushpilaid dimensiones popio COMMA lequad lecturaaux
    '''

def p_lequad(p):
    '''
    lequad :
    '''
    quad.pushPoper('lee')

def p_fcall(p):
    '''
    fcall : ID erainsert LPARENT RPARENT
          | ID erainsert LPARENT addfalsebottom fcallaux RPARENT removefalsebottom
    '''
    quad.gosub(p[1])
    quad.count += 1
    temp = quad.parcheguad(p[1], Tablas.isGlobal)
    if (temp):
        quad.count += 1
    quad.param = 1

def p_erainsert(p):
    '''
    erainsert :
    '''
    quad.quadInsert('Era', None, None, p[-1])
    quad.count += 1

def p_fcallaux(p):
    '''
    fcallaux : addfalsebottom expresion removefalsebottom paraminsert
             | addfalsebottom expresion removefalsebottom paraminsert COMMA fcallaux
    '''

def p_paraminsert(p):
    '''
    paraminsert :
    '''
    quad.paramInsert()
    quad.param += 1
    quad.count += 1

def p_escritura(p):
    '''
    escritura : ESCRIBE pushpoper LPARENT escrituraaux RPARENT SEMICOLON
    '''

def p_popio(p):
    '''
    popio :
    '''
    temp = quad.popIO()
    if temp:
        quad.count += 1

def p_escrituraaux(p):
    '''
    escrituraaux : CTE_S ctemem pushpilao popio
                 | expresion popio
                 | CTE_S ctemem pushpilao popio COMMA escquad escrituraaux
                 | expresion popio COMMA escquad escrituraaux
    '''

def p_escquad(p):
    '''
    escquad :
    '''
    quad.pushPoper('escribe')

def p_mientras(p):
    '''
    mientras : MIENTRAS while1 LPARENT expresion RPARENT while2 HAZ bloque while3
    '''

def p_while1(p):
    '''
    while1 :
    '''
    quad.pushJumps()

def p_while2(p):
    '''
    while2 :
    '''
    temp = quad.GotoF_While()
    if temp:
        quad.count += 1

def p_while3(p):
    '''
    while3 :
    '''
    temp = quad.Goto_While()
    if temp:
        quad.count += 1

def p_desde(p):
    '''
    desde : DESDE desdeaux popassign while1 HASTA exp for2 while2 HACER bloque for4 for5 while3
    '''

def p_for2(p):
    '''
    for2 :
    '''
    temp = quad.compareFor(Tablas.isGlobal)
    if temp:
        quad.count += 1
    
def p_for4(p):
    '''
    for4 :
    '''
    temp = quad.addToFor(Tablas.isGlobal)
    if temp:
        quad.count += 1
    
def p_for5(p):
    '''
    for5 :
    '''
    temp = quad.assignToFor()
    if temp:
        quad.count += 1

def p_desdeaux(p):
    '''
    desdeaux : ID pushpilaid IGUAL pushpoper exp
             | ID pushpilaid dimensiones IGUAL pushpoper exp
    '''

def p_expresion(p):
    '''
    expresion : expr
              | expr log expresion
    '''

def p_poplog(p):
    '''
    poplog :
    '''
    temp = quad.popLog(Tablas.isGlobal)
    if temp:
        quad.count += 1

def p_expr(p):
    '''
    expr : exp poprel
         | exp poprel rel expr
    '''

def p_porel(p):
    '''
    poprel :
    '''
    temp = quad.popRel(Tablas.isGlobal)
    if temp:
        quad.count += 1

def p_exp(p):
    '''
    exp : termino popterm
        | termino popterm MAS pushpoper exp
        | termino popterm MENOS pushpoper exp
    '''


def p_pushpoper(p):
    '''
    pushpoper :
    '''
    quad.pushPoper(p[-1])

def p_popterm(p):
    '''
    popterm :
    '''
    temp = quad.popTerm(Tablas.isGlobal)
    if temp:
        quad.count += 1

def p_termino(p):
    '''
    termino : factor popfact
            | factor popfact MULT pushpoper termino
            | factor popfact DIV pushpoper termino
    '''

def p_popfact(p):
    '''
    popfact :
    '''
    temp = quad.popFact(Tablas.isGlobal)
    if temp:
        quad.count += 1

def p_factor(p):
    '''
    factor : LPARENT addfalsebottom expresion RPARENT removefalsebottom
           | var_cte
           | MAS pushpoper var_cte
           | MENOS pushpoper var_cte
    '''

def p_addfalsebottom(p):
    '''
    addfalsebottom :
    '''
    quad.pushPoper(p[-1])

def p_removefalsebottom(p):
    '''
    removefalsebottom :
    '''
    quad.popFalseBottom()

def p_var_cte(p):
    '''
    var_cte : ID pushpilaid
            | ID pushpilaid dimensiones
            | CTE_I ctemem pushpilao
            | CTE_F ctemem pushpilao
            | CTE_S ctemem pushpilao
            | CTE_C ctemem pushpilao
            | fcall
    '''

def p_pushpilaid(p):
    '''
    pushpilaid :
    '''
    tipo = Tablas.getIdType(p[-1])
    dir = Tablas.findVM(p[-1])
    quad.pushPilaO(dir)
    quad.pushType(tipo)

def p_ctemem(p):
    '''
    ctemem :
    '''
    tipo = quad.gettipo(p[-1])
    #Memoria Virtual
    dir = mv.getMemoCte(tipo)
    temp = Tablas.cteInsert(p[-1], tipo, dir)
    if (temp == False):
        mv.restMemo(tipo)
    
def p_pushpilao(p):
    '''
    pushpilao :
    '''
    tipo = quad.gettipo(p[-2])
    dir = Tablas.findCteVM(p[-2])
    #Cuadruplo
    quad.pushPilaO(dir)
    quad.pushType(tipo)

def p_log(p):
    '''
    log : AND pushpoper
        | OR pushpoper
    '''

def p_rel(p):
    '''
    rel : MENOR pushpoper
        | MAYOR pushpoper
        | MENORIGUAL pushpoper
        | MAYORIGUAL pushpoper
        | COMPARE pushpoper
        | DIFFERENT pushpoper
    '''

#Funciones Nuerales
def p_dirfunctrue(p):
    '''
    dirfunctrue :
    '''
    Tablas.isGlobal = True
    #Tablas.varsPrint()
    #print('')
    mv.lI = 13000
    mv.ltI = 16000
    mv.ltF = 17000
    mv.ltC = 18000
    mv.ltB = 19000
    Tablas.varTable.clear()
    Tablas.vectLTable.clear()

def p_dirfuncfalse(p):
    '''
    dirfuncfalse :
    '''
    Tablas.isGlobal = False

def p_empty(p):
    '''
    empty :
    '''
    pass

#Errores de sintaxis
def p_error(p):
    print("ERROR DE SINTAXIS", p)

def p_endprog(p):
    '''
    endprog :
    '''
    size = str(Tablas.gli) + ',' + str(Tablas.glf) + ',' + str(Tablas.glc) + ',' + str(Tablas.glti) + ',' + str(Tablas.gltf) + ',' + str(Tablas.gltc) + ',' + str(Tablas.gltb)
    Tablas.insertFuncSize(size, Tablas.program)
    quad.quadInsert('End', None, None, None)
    cf.export_txt(Tablas.dirFuncs, Tablas.cteTable, quad.Quad)
    Tablas.gvarPrint()
    print('')
    print('DirFunc')
    Tablas.dirPrint()
    print('')
    print('Constantes')
    Tablas.ctePrint()
    print('')
    print('Cuadruplos')
    quad.imprime()
    #print('')
    #Tablas.gVectPrint()

#Build parse
parser = yacc.yacc()
result = parser.parse(entrada)

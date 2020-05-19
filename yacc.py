# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import ply.yacc as yacc
from lex import archivo
import tables as Tablas
import cuadruplo as quad
import sys

Tablas.dirFuncs.clear()
Tablas.varTable.clear()

# Obtains tokens
from lex import tokens

# Lee archivo de prueba
prueba = open(archivo, "r")
entrada = prueba.read()


# Creacion del programa
def p_programa(p):
    '''
    programa : PROGRAMA ID SEMICOLON vars funcs
    '''


# ======================== VARIABLES =======================
def p_vars(p):
    '''
    vars : VAR varaux
    '''
    # 5.Insert into DirFunc the number of local variables defined.
    # 6.Insert into DirFunc the current quadruple counter (CONT),


def p_varaux(p):
    '''
    varaux  : tipo varaux2 SEMICOLON varaux
            | tipo varaux2 SEMICOLON
    '''


def p_varaux2(p):
    '''
    varaux2 : ID
            | ID COMMA varaux2
            | ID LCORCH CTE_I RCORCH
            | ID LCORCH CTE_I RCORCH COMMA varaux2
            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH
            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH  COMMA varaux2
    '''
    Tablas.insert(p[1], Tablas.myType)


# ======================== END VARIABLES =======================
# ======================== FUNCIONES =======================

def p_funcs(p):
    '''
    funcs : principal
          | funcsaux principal
    '''


def p_principal(p):
    '''
    principal : PRINCIPAL LPARENT RPARENT bloque
    '''


def p_funcsaux(p):
    '''
    funcsaux : func
             | func funcsaux
    '''


def p_func(p):
    '''
    func : FUNCION funcaux
    '''
    Tablas.insert(Tablas.func, Tablas.funcType)


def p_funcaux(p):
    '''
    funcaux : functipo funcaux2
    '''


def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | CHAR
         | STRING
    '''
    Tablas.myType = p[1]


def p_functipo(p):
    '''
    functipo : INT
             | FLOAT
             | CHAR
             | STRING
             | VOID
    '''
    Tablas.funcType = p[1]


def p_funcaux2(p):
    '''
    funcaux2 : ID LPARENT funcaux3 RPARENT vars bloque dirfunctrue
    '''
    Tablas.func = p[1]

def p_funcaux3(p):
    '''
    funcaux3 : dirfuncfalse tipo ID
             | dirfuncfalse tipo ID COMMA funcaux3
    '''
    Tablas.insert(p[3], Tablas.myType)
    # 2.- Insert every parameter into the current (local) VarTable.
    # 3.- Insert the type to every parameter uploaded into the VarTable.At the same time into the ParameterTable (to create the Function’s signature)..
    #4.- Insert into DirFunc the number of parameters defined.
# ======================== END FUNCIONES =======================
# ======================== BLOQUE =======================

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
    dimensiones : LCORCH pos RCORCH
                | LCORCH pos COMMA pos RCORCH
    '''


def p_pos(p):
    '''
    pos : ID
        | CTE_I
    '''


def p_retorno(p):
    '''
    retorno : REGRESA LPARENT exp RPARENT SEMICOLON
    '''


def p_lectura(p):
    '''
    lectura : LEE pushpoper LPARENT lecturaaux RPARENT popio SEMICOLON
    '''


def p_lecturaaux(p):
    '''
    lecturaaux : ID pushpilaid
               | ID pushpilaid dimensiones
               | ID pushpilaid dimensiones COMMA lecturaaux
    '''


def p_fcall(p):
    '''
    fcall : ID pushfunId LPARENT era checkParameter RPARENT
          | ID LPARENT fcallaux RPARENT
    '''


def p_pushfunId(p):  # VERIFY
    '''
    pushfunId :
    '''
    Tablas.funcParam = p[-1]
    if Tablas.funcParam in Tablas.varTable.keys():
        Tablas.isParam = True
        Tablas.arrParam = Tablas.getidParam(p[-1])
    else:
        print("ERROR: Función no declarada.")
        sys.exit()
    p[0] = p[-1]

def p_era(p):  # VERIFY
    '''
    era :
    '''
    quad.genEraQuad(p[-3])

def p_checkParameter(p):
    '''
    checkParameter : exp checkArg
             | exp checkArg COMMA addParameter checkParameter
    '''

def p_addParameter(p):
    '''
        addParameter :
    '''
    quad.addParam()


def p_checkArg(p):  # VERIFY
    '''
    checkArg :
    '''
    valor = quad.genQuadParam()
    if Tablas.isParam:
        # IF para checar si la llamada a funcion es dentro del main o de una funcion
        if Tablas.isGlobal:
            Tablas.contParams += 1
            if Tablas.contParams > Tablas.simbolos[Tablas.funcParam].value["PARAMCANTI"].value:
                print("Sobran parametros en la funcion", Tablas.funcParam, ".")
                sys.exit()
            Tablas.updateIdOfFun(Tablas.arrParam[-1], Tablas.funcParam, valor)
            del (Tablas.arrParam[-1])
        if Tablas.esFuncion:
            Tablas.contParams += 1
            if Tablas.contParams > Tablas.simbolos[Tablas.funcParam].value["PARAMCANTI"].value:
                print("Sobran parametros en la funcion", Tablas.funcParam, "en", Tablas.miIdFunciones)
                sys.exit()
            Tablas.updateIdOfFun(Tablas.arrParam[-1], Tablas.miIdFunciones, valor)
            del (Tablas.arrParam[-1])



def p_fcallaux(p):
    '''
    fcallaux : expresion
             | expresion COMMA fcallaux
    '''


def p_escritura(p):
    '''
    escritura : ESCRIBE pushpoper LPARENT escrituraaux RPARENT popio SEMICOLON
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
    escrituraaux : CTE_S
                 | expresion
                 | CTE_S COMMA escrituraaux
                 | expresion COMMA escrituraaux
    '''


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
    temp = quad.compareFor()
    if temp:
        quad.count += 1


def p_for4(p):
    '''
    for4 :
    '''
    temp = quad.addToFor()
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


def p_poolog(p):
    '''
    poplog :
    '''
    temp = quad.popLog()
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
    temp = quad.popRel()
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
    temp = quad.popTerm()
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
    temp = quad.popFact()
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
            | CTE_I pushpilao
            | CTE_F pushpilao
            | CTE_S pushpilao
            | CTE_C pushpilao
            | fcall
    '''


def p_pushpilaid(p):
    '''
    pushpilaid :
    '''
    tipo = Tablas.getIdType(p[-1])
    quad.pushPilaO(p[-1])
    quad.pushType(tipo)


def p_pushpilao(p):
    '''
    pushpilao :
    '''
    tipo = quad.gettipo(p[-1])
    quad.pushPilaO(p[-1])
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



def p_cte(p):
    '''CTE : CTE_I
    | CTE_F
    | CTE_CH
    | CTE_STRING
    | FUNCION
   '''


# Funciones Nuerales
def p_dirfunctrue(p):
    '''
    dirfunctrue :
    '''
    Tablas.isGlobal = True
    Tablas.varTable.clear()
    # Tablas.varsPrint()
    # 7.Release the current VarTable (local).


def p_dirfuncfalse(p):
    '''
    dirfuncfalse :
    '''
    Tablas.isGlobal = False


# Errores de sintaxis
def p_error(p):
    # Tablas.dirPrint()
    quad.imprime()
    print("ERROR DE SINTAXIS", p)


# Build parse
parser = yacc.yacc()
result = parser.parse(entrada)

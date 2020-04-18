# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------
import ply.yacc as yacc
from lex import archivo
#Obtains tokens
from lex import tokens

#Lee archivo de prueba
prueba = open(archivo, "r")
entrada = prueba.read()

def p_programa(p):
    '''
    programa : PROGRAMA ID SEMICOLON vars funcs
    '''

def p_vars(p):
    '''
    vars : VAR varaux
    '''

def p_varaux(p):
    '''
    varaux  : tipo varaux2 SEMICOLON varaux
            | tipo varaux2 SEMICOLON
    '''

def p_varaux2(p):
    '''
    varaux2 : ID
            | ID COMMA varuax2
            | ID LCORCH CTE_I RCORCH
            | ID LCORCH CTE_I RCORCH COMMA varaux2
            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH
            | ID LCORCH CTE_I RCORCH LCORCH CTE_I RCORCH  COMMA varaux2
    '''

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
         | CHAR
    '''

def p_funcs(p):
    '''
    funcs : principal
          | funcsaux principal
    '''

def p_funcs2(p):
    '''
    funcsaux : func
             | func funcsaux
    '''

def p_func(p):
    '''
    func : FUNCION funcaux
    '''

def p_funcaux(p):
    '''
    funcaux : tipo funcaux2
            | VOID funcaux2
    '''

def p_funcaux2(p):
    '''
    funcaux2 : ID LPARENT funcaux3 RPARENT vars bloque
    '''

def p_funcaux3(p):
    '''
    funcaux3 : tipo ID
             | tipo ID COMMA funcaux3
    '''

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
             | si
             | mientras
             | desde
             | lectura
             | escritura
    '''

def p_si(p):
    '''
    si : siaux
       | siaux SINO bloque
    '''

def p_siaux(p):
    '''
    siaux : si LPARENT expresion RPARENT ENTONCES bloque
    '''

def p_asignacion(p):
    '''
    asignacion : ID asignacionaux SEMICOLON
    '''

def p_asignacionaux(p):
    '''
    asignacionaux : IGUAL expresion
                  | dimensiones IGUAL expresion
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
    retorno : regresa LPARENT exp RPARENT SEMICOLON
    '''

def p_lectura(p):
    '''
    lectura: lee LPARENT dimensiones RPARENT SEMICOLON
    '''

def p_escritura(p):
    '''
    escritura : escribe LPARENT escrituraaux RPARENT SEMICOLON
    '''

def p_escrituraaux(p):
    '''
    escrituraaux : CTE_S
                 | expresion
                 | CTE_S COMMA escrituraaux
                 | expresion COMMA escrituraaux
    '''

def p_mientras(p):
    '''
    mientras : mientras LPARENT expresion RPARENT HAZ bloque
    '''

def p_desde(p):
    '''
    desde : desde desdeaux HASTA exp HACER bloque
    '''

def p_desdeaux(p):
    '''
    desdeaux : ID IGUAL exp
             | ID dimensiones IGUAL exp
    '''

def p_expresion(p):
    '''
    expresion : expr
              | expr log expresion
    '''

def p_expr(p):
    '''
    expr : exp
         | exp rel expr
    '''

def p_exp(p):
    '''
    exp : termino
        | termino MAS exp
        | termino MENOS exp
    '''

#Build parser
parser = yacc.yacc()
result = parser.parse(entrada)
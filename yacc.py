import ply.yacc as yacc

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
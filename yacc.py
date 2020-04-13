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
          | funcs2 principal
    '''

def p_funcs2(p):
    '''
    funcs2 : func
           | func funcs2
    '''
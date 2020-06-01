# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García -  A01328426
# Compiladores
# ------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

archivo = None
path = None

# List of token names. This is always required
# RESERVED WORDS
reserved = {
    'null': 'NULL',
    'void': 'VOID',
    'programa': 'PROGRAMA',
    'principal': 'PRINCIPAL',
    'si': 'SI',
    'entonces': 'ENTONCES',
    'var': 'VAR',
    'funcion': 'FUNCION',
    'lee': 'LEE',
    'escribe': 'ESCRIBE',
    'sino': 'SINO',
    'regresa': 'REGRESA',
    'mientras': 'MIENTRAS',
    'haz': 'HAZ',
    'desde': 'DESDE',
    'hasta': 'HASTA',
    'hacer': 'HACER',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'string': 'STRING',
}

# LIST OF TOKENS
tokens = [
    'ID',
    'SEMICOLON',
    'COLON',
    'LBRACE',
    'RBRACE',
    'IGUAL',
    'MAYOR',
    'MENOR',
    'DIFFERENT',
    'LPARENT',
    'RPARENT',
    'COMMA',
    'MAS',
    'MENOS',
    'MULT',
    'DIV',
    'CTE_I',
    'CTE_F',
    'CTE_C',
    'CTE_S',
    'AND',
    'OR',
    'COMPARE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'LCORCH',
    'RCORCH',
    'DETERMINANTE',
    'TRANSPUESTA',
    'INVERSA',
] + list(reserved.values())

#Especiales
t_DETERMINANTE = r'\$'
t_TRANSPUESTA = r'\¡'
t_INVERSA = r'\?'

#Delimeters
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_COMMA = r'\,'
t_COLON = r'\:'
t_SEMICOLON = r'\;'

#Operators
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'

#Comparing
t_COMPARE = r'=='
t_IGUAL = r'\='
t_DIFFERENT = r'!='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_MAYOR = r'\>'
t_MENOR = r'\<'

t_AND = r'&&'
t_OR = r'\|\|'

t_CTE_S = r'\"([^\\\n]|(\\.))*?\"'
t_CTE_C = r'\'[A-Za-z]\''

t_ignore = ' \t\n'


#DECLARACIONES DE FUNCIONES
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_CTE_F(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

##Constuir lexer.
#lex.lex()
#
##Leer archivo prueba
#prueba = open('Pruebas/prueba.txt', "r")
#archivo = 'Pruebas/prueba.txt'
#entrada = prueba.read()
#prueba.close()
#
##Entrada de lexer.
#lex.input(entrada)
#
##Muestra tokens
#while True:
#    tok = lex.token()
#    if not tok:
#        break
#    #print(tok)
lex.lex()

#Leer archivo prueba
print("=================================")
print("===== Iniciando Patito ++ =====" )
x = input('Ingresa el nombre de tu archivo : ')
path = "Pruebas/" + x
print("Leyendo => " + path )
try:
    prueba = open(path, "r")
    archivo = x
    entrada = prueba.read()
    prueba.close()
    lex.input(entrada)
    # Muestra tokens
    while True:
        tok = lex.token()
        if not tok:
            break
        #print(tok)
    print("===== Finalizando Patito ++ =====")
    print("=================================")
except OSError as e:
    print("===== Finalizando Patito ++ =====")
    print("=================================")
    print('Error:')





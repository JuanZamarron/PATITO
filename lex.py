# ------------------------------------------------------------
# Juan Carlos
# Valentin Alexandro Trujillo García -  A01328426
# Compiladores
# ------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# List of token names. This is always required
# RESERVED WORDS
reserved = {
    'null': 'NULL',
    'void': 'VOID',
    'programa': 'PROGRAMA',
    'principal': 'PRINCIPAL',
    'si': 'SI',
    'entonces': 'ENTONCES',
    'vars': 'VAR',
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
             'ID', 'SEMICOLON', 'LBRACE', 'RBRACE',
             'IGUAL', 'GREATERTHAN', 'LESSTHAN','DIFFERENT',
             'LPARENT', 'RPARENT', 'COMMA','NOT'
             'MAS', 'MENOS', 'MULT', 'DIV',
             'CTE_I', 'CTE_F', 'CTE_CH', 'CTE_STRING',
             'AND', 'OR', 'COMPARE', 'MOD',
            'COMMENT','MAYORIGUAL', 'MENORIGUAL', 'LCORCH', 'RCORCH ',

         ] + list(reserved.values())

t_COMMA = r'\,'
t_COLON = r'\:'

t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_SEMICOLON = r'\;'

t_IGUAL = r'\='
t_DIFFERENT = r'!='
t_COMPARE   = r'=='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='

t_LPARENT = r'\('
t_RPARENT= r'\)'

t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_LCORCH   = r'\['
t_RCORCH  = r'\]'

t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'


t_CTE_I     = r'[0-9][0-9]*'
t_CTE_F     = r'(\+|-)?[0-9]+(\.[0-9]+)?f'
t_CTE_CH    = r'\'[A-Za-z]\''
t_CTE_STRING= r'".*."'
t_AND       = r'&&'
t_OR        = r'\|\|'
t_MOD       = r'%'
t_NOT       = r'!'
t_ignore_COMMENT = r'%%.*'

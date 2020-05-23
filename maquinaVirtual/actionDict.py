# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------

def dict(action):
    return {
        '+' : 1,
        '-' : 2,
        '/' : 3,
        '*' : 4,
        '>' : 5,
        '<' : 6,
        '<=' : 7,
        '>=' : 8,
        '==' : 9,
        '!=' : 10,
        '&&' : 11,
        '||' : 12,
        'GotoF' : 13,
        'Goto' : 14,
        'lee' : 15,
        'escribe' : 16,
        '=' : 17,
        'regresa' : 18,
        'Gosub' : 19,
        'Era' : 20,
        'Param' : 21,
        'Endfunc' : 22,
        'End' : 23,
        'Ver' : 24,
    }[action]
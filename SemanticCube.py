# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores varTables
# ------------------------------------------------------------
import sys


# Declaracion de cubo semantico
class SemanticCube:
    def __init__(self):
        self.cube = {
            '+': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'int',
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'float'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'int'
                }
            },
            '-': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'int'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'float'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err'
                }
            },
            '/': {
                'int': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'float'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'float'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string',
                    'boolean': 'float'
                },
                'boolean': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'float'
                }
            },
            '*': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'string',
                    'boolean': 'int'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'float'
                },
                'string': {
                    'int': 'string',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err'
                }
            },
            '>': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'boolean'
                },
            },
            '<': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'boolean'
                },
            },
            '&&': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'boolean'
                },
            },
            '||': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'boolean'
                },
            }
        }

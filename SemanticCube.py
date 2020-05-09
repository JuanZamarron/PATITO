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
                    'char': 'char',  # okay?
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
                    'char': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'int'
                },
                'char': {
                    'int': 'char',  # okay?
                    'float': 'err',
                    'string': 'err',
                    'char': 'char',
                    'boolean': 'err'
                }
            },
            '-': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'char': 'char',
                    'boolean': 'int'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'float'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'char': {
                    'int': 'char',  # okay?
                    'float': 'err',
                    'string': 'err',
                    'char': 'char',
                    'boolean': 'err'
                }
            },
            '/': {
                'int': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'float'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'float'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string',
                    'char': 'err',
                    'boolean': 'float'
                },
                'boolean': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'float'
                },
                'char': {
                    'int': 'err',  # okay?
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                }
            },
            '*': {
                'int': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'float'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'float'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string',
                    'char': 'err',
                    'boolean': 'float'
                },
                'boolean': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'float'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                }
            },
            '>': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'boolean'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                }
            },
            '<': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'boolean'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                }
            },
            '&&': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'boolean'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                }
            },
            '||': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'boolean'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'char': 'err',
                    'boolean': 'err'
                }
            }
        }

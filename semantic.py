# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores varTables
# ------------------------------------------------------------
import sys
from collections import defaultdict

#Declaracion de cubo semantico
semantic_cube = defaultdict(
    lambda: defaultdict(
        lambda: defaultdict(
            lambda: None)))
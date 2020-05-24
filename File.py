# ------------------------------------------------------------
# Juan Carlos Zamarrón Pérez - A00815058
# Valentin Alexandro Trujillo García - A01328426
# Compiladores
# ------------------------------------------------------------


def export_txt(filename, text):
        file = filename
        with open(file, 'w') as x_file:
            x_file.write('{} * Texto en File *'.format(text))

# FUENTES:
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
# https://stackoverflow.com/questions/5214578/print-string-to-text-file
# https://stackoverflow.com/questions/38031290/python-saving-long-string-in-text-file


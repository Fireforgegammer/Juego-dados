import re

def largo_real(texto):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return len(ansi_escape.sub('', texto))

def formatear_bloque(texto, ancho):
    relleno = ancho - largo_real(texto)
    return texto + (" " * relleno)
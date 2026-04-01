import pytest
from src.core.generador import generar_password

# Casos básicos y edge
@pytest.mark.parametrize(
    "longitud,mayus,minus,numeros,simbolos",
    [
        (4, True, True, True, True),   # mínima longitud
        (108, True, True, True, True), # máxima longitud
        (10, False, False, False, False), # solo longitud mínima, sin caracteres especiales
    ]
)
def test_generar_password(longitud, mayus, minus, numeros, simbolos):
    pwd = generar_password(longitud, mayus, minus, numeros, simbolos)
    assert isinstance(pwd, str)
    assert len(pwd) == longitud
    # Si hay mayúsculas
    if mayus:
        assert any(c.isupper() for c in pwd)
    # Si hay minúsculas
    if minus:
        assert any(c.islower() for c in pwd)
    # Si hay números
    if numeros:
        assert any(c.isdigit() for c in pwd)
    # Si hay símbolos
    if simbolos:
        import string
        symbols = string.punctuation
        assert any(c in symbols for c in pwd)
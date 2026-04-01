import pytest
import json
from src.core.generador import generar_password
from src.core.storage import cargar_passwords, guardar_passwords
import tempfile

def test_flujo_completo():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmpfile:
        # Generar contraseña
        pwd = generar_password(12, True, True, True, True)
        guardar_passwords([{"password": pwd, "sitio": None}], tmpfile.name)
        
        # Leer y verificar
        data = cargar_passwords(tmpfile.name)
        assert len(data) == 1
        assert data[0]["password"] == pwd
        assert data[0]["sitio"] is None

def test_edge_sin_caracteres(tmpfile_path=None):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmpfile:
        tmpfile_path = tmpfile.name
    # Guardar lista vacía
    guardar_passwords([], tmpfile_path)
    data = cargar_passwords(tmpfile_path)
    assert data == []
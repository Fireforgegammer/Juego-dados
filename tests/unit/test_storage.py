import pytest
from unittest.mock import patch, mock_open
from src.core.storage import cargar_passwords, guardar_passwords

def test_guardar_y_cargar_passwords():
    mock_data = [{"password": "ABC123", "sitio": None}]
    m = mock_open()
    with patch("builtins.open", m):
        guardar_passwords(mock_data, "fakefile.json")
        m.assert_called_once_with("fakefile.json", "w")
    
    m = mock_open(read_data='[{"password": "ABC123", "sitio": null}]')
    with patch("builtins.open", m):
        data = cargar_passwords("fakefile.json")
        assert data == mock_data
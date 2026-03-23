import pytest
from unittest.mock import patch
from clases import Participante, Taller, SistemaReservas

def test_es_mayor_edad():
    p1 = Participante("Ana", 20, "ana@mail.com")
    p2 = Participante("Luis", 16, "luis@mail.com")
    assert p1.es_mayor_edad() is True
    assert p2.es_mayor_edad() is False

# cupos disponibles
def test_cupos_disponibles():
    taller = Taller("Costura", 2, 50) # Añadido el costo: 50
    assert taller.cupos_disponibles() == 2

# inscripciones y pagos simulados
def test_registro_exitoso_con_pago_aprobado():
    sistema = SistemaReservas()
    taller = Taller("Python Avanzado", 10, 100) # Añadido el costo
    sistema.agregar_taller(taller)
    participante = Participante("Carlos", 25, "carlos@email.com")

    # Forzamos que el pago sea exitoso (True)
    with patch.object(sistema, 'procesar_pago', return_value=True):
        resultado = sistema.registrar_participante_en_taller(participante, taller)

    assert resultado is True
    assert len(taller.lista_inscritos) == 1

def test_registro_fallido_con_pago_rechazado():
    sistema = SistemaReservas()
    taller = Taller("Python Avanzado", 10, 100)
    sistema.agregar_taller(taller)
    participante = Participante("Lucía", 30, "lucia@email.com")

    # Forzamos que el pago falle (False)
    with patch.object(sistema, 'procesar_pago', return_value=False):
        resultado = sistema.registrar_participante_en_taller(participante, taller)

    assert resultado is False
    assert len(taller.lista_inscritos) == 0
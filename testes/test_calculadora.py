import pytest
from src import Calculadora

def test_adicionar():
    calc = Calculadora(5, 3)
    assert calc.adicionar() == 8
    calc = Calculadora(-2, 4)
    assert calc.adicionar() == 2

def test_subtrair():
    calc = Calculadora(10, 4)
    assert calc.subtrair() == 6
    calc = Calculadora(0, 5)
    assert calc.subtrair() == -5

def test_multiplicar():
    calc = Calculadora(2, 3)
    assert calc.multiplicar() == 6
    calc = Calculadora(-2, 4)
    assert calc.multiplicar() == -8

def test_dividir():
    calc = Calculadora(8, 2)
    assert calc.dividir() == 4
    with pytest.raises(ZeroDivisionError):
        Calculadora(5, 0).dividir()

def test_raiz_n():
    calc = Calculadora(9, 2)
    assert pytest.approx(calc.raiz_n()) == 3
    calc = Calculadora(27, 3)
    assert pytest.approx(calc.raiz_n()) == 3

def test_exponencial():
    calc = Calculadora(1, 0)
    assert pytest.approx(calc.exponencial()) == 2.7182818
    calc = Calculadora(0, 0)
    assert pytest.approx(calc.exponencial()) == 1

def test_potencia():
    calc = Calculadora(2, 3)
    assert calc.potencia() == 8
    calc = Calculadora(4, 0.5)
    assert pytest.approx(calc.potencia()) == 2

def test_fatorial():
    calc = Calculadora(5, 0)
    assert calc.fatorial() == 120
    calc = Calculadora(0, 0)
    assert calc.fatorial() == 1

def test_arredondar_para():
    calc = Calculadora(3.14159, 2)
    assert calc.arredondar_para() == 3.14
    calc = Calculadora(2.71828, 3)
    assert calc.arredondar_para() == 2.718

def test_modulo():
    calc = Calculadora(-10, 0)
    assert calc.modulo() == 10
    calc = Calculadora(3.5, 0)
    assert calc.modulo() == 3.5

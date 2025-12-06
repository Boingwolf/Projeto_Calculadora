from src import CalculadoraInteira

def test_somaint():
    assert CalculadoraInteira(5, 5).somaint() == 10
    assert CalculadoraInteira(-2, 3).somaint() == 1

def test_subint():
    assert CalculadoraInteira(9, 4).subint() == 5
    assert CalculadoraInteira(2, 7).subint() == -5

def test_multint():
    assert CalculadoraInteira(3, 4).multint() == 12
    assert CalculadoraInteira(-3, 2).multint() == -6

def test_divint():
    assert CalculadoraInteira(8, 2).divint() == 4
    assert CalculadoraInteira(9, 3).divint() == 3

from src import CalculadoraNumeroTeoria

def test_numero_primo():
    assert CalculadoraNumeroTeoria(7, 0).numero_primo() is True
    assert CalculadoraNumeroTeoria(8, 0).numero_primo() is False

def test_proximo_primo():
    calc = CalculadoraNumeroTeoria(8, 0)
    assert calc.proximo_primo() == 11
    calc = CalculadoraNumeroTeoria(0, 0)
    assert calc.proximo_primo() == 2

def test_mdc():
    calc = CalculadoraNumeroTeoria(12, 18)
    assert calc.mdc() == 6
    calc = CalculadoraNumeroTeoria(9, 3)
    assert calc.mdc() == 3

def test_mmc():
    calc = CalculadoraNumeroTeoria(4, 6)
    assert calc.mmc() == 12
    calc = CalculadoraNumeroTeoria(7, 5)
    assert calc.mmc() == 35

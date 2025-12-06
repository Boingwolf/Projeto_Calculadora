from fractions import Fraction
from src import CalculadoraFracoes

def test_soma_frac():
    calc = CalculadoraFracoes("1/2", "1/4")
    assert calc.soma_frac() == Fraction(3, 4)
    calc = CalculadoraFracoes("2/3", "1/3")
    assert calc.soma_frac() == 1

def test_sub_frac():
    calc = CalculadoraFracoes("3/4", "1/4")
    assert calc.sub_frac() == Fraction(1, 2)
    calc = CalculadoraFracoes("5/6", "1/6")
    assert calc.sub_frac() == Fraction(2, 3)

def test_mult_frac():
    calc = CalculadoraFracoes("1/2", "1/2")
    assert calc.mult_frac() == Fraction(1, 4)
    calc = CalculadoraFracoes("2/3", "3/4")
    assert calc.mult_frac() == Fraction(1, 2)

def test_div_frac():
    calc = CalculadoraFracoes("3/4", "1/2")
    assert calc.div_frac() == Fraction(3, 2)
    calc = CalculadoraFracoes("2/5", "1/5")
    assert calc.div_frac() == 2

def test_simplificar():
    calc = CalculadoraFracoes("4/8", "1")
    assert calc.simplificar() == Fraction(1, 2)
    calc = CalculadoraFracoes("10/20", "1")
    assert calc.simplificar() == Fraction(1, 2)

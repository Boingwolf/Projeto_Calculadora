import pytest
import math
from src import CalculadoraTrigonometrica

def test_seno():
    calc = CalculadoraTrigonometrica(math.pi/2)
    assert pytest.approx(calc.seno(), 0.001) == 1
    calc = CalculadoraTrigonometrica(0)
    assert pytest.approx(calc.seno(), 0.001) == 0

def test_cosseno():
    calc = CalculadoraTrigonometrica(0)
    assert pytest.approx(calc.cosseno(), 0.001) == 1
    calc = CalculadoraTrigonometrica(math.pi)
    assert pytest.approx(calc.cosseno(), 0.001) == -1

def test_tangente():
    calc = CalculadoraTrigonometrica(math.pi/4)
    assert pytest.approx(calc.tangente(), 0.001) == 1
    calc = CalculadoraTrigonometrica(0)
    assert pytest.approx(calc.tangente(), 0.001) == 0

def test_arco_seno():
    calc = CalculadoraTrigonometrica(0.5)
    assert pytest.approx(calc.arco_seno(), 0.001) == math.asin(0.5)
    with pytest.raises(ValueError):
        CalculadoraTrigonometrica(2).arco_seno()

def test_arco_cosseno():
    calc = CalculadoraTrigonometrica(0)
    assert pytest.approx(calc.arco_cosseno(), 0.001) == math.acos(0)
    with pytest.raises(ValueError):
        CalculadoraTrigonometrica(-2).arco_cosseno()

def test_arco_tan():
    calc = CalculadoraTrigonometrica(1)
    assert pytest.approx(calc.arco_tan(), 0.001) == math.pi / 4
    calc = CalculadoraTrigonometrica(0)
    assert calc.arco_tan() == 0

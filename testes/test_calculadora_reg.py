import pytest
import math
import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath("src"))
from src.calculadora import CalculadoraRegistada, Calculadora


@pytest.fixture(autouse=True)
def limpar_historico(tmp_path, monkeypatch):
    caminho_falso = tmp_path / "historico.txt"
    monkeypatch.setattr("src.calculadora.caminho", caminho_falso)
    yield caminho_falso

def test_soma_registrada(limpar_historico):
    calc = CalculadoraRegistada(5, 3)
    resultado = calc.soma()
    assert resultado == 8
    conteudo = limpar_historico.read_text()
    assert "5 + 3 = 8" in conteudo

def test_subtrair_registrada(limpar_historico):
    calc = CalculadoraRegistada(10, 4)
    resultado = calc.menos()
    assert resultado == 6
    assert "10 - 4 = 6" in limpar_historico.read_text()


def test_multiplicar_registrada(limpar_historico):
    calc = CalculadoraRegistada(2, 4)
    resultado = calc.vezes()
    assert resultado == 8
    assert "2 * 4 = 8" in limpar_historico.read_text()

def test_dividir_registrada(limpar_historico):
    calc = CalculadoraRegistada(8, 2)
    resultado = calc.divide()
    assert resultado == 4
    assert "8 / 2 = 4" in limpar_historico.read_text()


def test_raiz_registrada(limpar_historico):
    calc = CalculadoraRegistada(9, 2)
    resultado = calc.raiz()
    assert pytest.approx(resultado, 0.001) == 3
    assert "9 v 2" in limpar_historico.read_text()

def test_exponencial_registrada(limpar_historico):
    calc = CalculadoraRegistada(1, 0)
    resultado = calc.Expe()
    assert pytest.approx(resultado, 0.001) == math.e
    assert f"e ** {calc.n1}" in limpar_historico.read_text()


def test_fatorial_registrada(limpar_historico):
    calc = CalculadoraRegistada(5, 0)
    resultado = calc.Fato()
    assert resultado == 120
    assert "5! = 120" in limpar_historico.read_text()

def test_arredondar_registrada(limpar_historico):
    calc = CalculadoraRegistada(3.14159, 2)
    resultado = calc.Arredonda()
    assert resultado == 3.14
    texto = limpar_historico.read_text()
    assert "3.14159 arredondado para 2 = 3.14" in texto

def test_registarModulo(limpar_historico):
    calc = CalculadoraRegistada(-10, 0)
    calc.resultado = abs(calc.n1)
    calc.registarModulo()
    texto = limpar_historico.read_text()
    assert "O modulo de -10 = 10" in texto

def test_registarExp(limpar_historico):
    calc = CalculadoraRegistada(2, 0)
    calc.resultado = math.exp(2)
    calc.registarExp()
    assert f"e ** 2 = {calc.resultado}" in limpar_historico.read_text()


def test_registarFat(limpar_historico):
    calc = CalculadoraRegistada(4, 0)
    calc.resultado = math.factorial(4)
    calc.registarFat()
    texto = limpar_historico.read_text()
    assert "4! = 24" in texto


def test_registarSimplificada(limpar_historico):
    calc = CalculadoraRegistada("3/4", 0)
    calc.resultado = "1/2"
    calc.registarSimplificada()
    texto = limpar_historico.read_text()
    assert "A fração simplicada" in texto


def test_resgistarIfPrimo_true(limpar_historico):
    calc = CalculadoraRegistada(7, 0)
    calc.resgistarIfPrimo()
    texto = limpar_historico.read_text()
    assert "7 = Primo" in texto

def test_resgistarIfPrimo_false(limpar_historico):
    calc = CalculadoraRegistada(8, 0)
    calc.resgistarIfPrimo()
    texto = limpar_historico.read_text()
    assert "8 = Não Primo" in texto


def test_resgistarProxPrimo(limpar_historico):
    calc = CalculadoraRegistada(10, 0)
    calc.resultado = 11
    calc.resgistarProxPrimo()
    texto = limpar_historico.read_text()
    assert "O proximo primo de 10 = 11" in texto


def test_resgistarMdc(limpar_historico):
    calc = CalculadoraRegistada(12, 18)
    calc.resultado = 6
    calc.resgistarMdc()
    texto = limpar_historico.read_text()
    assert "O MDC de 12 e 18 é 6" in texto

def test_registarMmc(limpar_historico):
    calc = CalculadoraRegistada(3, 5)
    calc.resultado = 15
    calc.registarMmc()
    texto = limpar_historico.read_text()
    assert "O Mmc de 3 e 5 é 15" in texto


def test_registrar_trig(limpar_historico):
    calc = CalculadoraRegistada(math.pi/2, 0)
    calc.resultado = 1
    calc.registrar_trig("seno")
    texto = limpar_historico.read_text()
    assert "seno(" in texto

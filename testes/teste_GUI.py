import pytest
from unittest.mock import MagicMock, patch
from fractions import Fraction
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.GUI import GUI


@pytest.fixture(scope="module")
def app():
    """Cria a GUI em modo teste (sem mainloop, sem ficheiros)."""
    with patch("builtins.open", create=True) as fake_open:
        fake_open.return_value.__enter__.return_value = []
        gui = GUI.__new__(GUI)
        GUI.__init__(gui)
        gui.janela.withdraw()
        gui.historico.carregar_historico = MagicMock()
        gui.historico.atualizar_historico = MagicMock()  # type: ignore[attr-defined]

        yield gui
        gui.janela.destroy()

# ------------------ Testes básicos ------------------

def test_input_value(app):
    app.clean()
    app.inputValue("12")
    assert app.showValue.get() == "12"

def test_clean(app):
    app.inputValue("123")
    app.clean()
    assert app.showValue.get() == ""

def test_apagar(app):
    app.inputValue("123")
    app.apagar()
    assert app.showValue.get().endswith("12")

def test_set_operador(app):
    app.clean()
    app.inputValue("5")
    app.set_operador("+")
    assert "+" in app.showValue.get()

def test_calculate_soma(app):
    app.clean()
    app.inputValue("3+2")
    app.calculate()
    assert app.showValue.get() in ["5", "5.0"]

# ------------------ Testes Trigonometria ------------------

def test_func_trig_sin(app):
    app.clean()
    app.showValue.set("90")
    app.angulo_var.set("deg")
    app.func_trig("sin")
    assert round(float(app.showValue.get()), 6) == 1.0

def test_func_trig_cos(app):
    app.clean()
    app.showValue.set("0")
    app.angulo_var.set("deg")
    app.func_trig("cos")
    assert round(float(app.showValue.get()), 6) == 1.0

# ------------------ Testes Frações ------------------

def test_soma_fracao(app):
    app.clean()
    app.inputValue("1/2+1/3")
    app.soma_fracao()
    val = app.showValue.get()
    assert "5/6" in val or "0.833" in val

def test_simpl_frac(app):
    app.clean()
    app.inputValue("2/4")
    app.simpl_frac()
    assert app.showValue.get() == "1/2"

# ------------------ Testes Número Teoria ------------------

def test_divisores_numero(app):
    app.clean()
    app.inputValue("6")
    app.divisores_numero()
    val = app.showValue.get()
    assert "1" in val and "6" in val

def test_numero_primo(app):
    app.clean()
    app.inputValue("7")
    app.numero_primo()
    assert app.showValue.get() == "True"

def test_fatorial_numero(app):
    app.clean()
    app.inputValue("5")
    app.fatorial_numero()
    assert app.showValue.get() in ["120", "120.0"]

def test_mdc_numero(app):
    app.clean()
    app.inputValue("8,12")
    app.mdc_numero()
    assert app.showValue.get() == "4"

def test_mmc_numero(app):
    app.clean()
    app.inputValue("3,4")
    app.mmc_numero()
    assert app.showValue.get() == "12"

# ------------------ Testes GUI: Checkbuttons e Botões ------------------

def test_checkboxes_toggle(app):
    """Ativa e desativa todas as checkboxes."""
    for var in [app.trigonometria_var, app.fracoes_var, app.numeroTeoria_var, app.historico_var]:
        var.set(True)
        app.formatar_botoes("4" if var == app.historico_var else "1")
        var.set(False)
    assert True  # se não der erro, passou

def test_botao_numerico(app):
    """Verifica que o botão 5 insere o valor."""
    app.clean()
    b5 = None
    for child in app.frame_2.winfo_children():
        if getattr(child, "cget", lambda x: None)("text") == "5":
            b5 = child
            break
    assert b5 is not None
    b5.invoke()
    assert app.showValue.get().endswith("5")

def test_botao_igual(app):
    """Verifica que o botão '=' executa cálculo."""
    app.clean()
    app.inputValue("9+1")
    beq = None
    for child in app.frame_2.winfo_children():
        if getattr(child, "cget", lambda x: None)("text") == "=":
            beq = child
            break
    beq.invoke() # type: ignore
    assert app.showValue.get() in ["10", "10.0"]

def test_checkbox_historico_abre(app):
    """Simula abrir e fechar o histórico."""
    app.historico_var.set(True)
    app.formatar_botoes("4")
    app.historico_var.set(False)
    app.formatar_botoes("4")
    assert True

def test_radio_angulo(app):
    """Verifica que o radiobutton de ângulo muda valor."""
    app.angulo_var.set("deg")
    assert app.angulo_var.get() == "deg"
    app.angulo_var.set("rad")
    assert app.angulo_var.get() == "rad"

def test_voltar_calculadora_basica(app):
    """Verifica que pode voltar da trigonometria para a básica."""
    app.trigonometria_var.set(True)
    app.formatar_botoes("1")
    app.trigonometria_var.set(False)
    app.formatar_botoes("1")
    assert True

from tkinter import * # type: ignore
from tkinter import ttk
from calculadora import *
import math
from fractions import Fraction
import re
from pathlib import Path

# Cores e fontes globais
bg_color = "#1e1e1e"
bt_bg_color = "#2F2F2F"
txt_color = "#FFFFFF"
txt_font = ("Comic Sans MS", 14, "bold")


class Historico:
    def __init__(self, master):
        self.janela_history = Toplevel(master)
        self.janela_history.title("Histórico de Cálculos")
        self.janela_history.config(bg=bg_color)
        self.janela_history.geometry("400x600")
        self.janela_history.resizable(width=True, height=True)
        self.janela_history.protocol("WM_DELETE_WINDOW", self.janela_history.withdraw)

        self.frame_hist = Frame(self.janela_history, bg=bg_color)
        self.frame_hist.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.lista_historico = ttk.Treeview(self.frame_hist, height=20, columns=("Cálculos",), show="headings")
        self.lista_historico.heading("Cálculos", text="Cálculos", anchor=CENTER)
        self.lista_historico.column("Cálculos", width=380, anchor=CENTER)
        self.lista_historico.place(relx=0.02, rely=0.02, relwidth=0.94, relheight=0.96)

        self.scrollHist = Scrollbar(self.frame_hist, orient="vertical", command=self.lista_historico.yview)
        self.lista_historico.configure(yscrollcommand=self.scrollHist.set)
        self.scrollHist.place(relx=0.94, rely=0.02, relwidth=0.06, relheight=0.96)

        self.janela_history.withdraw()

    def carregar_historico(self):
        for item in self.lista_historico.get_children():
            self.lista_historico.delete(item)
        try:
            with open("historico.txt", "r") as ficheiro:
                for linha in ficheiro:
                    self.lista_historico.insert("", "end", values=(linha.strip(),))
        except FileNotFoundError:
            pass

    def adicionar_calculo(self, expressao):
        with open("historico.txt", "a") as ficheiro:
            ficheiro.write(expressao + "\n")
        self.carregar_historico()


class GUI:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Super Calculadora")
        self.janela.config(bg=bg_color)
        self.janela.geometry("500x600")
        self.janela.resizable(width=True, height=True)
        self.janela.maxsize(width=700, height=800)
        self.janela.minsize(width=500, height=600)

        self.showValue = StringVar(self.janela)
        self.values = ''
        self.operador = None
        self.operando1 = None
        self.modo = "basica"  # modos: basica, trig, num, frac
        self.angulo_var = StringVar(value="deg")  # rad ou deg para trigonometria

        self.historico = Historico(self.janela)

        # Frames
        self.frame_top = Frame(self.janela, bg=bg_color, highlightbackground="#FFFFFF", highlightthickness=2)
        self.frame_top.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)
        self.frame_bottom = Frame(self.janela, bg=bg_color, highlightbackground="#FFFFFF", highlightthickness=2)
        self.frame_bottom.place(relx=0.02, rely=0.14, relwidth=0.96, relheight=0.84)
        self.frame_buttons = Frame(self.frame_bottom, bg=bg_color)
        self.frame_buttons.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        # Label
        self.label = Label(self.frame_top, textvariable=self.showValue, bg=bg_color, fg=txt_color,
                           font=("Comic Sans MS", 24, "bold"), anchor=E)
        self.label.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.8)

        # Checkboxes
        self.frame_checks = Frame(self.frame_bottom, bg=bg_color)
        self.frame_checks.place(relx=0.02, rely=0, relwidth=0.74, relheight=0.2)
        self.trigonometria_var = BooleanVar()
        self.numeroTeoria_var = BooleanVar()
        self.fracoes_var = BooleanVar()
        self.historico_var = BooleanVar()
        Checkbutton(self.frame_checks, text="Trigonometria", variable=self.trigonometria_var,
                    command=lambda: self.mudar_modo("trig"), bg=bg_color, fg=txt_color,
                    selectcolor=bt_bg_color).pack(anchor=W)
        Checkbutton(self.frame_checks, text="Número Teoria", variable=self.numeroTeoria_var,
                    command=lambda: self.mudar_modo("num"), bg=bg_color, fg=txt_color,
                    selectcolor=bt_bg_color).pack(anchor=W)
        Checkbutton(self.frame_checks, text="Frações", variable=self.fracoes_var,
                    command=lambda: self.mudar_modo("frac"), bg=bg_color, fg=txt_color,
                    selectcolor=bt_bg_color).pack(anchor=W)
        Checkbutton(self.frame_checks, text="Histórico", variable=self.historico_var,
                    command=self.abrir_historico, bg=bg_color, fg=txt_color,
                    selectcolor=bt_bg_color).pack(anchor=W)

        self.botoes_ativos = []
        self.desenhar_botoes()

        self.janela.mainloop()

    def abrir_historico(self):
        if self.historico_var.get():
            self.historico.carregar_historico()
            self.historico.janela_history.deiconify()
        else:
            self.historico.janela_history.withdraw()

    def mudar_modo(self, modo):
        if self.modo == modo:
            # já está no modo, desmarcar e voltar para basica
            self.modo = "basica"
            self.trigonometria_var.set(False)
            self.numeroTeoria_var.set(False)
            self.fracoes_var.set(False)
        else:
            self.modo = modo
            self.trigonometria_var.set(modo == "trig")
            self.numeroTeoria_var.set(modo == "num")
            self.fracoes_var.set(modo == "frac")
        self.desenhar_botoes()

    def limpar_botoes(self):
        for b in self.botoes_ativos:
            b.destroy()
        self.botoes_ativos.clear()

    def desenhar_botoes(self):
        self.limpar_botoes()
        if self.modo == "basica":
            self.desenhar_basica()
        elif self.modo == "trig":
            self.desenhar_trig()
        elif self.modo == "num":
            self.desenhar_num()
        elif self.modo == "frac":
            self.desenhar_frac()

    # --------------------- Modos ---------------------
    def desenhar_basica(self):
        # Números
        for n, (x, y) in zip(range(1, 10),
                              [(0.12, 0.55), (0.34, 0.55), (0.56, 0.55),
                               (0.12, 0.65), (0.34, 0.65), (0.56, 0.65),
                               (0.12, 0.75), (0.34, 0.75), (0.56, 0.75)]):
            btn = Button(self.frame_buttons, text=str(n), bg=bt_bg_color, fg=txt_color, font=txt_font,
                         command=lambda t=str(n): self.inputValue(t))
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)
        # Zero e ponto
        btn0 = Button(self.frame_buttons, text="0", bg=bt_bg_color, fg=txt_color, font=txt_font,
                      command=lambda: self.inputValue("0"))
        btn0.place(relx=0.34, rely=0.88, relwidth=0.2, relheight=0.1)
        btnp = Button(self.frame_buttons, text=".", bg=bt_bg_color, fg=txt_color, font=txt_font,
                      command=lambda: self.inputValue("."))
        btnp.place(relx=0.56, rely=0.88, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.extend([btn0, btnp])

        # Operadores
        for op, x, y in [('+', 0.78, 0.75), ('-', 0.78, 0.65), ('*', 0.78, 0.55), ('÷', 0.78, 0.45), ('v', 0.78, 0.35)]:
            btn = Button(self.frame_buttons, text=op, bg=bt_bg_color, fg=txt_color, font=txt_font,
                         command=lambda o=op: self.set_operador(o))
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)

        # C, ⌫, =
        btnc = Button(self.frame_buttons, text="C", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.clean)
        btnc.place(relx=0.02, rely=0.88, relwidth=0.3, relheight=0.1)
        btnb = Button(self.frame_buttons, text="⌫", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.apagar)
        btnb.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.1)
        btne = Button(self.frame_buttons, text="=", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.calculate)
        btne.place(relx=0.78, rely=0.88, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.extend([btnc, btnb, btne])

    def desenhar_trig(self):
        # Radiobutton graus/rad
        Label(self.frame_buttons, text="Ângulo:", bg=bg_color, fg=txt_color).place(relx=0.02, rely=0, relwidth=0.2, relheight=0.1)
        R1 = Radiobutton(self.frame_buttons, text="°", variable=self.angulo_var, value="deg", bg=bg_color, fg=txt_color)
        R1.place(relx=0.24, rely=0, relwidth=0.1, relheight=0.1)
        R2 = Radiobutton(self.frame_buttons, text="rad", variable=self.angulo_var, value="rad", bg=bg_color, fg=txt_color)
        R2.place(relx=0.36, rely=0, relwidth=0.15, relheight=0.1)

        # Botões trigonometria (mantendo layout original mas adicionando arcs)
        trig_funcs = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']
        positions = [(0.12, 0.40), (0.34, 0.40), (0.56, 0.40),
                     (0.12, 0.30), (0.34, 0.30), (0.56, 0.30)]
        for f, (x, y) in zip(trig_funcs, positions):
            btn = Button(self.frame_buttons, text=f, bg=bt_bg_color, fg=txt_color, font=txt_font,
                         command=lambda func=f: self.func_trig(func))
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)
        # Números
        for n, (x, y) in zip(range(1, 10), [(0.12, 0.50), (0.34, 0.50), (0.56, 0.50), (0.12, 0.60), (0.34, 0.60),
                                            (0.56, 0.60), (0.12, 0.70), (0.34, 0.70), (0.56, 0.70)]):
            btn = Button(self.frame_buttons, text=str(n), bg=bt_bg_color, fg=txt_color, font=txt_font,
                         command=lambda t=str(n): self.inputValue(t))
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)

        btn0 = Button(self.frame_buttons, text="0", bg=bt_bg_color, fg=txt_color, font=txt_font,
                      command=lambda: self.inputValue("0"))
        btn0.place(relx=0.34, rely=0.82, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.append(btn0)
        btnc = Button(self.frame_buttons, text="C", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.clean)
        btnc.place(relx=0.02, rely=0.82, relwidth=0.2, relheight=0.1)
        btnb = Button(self.frame_buttons, text="⌫", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.apagar)
        btnb.place(relx=0.56, rely=0.82, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.extend([btnc, btnb])

    def desenhar_num(self):
        # Botões Número Teoria
        funcoes = [("Divisores", self.divisores_numero),
                   ("Primo?", self.numero_primo),
                   ("Fatorial", self.fatorial_numero),
                   ("MDC", self.mdc_numero),
                   ("MMC", self.mmc_numero)]
        for (text, cmd), (x, y) in zip(funcoes, [(0.12, 0.35), (0.34,0.35),(0.56,0.35),(0.12,0.45),(0.34,0.45)]):
            btn = Button(self.frame_buttons, text=text, bg=bt_bg_color, fg=txt_color, font=txt_font, command=cmd)
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)
        # Números para input
        for n, (x, y) in zip(range(1,10), [(0.12,0.55),(0.34,0.55),(0.56,0.55),(0.12,0.65),(0.34,0.65),(0.56,0.65),(0.12,0.75),(0.34,0.75),(0.56,0.75)]):
            btn = Button(self.frame_buttons, text=str(n), bg=bt_bg_color, fg=txt_color, font=txt_font,
                         command=lambda t=str(n): self.inputValue(t))
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)
        btn0 = Button(self.frame_buttons, text="0", bg=bt_bg_color, fg=txt_color, font=txt_font,
                      command=lambda: self.inputValue("0"))
        btn0.place(relx=0.34, rely=0.87, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.append(btn0)
        # Limpar
        btnc = Button(self.frame_buttons, text="C", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.clean)
        btnc.place(relx=0.02, rely=0.87, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.append(btnc)

    def desenhar_frac(self):
        for n, (x, y) in zip(range(1, 10),
                              [(0.12, 0.55), (0.34, 0.55), (0.56, 0.55),
                               (0.12, 0.65), (0.34, 0.65), (0.56, 0.65),
                               (0.12, 0.75), (0.34, 0.75), (0.56, 0.75)]):
            btn = Button(self.frame_buttons, text=str(n), bg=bt_bg_color, fg=txt_color, font=txt_font,
                         command=lambda t=str(n): self.inputValue(t))
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)
        # Zero e barra para frações
        btn0 = Button(self.frame_buttons, text="0", bg=bt_bg_color, fg=txt_color, font=txt_font,
                      command=lambda: self.inputValue("0"))
        btn0.place(relx=0.34, rely=0.88, relwidth=0.2, relheight=0.1)
        btnp = Button(self.frame_buttons, text="/", bg=bt_bg_color, fg=txt_color, font=txt_font,
                      command=lambda: self.inputValue("/"))
        btnp.place(relx=0.56, rely=0.88, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.extend([btn0, btnp])
        
        # Operações frações (mantivemos aparência igual)
        for op, x, y in [('+', 0.78, 0.75), ('-', 0.78, 0.65), ('*', 0.78, 0.55), ('÷', 0.78, 0.45)]:
            btn = Button(self.frame_buttons, text=op, bg=bt_bg_color, fg=txt_color, font=txt_font,
                         command=lambda o=op: self.set_operador(o))
            btn.place(relx=x, rely=y, relwidth=0.2, relheight=0.1)
            self.botoes_ativos.append(btn)
        
        # C, ⌫, =
        btnc = Button(self.frame_buttons, text="C", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.clean)
        btnc.place(relx=0.02, rely=0.88, relwidth=0.3, relheight=0.1)
        btnb = Button(self.frame_buttons, text="⌫", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.apagar)
        btnb.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.1)
        btne = Button(self.frame_buttons, text="=", bg=bt_bg_color, fg=txt_color, font=txt_font, command=self.calculate)
        btne.place(relx=0.78, rely=0.88, relwidth=0.2, relheight=0.1)
        self.botoes_ativos.extend([btnc, btnb, btne])

    # --------------------- Funções ---------------------
    def inputValue(self, val):
        self.values += val
        self.showValue.set(self.values)

    def clean(self):
        self.values = ''
        self.showValue.set('')

    def apagar(self):
        self.values = self.values[:-1]
        self.showValue.set(self.values)

    def set_operador(self, op):
        if op == '÷':
            self.values += '/'
        else:
            self.values += op
        self.showValue.set(self.values)

    # ---------- Helper: parse two numbers and operator ----------
    def _parse_two_operands(self, expr):
        """
        Parse expression like '12.3+4.5' or '3/4' (for frac mode we handle separately).
        Returns (n1, op, n2) where n1/n2 are floats (or strings for fractions).
        """
        # Try to find operator + - * / not within a fraction (fractions use '/'; for fractions mode we won't call this)
        match = re.search(r'([-]?\d*\.?\d+)\s*([\+\-\*\/])\s*([-]?\d*\.?\d+)$', expr)
        if not match:
            return None
        n1_s, op, n2_s = match.group(1), match.group(2), match.group(3)
        return float(n1_s), op, float(n2_s)

    def calculate(self):
        """
        Replace eval: depending on mode, use appropriate classes from calculadora.py
        - basica: CalculadoraRegistada (soma, subtrair, multiplicar, dividir, raiz 'v', potencia '^' not supported by buttons)
        - frac: CalculadoraFracoes
        """
        try:
            expr = self.values.strip()

            if self.modo == "frac":
                # We expect expressions like "a/b + c/d" or "a/b" for simplify.
                # First, if '=' not used here, parse operator among + - * /
                # Split by + - * / but preserve fraction slashes.
                # We'll find the main operator using regex that finds operator not between digits and '/'
                # Simpler approach: search for + or * or - (binary) that is not part of fraction 'a/b'
                # We'll try to find one operator outside fraction parts:
                op_match = re.search(r'(?P<f1>[-]?\d+/\d+)\s*(?P<op>[\+\-\*\/])\s*(?P<f2>[-]?\d+/\d+)$', expr)
                if op_match:
                    f1 = Fraction(op_match.group('f1'))
                    f2 = Fraction(op_match.group('f2'))
                    op = op_match.group('op')
                    calc = CalculadoraFracoes(f1, f2)
                    if op == '+':
                        res = calc.soma_frac()
                    elif op == '-':
                        res = calc.sub_frac()
                    elif op == '*':
                        res = calc.mult_frac()
                    elif op == '/':
                        res = calc.div_frac()
                    else:
                        raise ValueError("Operador inválido")
                else:
                    # Maybe the user entered a single fraction to simplify: "a/b"
                    frac_match = re.match(r'^\s*([-]?\d+/\d+)\s*$', expr)
                    if frac_match:
                        f = Fraction(frac_match.group(1))
                        calc = CalculadoraFracoes(f, 1)
                        res = calc.simplificar()
                    else:
                        # Try mixed: numbers without slash -> treat as Fraction(n,1)
                        # fallback: attempt to split by + - * /
                        m = re.search(r'(?P<n1>[-]?\d*\.?\d+)\s*(?P<op>[\+\-\*\/])\s*(?P<n2>[-]?\d*\.?\d+)$', expr)
                        if m:
                            n1 = Fraction(m.group('n1'))
                            n2 = Fraction(m.group('n2'))
                            op = m.group('op')
                            calc = CalculadoraFracoes(n1, n2)
                            if op == '+':
                                res = calc.soma_frac()
                            elif op == '-':
                                res = calc.sub_frac()
                            elif op == '*':
                                res = calc.mult_frac()
                            elif op == '/':
                                res = calc.div_frac()
                            else:
                                raise ValueError("Operador inválido")
                        else:
                            raise ValueError("Entrada de fração inválida")
                self.showValue.set(str(res))
                self.historico.adicionar_calculo(f"{self.values} = {res}")
                self.values = str(res)
                return

            # modo basica ou outros: parse using regex for basic binary ops or raiz 'v'
            # handle raiz 'v' notation: e.g. '9v2' in your original code represented as raiz_n (n1 **(1/n2))
            if 'v' in expr:
                # expect format n1 v n2
                m = re.match(r'^\s*([-]?\d*\.?\d+)\s*v\s*([-]?\d*\.?\d+)\s*$', expr)
                if m:
                    n1 = float(m.group(1)); n2 = float(m.group(2))
                    calc = CalculadoraRegistada(n1, n2)
                    calc.resultado = calc.raiz_n()  # uses base class raiz_n
                    res = calc.resultado
                    # registrar
                    calc.registarNormal("v")
                    self.showValue.set(str(res))
                    self.historico.adicionar_calculo(f"{self.values} = {res}")
                    self.values = str(res)
                    return
                else:
                    raise ValueError("Formato raiz inválido")

            parsed = self._parse_two_operands(expr)
            if not parsed:
                raise ValueError("Expressão inválida")
            n1, op, n2 = parsed
            calc = CalculadoraRegistada(n1, n2)
            if op == '+':
                res = calc.soma()
            elif op == '-':
                res = calc.menos()
            elif op == '*':
                res = calc.vezes()
            elif op == '/':
                res = calc.divide()
            else:
                raise ValueError("Operador desconhecido")

            self.showValue.set(str(res))
            self.historico.adicionar_calculo(f"{self.values} = {res}")
            self.values = str(res)
        except ZeroDivisionError:
            self.showValue.set("Erro: divisão por zero")
            self.values = ''
        except Exception:
            # fallback genérico
            self.showValue.set("Erro")
            self.values = ''

    # --------------------- Trigonometria ---------------------
    def func_trig(self, func):
        try:
            # Usa o modo atual selecionado nos radiobuttons
            modo_atual = self.angulo_var.get()  # "deg" ou "rad"

            # Obtem o valor atual do display
            val_str = self.showValue.get() if self.showValue.get() != '' else self.values
            if val_str in ('', None):
                n_raw = 0.0
            else:
                n_raw = float(val_str)

            # Cria a calculadora trigonométrica com o modo atual
            calc = CalculadoraTrigonometrica(n_raw, modo_angulos='graus' if modo_atual == 'deg' else 'radianos', tipo=modo_atual)

            # Converte entrada para radianos se o modo atual for graus (exceto para arcs)
            if modo_atual == 'deg' and func in ('sin', 'cos', 'tan'):
                n_input = math.radians(n_raw)
            else:
                n_input = n_raw

            # Executa a função correspondente
            if func == 'sin':
                res = math.sin(n_input)
            elif func == 'cos':
                res = math.cos(n_input)
            elif func == 'tan':
                res = math.tan(n_input)
            elif func == 'asin':
                res = math.asin(n_input)
                if modo_atual == 'deg':
                    res = math.degrees(res)
            elif func == 'acos':
                res = math.acos(n_input)
                if modo_atual == 'deg':
                    res = math.degrees(res)
            elif func == 'atan':
                res = math.atan(n_input)
                if modo_atual == 'deg':
                    res = math.degrees(res)
            else:
                raise ValueError("Função trig desconhecida")

            # Arredonda resultado e exibe
            display_res = round(res, 6)
            self.showValue.set(str(display_res))
            self.historico.adicionar_calculo(f"{func}({n_raw}{'°' if modo_atual == 'deg' else ' rad'}) = {display_res}")
            self.values = str(display_res)

        except ValueError:
            self.showValue.set("Erro domínio")
            self.values = ''
        except Exception:
            self.showValue.set("Erro")
            self.values = ''

    # --------------------- Número Teoria ---------------------
    def divisores_numero(self):
        try:
            n = int(self.values)
            divs = [str(i) for i in range(1, n+1) if n % i == 0]
            res = ", ".join(divs)
            self.showValue.set(res)
            self.historico.adicionar_calculo(f"Divisores({n}) = {res}")
            self.values = ''
        except:
            self.showValue.set("Erro")
            self.values = ''

    def numero_primo(self):
        try:
            n = int(self.values)
            primo = n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
            self.showValue.set(str(primo))
            self.historico.adicionar_calculo(f"Primo({n}) = {primo}")
            # usar a classe para registar
            try:
                calc = CalculadoraNumeroTeoria(n, 0)
                calc.resgistarIfPrimo()
            except:
                pass
            self.values = ''
        except:
            self.showValue.set("Erro")
            self.values = ''

    def fatorial_numero(self):
        try:
            n = int(self.values)
            calc = CalculadoraRegistada(n, 0)
            res = calc.Fato()
            # calc.Fato já registra o fatorial
            self.showValue.set(str(res))
            # também adiciona ao histórico via historico.adicionar_calculo, por segurança
            self.historico.adicionar_calculo(f"{n}! = {res}")
            self.values = ''
        except:
            self.showValue.set("Erro")
            self.values = ''

    def mdc_numero(self):
        try:
            nums = list(map(int, self.values.split(",")))
            if len(nums) < 2:
                raise ValueError("Precisa de 2 ou mais números")
            # usar CalculadoraNumeroTeoria
            calc = CalculadoraNumeroTeoria(nums[0], nums[1])
            res = calc.mdc() if len(nums) == 2 else math.gcd(*nums)  # calc.mdc usa apenas 2
            self.showValue.set(str(res))
            self.historico.adicionar_calculo(f"MDC({self.values}) = {res}")
            self.values = ''
        except:
            self.showValue.set("Erro")
            self.values = ''

    def mmc_numero(self):
        try:
            nums = list(map(int, self.values.split(",")))
            if len(nums) < 2:
                raise ValueError("Precisa de 2 ou mais números")
            # usar a função mmc da classe para os dois primeiros, iterar para o resto
            res = nums[0]
            for n in nums[1:]:
                # usa o lcm da biblioteca math se disponível (py3.9+), mas para consistência, usamos a classe
                res = lcm(res, n) if 'lcm' in globals() else abs(res * n) // math.gcd(res, n)
            self.showValue.set(str(res))
            self.historico.adicionar_calculo(f"MMC({self.values}) = {res}")
            self.values = ''
        except:
            self.showValue.set("Erro")
            self.values = ''

    # --------------------- Frações ---------------------
    # No teu design original, os métodos de frações não recebiam parâmetros — vamos extrair self.values
    def soma_fracao(self):
        try:
            # espera algo como "a/b+c/d" ou "a/b + c/d" ou "n1/n2"
            expr = self.values.replace(" ", "")
            # buscar operador principal (+ - * /) que não seja o slash de fração
            m = re.search(r'(?P<f1>-?\d+/\d+)\s*(?P<op>[\+\-\*\/])\s*(?P<f2>-?\d+/\d+)', expr)
            if not m:
                raise ValueError("Entrada de fração inválida")
            f1 = Fraction(m.group('f1'))
            f2 = Fraction(m.group('f2'))
            calc = CalculadoraFracoes(f1, f2)
            res = calc.soma_frac()
            self.showValue.set(str(res))
            self.historico.adicionar_calculo(f"{f1} + {f2} = {res}")
            self.values = str(res)
        except:
            self.showValue.set("Erro")
            self.values = ''

    def sub_frac(self):
        try:
            expr = self.values.replace(" ", "")
            m = re.search(r'(?P<f1>-?\d+/\d+)\s*\-\s*(?P<f2>-?\d+/\d+)', expr)
            if not m:
                raise ValueError("Entrada inválida")
            f1 = Fraction(m.group('f1'))
            f2 = Fraction(m.group('f2'))
            calc = CalculadoraFracoes(f1, f2)
            res = calc.sub_frac()
            self.showValue.set(str(res))
            self.historico.adicionar_calculo(f"{f1} - {f2} = {res}")
            self.values = str(res)
        except:
            self.showValue.set("Erro")
            self.values = ''

    def mult_frac(self):
        try:
            expr = self.values.replace(" ", "")
            m = re.search(r'(?P<f1>-?\d+/\d+)\s*\*\s*(?P<f2>-?\d+/\d+)', expr)
            if not m:
                raise ValueError("Entrada inválida")
            f1 = Fraction(m.group('f1'))
            f2 = Fraction(m.group('f2'))
            calc = CalculadoraFracoes(f1, f2)
            res = calc.mult_frac()
            self.showValue.set(str(res))
            self.historico.adicionar_calculo(f"{f1} * {f2} = {res}")
            self.values = str(res)
        except:
            self.showValue.set("Erro")
            self.values = ''

    def div_frac(self):
        try:
            expr = self.values.replace(" ", "")
            m = re.search(r'(?P<f1>-?\d+/\d+)\s*\/\s*(?P<f2>-?\d+/\d+)', expr)
            if not m:
                raise ValueError("Entrada inválida")
            f1 = Fraction(m.group('f1'))
            f2 = Fraction(m.group('f2'))
            calc = CalculadoraFracoes(f1, f2)
            res = calc.div_frac()
            self.showValue.set(str(res))
            self.historico.adicionar_calculo(f"{f1} / {f2} = {res}")
            self.values = str(res)
        except ZeroDivisionError:
            self.showValue.set("Erro: divisão por zero")
            self.values = ''
        except:
            self.showValue.set("Erro")
            self.values = ''

    def simpl_frac(self):
        try:
            expr = self.values.strip()
            # aceitar "a/b" ou inteiro
            if '/' in expr:
                f = Fraction(expr)
                calc = CalculadoraFracoes(f, 1)
                res = calc.simplificar()
                self.showValue.set(str(res))
                self.historico.adicionar_calculo(f"Simpl({f}) = {res}")
                self.values = str(res)
            else:
                # se apenas um número, converte para fraction e simplifica (sem mudança)
                f = Fraction(expr)
                calc = CalculadoraFracoes(f, 1)
                res = calc.simplificar()
                self.showValue.set(str(res))
                self.historico.adicionar_calculo(f"Simpl({f}) = {res}")
                self.values = str(res)
        except:
            self.showValue.set("Erro")
            self.values = ''


if __name__ == "__main__":
    GUI()

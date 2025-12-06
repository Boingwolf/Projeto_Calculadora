import os
from  math import factorial, exp, gcd, lcm, sin, cos, tan, asin, acos, atan, radians, degrees
from fractions import Fraction
from pathlib import Path

#**********************************************
historico = []
caminho = Path('historico.txt')
#**********************************************

class Calculadora:
    def __init__(self, n1, n2):
        self.resultado = 0
        self.n1 = n1
        self.n2 = n2

    def adicionar(self):
        self.resultado = self.n1 + self.n2
        return self.resultado

    def subtrair(self):
        self.resultado = self.n1 - self.n2
        return self.resultado

    def multiplicar(self):
        self.resultado = self.n1 * self.n2
        return self.resultado

    def dividir(self):
        if self.n2 != 0:
            self.resultado = self.n1 / self.n2
        else:
            raise ZeroDivisionError
        return self.resultado
    
    def raiz_n(self):
        self.resultado = self.n1 ** (1/self.n2)
        return self.resultado
    
    def exponencial(self):
        self.resultado = exp(self.n1)
        print(f"e ** {self.n1} = {self.resultado}")
        return self.resultado
    
    def potencia(self):
        self.resultado = self.n1 ** self.n2
        return self.resultado
            
    def fatorial(self):
        self.resultado = factorial(self.n1)
        return self.resultado

    def arredondar_para(self):
        self.resultado = round(self.n1, self.n2)
        print(f"{self.n1} arredondado para {self.n2} casas decimais é igual a: {self.resultado}")
        return self.resultado
    
    def modulo(self):
        self.resultado = abs(self.n1)
        return self.resultado

    def limpar(self):
        if self.resultado == str(self.resultado):
            self.resultado = ''
        self.resultado = 0
        return self.resultado
    

class CalculadoraRegistada(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
    
    def registarNormal(self, operador: str):
        entrada = f"{self.n1} {operador} {self.n2} = {self.resultado}"
        #historico.append(entrada)
        # Anexa ao ficheiro em vez de sobrescrever
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def registarFat(self):
        entrada = f"{self.n1}! = {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
        
    def registarExp(self):
        entrada = f"e ** {self.n1} = {self.resultado}"  # Corrigido: usa self.n1
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def registarArredonda(self):
        entrada = f"{self.n1} arredondado para {self.n2} = {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def registarModulo(self):
        entrada = f"O modulo de {self.n1} = {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def resgistarIfPrimo(self):
        if CalculadoraNumeroTeoria(self.n1, 0).numero_primo():
            self.resultado = 'Primo'
        else:
            self.resultado = 'Não Primo'
        entrada = f"{int(self.n1)} = {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def resgistarProxPrimo(self):
        entrada = f"O proximo primo de {self.n1} = {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def resgistarMdc(self):
        entrada = f"O MDC de {int(self.n1)} e {int(self.n2)} é {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
            
    def registarMmc(self):
        entrada = f"O Mmc de {self.n1} e {self.n2} é {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def registarSimplificada(self):
        entrada = f"A fração simplicada de {self.n1} = {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def registrar_trig(self, operacao):
        entrada = f"{operacao}({self.n1}) = {self.resultado}"
        historico.append(entrada)
        with caminho.open('a') as f:
            f.write(entrada + '\n')
    
    def soma(self):
        self.resultado = super().adicionar()
        self.registarNormal("+")
        return self.resultado    
    
    def menos(self):
        self.resultado = super().subtrair()
        self.registarNormal("-")
        return self.resultado
    
    def vezes(self):
        self.resultado = super().multiplicar()
        self.registarNormal("*")
        return self.resultado  
    
    def divide(self):
        self.resultado = super().dividir()
        self.registarNormal("/")
        return self.resultado   
    
    def raiz(self):
        self.resultado = super().raiz_n()
        self.registarNormal("v")
        return self.resultado   
    
    def Expe(self):
        self.resultado = super().exponencial()
        self.registarExp()
        return self.resultado   
    
    def Fato(self):
        self.resultado = super().fatorial()
        self.registarFat()
        return self.resultado   
    
    def Arredonda(self):
        self.resultado = super().arredondar_para()
        self.registarArredonda()
        return self.resultado   
    
class CalculadoraNumeroTeoria(CalculadoraRegistada):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        
    def numero_primo(self): 
        if self.n1 <= 1:
            return False
        for i in range(2, int(self.n1)):
            if self.n1 % i == 0:
                return False
        return True

    def proximo_primo(self):
        if self.n1 < 2:
            return 2
        
        while not CalculadoraNumeroTeoria(int(self.n1), 0).numero_primo():
            self.n1 += 1
        
        self.resultado = self.n1
        return self.resultado
    
    def mdc(self):
        self.resultado = gcd(self.n1, self.n2)
        self.resgistarMdc()
        return self.resultado
    
    def mmc(self):
        self.resultado = lcm(self.n1, self.n2)
        self.registarMmc()
        return self.resultado

class CalculadoraInteira(CalculadoraRegistada):
    
    def __init__(self, n1, n2):
        super().__init__(int(n1), int(n2))
        
    def somaint(self):
        self.resultado = super().soma()
        return self.resultado
    def subint(self):
        self.resultado = super().menos()
        return self.resultado
    def multint(self):
        self.resultado = super().vezes()
        return self.resultado
    def divint(self):
        self.resultado = super().divide()
        return self.resultado
    def Expeint(self):
        self.resultado = super().Expe()
        return self.resultado
    def Fatoint(self):
        self.resultado = super().Fato()
        return self.resultado

class CalculadoraFracoes(CalculadoraRegistada): 
    def __init__(self, n1, n2):
        try:
            # Permitir "1/2", "3.5" ou números inteiros
            self.n1 = Fraction(str(n1))
            self.n2 = Fraction(str(n2))
        except ValueError:
            raise ValueError("Os valores devem ser números ou frações válidas (ex: 1/2, 3/4, 2.5)")
        super().__init__(self.n1, self.n2)
    
    def soma_frac(self):
        self.resultado = self.n1 + self.n2
        self.registarNormal("+")
        return self.resultado
    
    def sub_frac(self):
        self.resultado = self.n1 - self.n2
        self.registarNormal("-")
        return self.resultado
    
    def mult_frac(self):
        self.resultado = self.n1 * self.n2
        self.registarNormal("*")
        return self.resultado
    
    def div_frac(self):
        if self.n2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        self.resultado = self.n1 / self.n2
        self.registarNormal("/")
        return self.resultado
    
    def simplificar(self):
        """Simplifica uma fração qualquer"""
        self.resultado = Fraction(self.n1)
        self.registarSimplificada()
        return self.resultado
    
class CalculadoraTrigonometrica(CalculadoraRegistada):
    def __init__(self, n1, modo_angulos='rad', tipo='graus'):
        super().__init__(n1, 0)
        self.modo_angulos = modo_angulos
        self.tipo = tipo

    def _converter_para_radianos(self):
        self.tipo = 'rad'
        return radians(self.n1) if self.modo_angulos == 'graus' else self.n1

    def _converter_para_graus(self):
        self.tipo = 'graus'
        return degrees(self.n1) if self.modo_angulos == 'graus' else self.n1
    
    def seno(self):
        self.resultado = sin(self.n1)
        if self.tipo == 'graus':
            self.registrar_trig("Tipo Graus: seno")
        else:
            self.registrar_trig("Tipo Radianos: seno")
        return self.resultado
    
    def cosseno(self):
        self.resultado = cos(self.n1)
        if self.tipo == 'graus':
            self.registrar_trig("Tipo Graus: cosseno")
        else:
            self.registrar_trig("Tipo Radianos: cosseno")
        return self.resultado
    
    def tangente(self):
        self.resultado = tan(self.n1)
        if self.tipo == 'graus':
            self.registrar_trig("Tipo Graus: tangente")
        else:
            self.registrar_trig("Tipo Radianos: tangente")
        return self.resultado
    
    def arco_seno(self):
        if not -1 <= self.n1 <= 1:
            raise ValueError("arco_seno(x) indefinido para |x| > 1")
        self.resultado = asin(self.n1)
        if self.tipo == 'graus':
            self.registrar_trig("Tipo Graus: arco seno")
        else:
            self.registrar_trig("Tipo Radianos: arco seno")
        return self.resultado
    
    def arco_cosseno(self):
        if not -1 <= self.n1 <= 1:
            raise ValueError("arco_cosseno(x) indefinido para |x| > 1")
        self.resultado = acos(self.n1)
        if self.tipo == 'graus':
            self.registrar_trig("Tipo Graus: arco cosseno")
        else:
            self.registrar_trig("Tipo Radianos: arco cosseno")
        return self.resultado
    
    def arco_tan(self):
        self.resultado = atan(self.n1)
        if self.tipo == 'graus':
            self.registrar_trig("Tipo Graus: arco tangente")
        else:
            self.registrar_trig("Tipo Radianos: arco tangente")
        return self.resultado
    

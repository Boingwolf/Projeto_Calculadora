import os
from calculadora import *

if __name__ == "__main__":
    continuar = True
    while continuar:
        op1 = None
        op2 = None
        os.system('cls')
            
        op1 = int(input("\nEscolha a Calculadora que deseja utilizar:\n1 - Números Reais\n2 - Números Inteiros\n3 - Números Teoria\n4 - Trigonometria\n5 - Frações\n6 - Histórico\n\tOpção: "))
        match op1:  
            case 1: #Numeros Reais
                os.system('cls')
                try:
                    conta = float(input("Digite o primeiro número: "))
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro.")
                    input("\nPressione Enter para continuar...")
                    continue
                try:
                    op2 = input("\nEscolha a operação:\n+ - Adição\n- - Subtração\n* - Multiplicação\n/ - Divisão\nv - Raiz nésima\ne - Exponencial\n! - Fatorial\n** - Potência\nm - Modulo\nA - Arredondar\n\tOpção: ").strip()
                except ValueError:
                    print("Entrada inválida. Por favor, escolha uma op2ração válida.")
                    input("\nPressione Enter para continuar...")
                    continue
                op2map = {'1': '+', '2': '-', '3': '*', '4': '/', '5': 'v', '6': '**', '7': '!', '8': '||', '9': 'm', '0': 'A'}
                if op2 in op2map:
                    op2= op2map[op2]
                if op2 in ['+', '-', '*', '/', 'v', '**']:
                    try:
                        conta2 = float(input("Digite o segundo número: "))
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número inteiro.")
                        input("\nPressione Enter para continuar...")
                        continue
                    calc = CalculadoraRegistada(conta, conta2)
                match op2:
                    case '+':
                        print(f"{conta} + {conta2} = {calc.soma()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case '-':
                        print(f"{conta} - {conta2} = {calc.menos()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case '*':
                        print(f"{conta} * {conta2} = {calc.vezes()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case '/':
                        print(f"{conta} / {conta2} = {calc.divide()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case 'v':
                        print(f"{conta} v {conta2} = {calc.raiz()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case 'e':
                        CalculadoraRegistada(conta, 0).Expe()
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case '!':
                        CalculadoraRegistada(int(conta),0).Fato()
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case '||':
                        CalculadoraRegistada(conta, 0).modulo()
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case '**':
                        print(f"{conta} ** {conta2} = {calc.potencia()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case 'm', 'M':
                        print(f"O modulo de {conta} = {CalculadoraRegistada(conta, 0).modulo()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case 'A', 'a':
                        try:
                            casa_decimal = int(input("Digite o número de casas decimais: "))
                            calc = CalculadoraRegistada(conta, casa_decimal)
                            calc.Arredonda()
                            if input("\nDeseja continuar? (S/N): ").lower() == "n":
                                continuar = False
                        except ValueError:
                            print("Entrada inválida para casas decimais.")
                            input("\nPressione Enter para continuar...")
                    case _:
                        print("Operação inválida.")
                        input("\nPressione Enter para continuar...")
                    
            case 2: #Numeros Inteiros
                os.system('cls')
                try:
                    conta = int(input("Digite o primeiro número: "))
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro.")
                    input("\nPressione Enter para continuar...")
                    continue
                try:
                    op2= input("\nEscolha a operação:\n+ - Adição\n- - Subtração\n* - Multiplicação\n// - Divisão\ne - Exponencial\n! - Fatorial\n** - Potência\n\tOpção: ").strip()
                except ValueError:
                    print("Entrada inválida. Por favor, escolha uma op2ração válida.")
                    input("\nPressione Enter para continuar...")
                    continue
                op2map = {'1': '+', '2': '-', '3': '*', '4': '//', '6': '**', '7': '!'}
                if op2 in op2map:
                    op2= op2map[op2]
                if op2 in ['+', '-', '*', '//', '**']:
                    try:
                        conta2 = int(input("Digite o segundo número: "))
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número inteiro.")
                        input("\nPressione Enter para continuar...")
                        continue
                    calc = CalculadoraInteira(conta, conta2)
                match op2:
                    case '+':
                        print(f"{conta} + {conta2} = {calc.somaint()}") # type: ignore
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case '-':
                        print(f"{conta} - {conta2} = {calc.subint()}") # type: ignore
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case '*':
                        print(f"{conta} * {conta2} = {calc.multint()}") # type: ignore
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case '//':
                        print(f"{conta} / {conta2} = {calc.divint()}") # type: ignore
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                            break
                    case 'e':
                        Calculadora(conta, 0).Expeint() # type: ignore
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case '!':
                        CalculadoraInteira(int(conta),0).Fatoint()
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case '**':
                        print(f"{conta} ** {conta2} = {calc.potencia()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case _:
                        print("Op2ração inválida.")
                        input("\nPressione Enter para continuar...")   
                
            case 3: #Numeros Teoria
                os.system('cls')
                op5 = int(input("\nEscolha a operação:\n1 - Verificar se é primo\n2 - Próximo primo\n3 - MDC\n4 - MMC\n\tOpção: "))
                try:
                    conta = float(input("Digite o primeiro número: "))
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro.")
                    input("\nPressione Enter para continuar...")
                    continue
                if op5 in [3, 4]:
                    try:
                        conta2 = float(input("Digite o segundo número: "))
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número inteiro.")
                        input("\nPressione Enter para continuar...")
                        continue
                    calc = CalculadoraRegistada(conta, conta2)
                match op5:
                    case 1: #Ver se é primo
                        CalculadoraRegistada(conta, 0).resgistarIfPrimo()
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case 2: #Proximo primo
                        CalculadoraRegistada(conta, 0).resgistarProxPrimo()
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case 3: #MDC
                        calc = CalculadoraNumeroTeoria(int(conta), int(conta2))
                        print(f"O MDC de {int(conta)} e {int(conta2)} é {calc.mdc()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
                    case 4: #MMC
                        calc = CalculadoraNumeroTeoria(int(conta), int(conta2))
                        print(f"O MMC de {int(conta)} e {int(conta2)} é {calc.mmc()}")
                        if input("\nDeseja continuar? (S/N): ").lower() == "n":
                            continuar = False
            
            case 4: #Trigonometria
                os.system('cls')
                try:
                    op_trig = int(input("\nEscolha a operação:\n1 - Seno\n2 - Cosseno\n3 - Tangente\n4 - ArcSin\n5 - ArcCos\n6 - ArcTan\n\tOpção: "))
                except ValueError:
                    print("Opção inválida.")
                    input("\nPressione Enter para continuar...")
                    continue

                try:
                    valor = float(input("Digite o valor (ângulo): "))
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
                    input("\nPressione Enter para continuar...")
                    continue

                unidade = input("\nInforme a unidade de entrada: (G)raus ou (R)adianos [G/R]: ").strip().lower()
                if unidade not in ('g', 'r'):
                    unidade = 'g'

                # Para funções trigonométricas diretas, convertemos para radianos se o usuário informou graus
                if op_trig in (1, 2, 3):
                    if unidade == 'g':
                        n = radians(valor)
                        calc = CalculadoraTrigonometrica(n, modo_angulos='graus', tipo='graus')
                    else:
                        calc = CalculadoraTrigonometrica(valor, modo_angulos='rad', tipo='rad')

                    if op_trig == 1:
                        print(f"seno({valor}{'°' if unidade=='g' else ' rad'}) = {calc.seno()}")
                    elif op_trig == 2:
                        print(f"cosseno({valor}{'°' if unidade=='g' else ' rad'}) = {calc.cosseno()}")
                    elif op_trig == 3:
                        print(f"tangente({valor}{'°' if unidade=='g' else ' rad'}) = {calc.tangente()}")

                # Para arcos, a entrada é o valor da função (deve estar no domínio apropriado)
                elif op_trig in (4, 5, 6):
                    calc = CalculadoraTrigonometrica(valor, modo_angulos='rad', tipo='graus' if unidade == 'g' else 'rad')
                    try:
                        if op_trig == 4:
                            tipo = "arcsin"
                            res = calc.arco_seno()
                        elif op_trig == 5:
                            tipo = "arccos"
                            res = calc.arco_cosseno()
                        else:
                            tipo = "arctan"
                            res = calc.arco_tan()

                        # Se o usuário quer o resultado em graus, convertê-lo para apresentação
                        if unidade == 'g':
                            res_display = degrees(res)
                            # atualizar resultado também para histórico consistente
                            calc.resultado = res_display
                            print(f"{tipo}({valor}) = {res_display}°")
                        else:
                            print(f"{tipo}({valor}) = {res} rad")
                    except ValueError as e:
                        print(f"Erro: {e}")
                else:
                    print("Operação inválida.")

                if input("\nDeseja continuar? (S/N): ").lower() == "n":
                    continuar = False
                
            case 5: #Frações
                os.system('cls')
                try:
                    conta = input("Digite a primeira fração (ex: 1/2 ou 3): ")
                except ValueError as e:
                    print(f"Erro: {e}")
                    input("\nPressione Enter para continuar...")
                    continue

                op_frac = input("\nEscolha a operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Simplificar\n\tOpção: ").strip()
                
                if op_frac not in ['5']:
                    try:
                        conta2 = input("Digite a segunda fração (ex: 3/4 ou 2): ")
                    except ValueError as e:
                        print(f"Erro: {e}")
                        input("\nPressione Enter para continuar...")
                        continue
                else:
                    conta2 = 0
                calc = CalculadoraFracoes(conta, conta2)
                
                try:
                    match op_frac:
                        case '1':
                            print(f"{conta} + {conta2} = {calc.soma_frac()}")
                        case '2':
                            print(f"{conta} - {conta2} = {calc.sub_frac()}")
                        case '3':
                            print(f"{conta} * {conta2} = {calc.mult_frac()}")
                        case '4':
                            print(f"{conta} / {conta2} = {calc.div_frac()}")
                        case '5':
                            print(f"Simplificação de {conta} = {calc.simplificar()}")
                        case _:
                            print("Operação inválida.")
                except Exception as e:
                    print(f"Erro: {e}")

                if input("\nDeseja continuar? (S/N): ").lower() == "n":
                    continuar = False
                    
            case 6: #Historico
                os.system('cls')
                op4 = int(input("\nEscolha a operação:\n1 - Ver Histórico\n2 - Apagar Histórico\n\tOpção: "))
                match op4:
                    case 1:
                        print("____Histórico____")
                        if caminho.exists():
                            with caminho.open('r') as f:
                                print(f.read())
                        input("\nPressione Enter para continuar...")
                    case 2:
                        print("Histórico Apagado!!!")
                        input("\nPressione Enter para continuar...")
                        with caminho.open('w') as f:
                            pass
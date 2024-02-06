# Criador         : Brayan vieira 
# função          : realiza varios calculos de numeros inteiros 
# versão          : 2.1
# data da criação : 06/2/2024

#---------------------------------------------------------------------------------------------------
#                                   Variaveis e bibliotecas importadas
import math 
barras = 50 * "-"
ESPACO = 3 * "\n"
opçoes = ("s", "d", "m", "p", "rr", "dd")
MENU = "oque você deseja realizar ?  [s] soma | [d] divisão | [m] multiplicação | [p] potencia | [rr] raiz quadrada | [dd] divisão inteira  : "
#---------------------------------------------------------------------------------------------------
#                                   Menu e inicio da calculadora
while True:
    print(ESPACO)
    decisao1 = input("deseja entrar na calculadora ? [S] sim ou [N] não? : ").lower().startswith("s")
    print(barras)
    if not decisao1 :
        print("saindo do programa")
        break
#-------------------------------------------------------------------------------------------------
#                                  Escolha de calculo 
    else:
        print("\n" * 100)
        decisao2 = input(MENU).lower()
    if decisao2 not in opçoes:
        print(ESPACO)
        print(" Você inseriu um caracter invalido ")
        print(ESPACO)
        continue

#-------------------------------------------------------------------------------------------------
#                               calculo da Raiz quadrada 
    if decisao2 == "rr":
        print(ESPACO)
        raiz_num = int(input("insira o numero para ver a raiz quadrada : "))
        resul = math.sqrt(raiz_num)
        print(barras)
        print(f" a raiz de {raiz_num} e {resul:.2f}")
        print(barras)
        continue
#-------------------------------------------------------------------------------------------------
#                                   Calculo da potencia 
    if decisao2 == "p":
        print(ESPACO)
        potencia1 = int(input("insira o numero inteiro para a potencia : "))
        potencia2 = int(input("insira o numero da potencia : "))
        result = math.pow(potencia1, potencia2)
        print(barras)
        print(f"o resultado da potencia e : {result}")
        print(barras)
        continue
#-----------------------------------------------------------------------------------------------
#                                   Divisão inteira 
    if decisao2 == "dd":
        print(barras)
        divisao_int = int(input("insira o numero inteiro para dividir : "))
        print(barras)
        divisor_int = int(input("insira o divisor : "))
        total = divisao_int // divisor_int
        print(ESPACO)
        print(f"o resultado da divisão inteira e : {total} \n ")
        continue
#-----------------------------------------------------------------------------------------------
#                                      Possiveis erros
    total_input2 = len(decisao2)
    if total_input2 > 2:
        print("erro realize cada calculo apenas 1 vez")
        continue
    else : 
   
#------------------------------------------------------------------------------------------------
#                           Entrada de dados para o numero do calculo e mensagem de erro
        try:
            print(barras)
            num1 = int(input(f" insira um numero para continuar para o calculo  : "))
            print(barras)
            num2 = int(input(f" insira outro numero para continuar o calculo  : "))
            print(barras)
        except ValueError:
            print(barras)
            print("erro insira apenas numeros")
            print(barras)
            continue
#------------------------------------------------------------------------------------------------
#                                       ifs direcionados para Calculos 
        if decisao2 == "s":
            soma = num1 + num2
            print(f" o resultado da sua soma e : {soma}")
            print(barras)

        elif decisao2 == "d":
            divisao = num1 / num2

            print(f" o resulado da divisão e : {divisao} ")
            print(barras)

        elif decisao2 == "m":
            multiplicaçao = num1 * num2
            print(f" o resultado da multiplicação e : {multiplicaçao} ")
            print(barras)
#------------------------------------------------------------------------------------------------
#                                 mensagem de erro
        else:
            print("um erro ocorreu tente novamente : ")
            continue

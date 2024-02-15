# Criador         : Brayan vieira 
# função          : realiza varios calculos de numeros inteiros 
# versão          : 2.3
# data da criação : 06/2/2024
# Notas versão 2.2: estabilidade melhorado e mais rapidez função, case adicionada 
# Notas versão 2.3: melhor nitidez e usabilidade, trocados espacos pelo limpador de tela 
#---------------------------------------------------------------------------------------------------
#                                   Variaveis e bibliotecas importadas
import os
import math 
import platform
barras = 50 * "-"
ESPACO = 3 * "\n"
opçoes = ("s", "d", "m", "p", "rr", "dd")
#----------------------------------------------------------------------------------------------------
#                                   Função limpar a tela  
def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        limpador = "cls"
    elif sistema == "Linux":
        limpador = "clear"
    return os.system(limpador)
#---------------------------------------------------------------------------------------------------
#                                   Menu e inicio da calculadora
while True:
    decisao1 = input("deseja entrar na calculadora ? [S] sim ou [N] não? : ").lower().startswith("s")
    print(barras)
    if not decisao1 :
        print("saindo do programa")
        break
#-------------------------------------------------------------------------------------------------
#                                  Escolha de calculo 
    print("\n" * 100)
    decisao2 = input("oque você deseja realizar ? \n \n [s] soma | [d] divisão \n \n [m] multiplicação | [p] potencia \n \n [rr] raiz quadrada | [dd] divisão inteira  \n \n Insira : ").lower()
    limpar_tela()
    if decisao2 not in opçoes:
        limpar_tela()
        print(" Você inseriu um caracter invalido \n ")
        continue

#-------------------------------------------------------------------------------------------------
#                               calculo da Raiz quadrada 
    match decisao2:
        case "rr":
                print(ESPACO)
                raiz_num = int(input("insira o numero para ver a raiz quadrada : "))
                resul = math.sqrt(raiz_num)
                limpar_tela()
                print(f" a raiz de {raiz_num} e {resul:.2f} \n ")
                continue
#-------------------------------------------------------------------------------------------------
#                                   Calculo da potencia 
        case "p":
            limpar_tela()
            potencia1 = int(input("insira o numero inteiro para a potencia : "))
            potencia2 = int(input("insira o numero da potencia : "))
            result = math.pow(potencia1, potencia2)
            limpar_tela()
            print(f" \n o resultado da potencia e : {result} \n ")
            continue
#-----------------------------------------------------------------------------------------------
#                                   Divisão inteira 
        case "dd":
            limpar_tela()
            divisao_int = int(input("insira o numero inteiro para dividir : "))
            limpar_tela()
            divisor_int = int(input("insira o divisor : "))
            total = divisao_int // divisor_int
            limpar_tela()
            print(f"\n o resultado da divisão inteira e : {total} \n ")
            continue
#-----------------------------------------------------------------------------------------------
#                                      Possiveis erros
    total_input2 = len(decisao2)
    if total_input2 > 2:
        print("erro realize cada calculo apenas 1 vez")
        continue
#------------------------------------------------------------------------------------------------
#                           Entrada de dados para o numero do calculo e mensagem de erro
    try:
            limpar_tela()
            num1 = int(input(f" \n  insira um numero para continuar para o calculo  : "))
            limpar_tela()
            num2 = int(input(f" \n insira outro numero para continuar o calculo  : "))
            limpar_tela()
    except ValueError:
            limpar_tela()
            print("\n erro insira apenas numeros")
            limpar_tela()
            continue
#------------------------------------------------------------------------------------------------
#                                       ifs direcionados para Calculos 
    match decisao2:
            case "s":
                soma = num1 + num2
                print(f" o resultado da sua soma e : {soma}")
                print(barras)

            case "d":
                divisao = num1 / num2
                print(f" o resulado da divisão e : {divisao} ")
                print(barras)

            case "m":
                multiplicaçao = num1 * num2
                print(f" o resultado da multiplicação e : {multiplicaçao} ")
                print(barras)
#------------------------------------------------------------------------------------------------
#                                 mensagem de erro
            case _:
                print("um erro ocorreu tente novamente : ")
                continue

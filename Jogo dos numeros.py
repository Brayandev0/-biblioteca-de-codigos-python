# Criador         : Brayan vieira 
# função          : jogo de acerto de numero aleatorio 
# versão          : 2.2
# data da criação : 06/2/2024

import random 
import platform
import os
#----------------------------------------------------------------------------------------------------------------
#                                       Funções extras para deixar o codigo mais limpo
ESPACO = 2 * "\n"
BARRAS = 30 * "-"
#----------------------------------------------------------------------------------------------------------------
#                                            Erros do programa salvos
ERRO12 = "você não deve inserir numeros menores que 0"
ERRO10 = "você não deve inserir numeros maiores que 10"
ERRO5 = " erro insira somente numeros "
#----------------------------------------------------------------------------------------------------------------
#                                       identificando o sistema operacional para utilizar o clear 
SISTEMA = platform.system()
if SISTEMA == "Windows":
    limpar = "cls"
elif SISTEMA == "Linux":
    limpar = "clear"
#----------------------------------------------------------------------------------------------------------------
#                                       Cores do programa 
class color :
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

while True:
#-----------------------------------------------------------------------------------------------------------------
#                                        Menu de inicio
    os.system(limpar)
    print("bem vindo ao jogo de acertos, irei gerar um numero de 1 a 10 e vc deve acertar qual e o numero  \n ")
#-----------------------------------------------------------------------------------------------------------------
#                                         Erro de caracter invalido 
    try:
        numero_do_usuario = int(input(" Insira algum numero para tentar adivinhar o meu :  "))
        print(BARRAS)
    except ValueError:
        print(ESPACO)
        print(ERRO5)
        print(BARRAS)
        exit(5)
#----------------------------------------------------------------------------------------------------------------
#                                Erro de numero invalido (maior que 10)

    if numero_do_usuario > 10:
        print(ERRO10)
        print(BARRAS)
        exit(10)
#----------------------------------------------------------------------------------------------------------------
#                                       erro de numero invalido (menor que 0)
    if numero_do_usuario < 0:
        print(ERRO12)
        print(BARRAS)
        exit(12)

#-----------------------------------------------------------------------------------------------------------------
#                                       gerando o numero 
    numero_da_maquina = random.randint(1,10)
#-----------------------------------------------------------------------------------------------------------------
#                                   configurando o acerto 
    if numero_do_usuario == numero_da_maquina:
        os.system(limpar)
        print(color.GREEN + "você acertou meu numero parabens " + color.RESET)
        print(ESPACO)
#----------------------------------------------------------------------------------------------------------------
#                                   configurando o erro 
    os.system(limpar)
    print(color.RED + f" Você errou meu numero e : {numero_da_maquina}" + color.RESET)
    print(ESPACO)
#----------------------------------------------------------------------------------------------------------------
#                                       quer reiniciar o looping? 
    dnv = input("quer jogar novamente ? [S] sim [N] não : ").lower().startswith("s")
    if dnv == True:
        continue
    break

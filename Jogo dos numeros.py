import random 
import sys
ESPACO = 5 * "\n"
BARRAS = 30 * "-"
class color :
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
while True:
#-----------------------------------------------------------------------------------------------------------------
#                                        Menu de inicio
    print(ESPACO)
    print("bem vindo ao jogo de acertos, irei gerar um numero de 1 a 10 e vc deve acertar qual e o numero ")
    print(ESPACO)

#-----------------------------------------------------------------------------------------------------------------
#                                          tratamento de erros 
    try:
        num1 = int(input(" Insira algum numero para tentar adivinhar o meu :  "))
    except:
        print(BARRAS)
        print(" erro insira somente numeros ")
        print(BARRAS)
        sys.exit()


    if num1 > 10:
        print(BARRAS)
        print("você não deve inserir numeros maiores que 10 ")
        print(BARRAS)
        sys.exit()
    if num1 < 0:
        print(BARRAS)
        print("você não deve inserir numeros menores que 0 ")
        print(BARRAS)
        sys.exit()

#-----------------------------------------------------------------------------------------------------------------
#                                       gerando o numero 
    my_num = random.randint(1,10)


#-----------------------------------------------------------------------------------------------------------------
    #                                             verificador de acertos
    if num1 == my_num:
        print(ESPACO)
        print(color.GREEN + "você acertou meu numero parabens " + color.RESET)
        print(ESPACO)
    else:
        print(ESPACO)
        print(color.RED + f" Você errou meu numero e : {my_num}" + color.RESET)
        print(ESPACO)
    dnv = input("quer jogar novamente ? [S] sim [N] não : ").lower().startswith("s")
    if dnv == True:
        continue
    else:
        break

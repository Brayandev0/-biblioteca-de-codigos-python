# Criador         : Brayan vieira 
# função          : Um teste de acertos  
# versão          : 1.0
# data da criação : 15/2/2024

#---------------------------------------------------------------------------------------
#                           configurando cores para o programa 
class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    RESET = '\033[0m'
#---------------------------------------------------------------------------------------
#                               Numero de acertos 
qtd_acertos = 0
qtd_erros = 0
#---------------------------------------------------------------------------------------
#                               configurando as perguntas 
perguntas = [
    {
    "pergunta": "quanto e 100 x 30 ?",
    "opcoes": ["1,000","2,000","3,000","4,930"],
    "resposta": "2"
    },
    {
        "pergunta" : "Quanto e 30 x 5 ? ",
        "opcoes"   : ["100","120","100","150","1000"],
        "resposta" : "3"   ,
    },

    {
        "pergunta" : "quanto e 100 / 20 ? ",
        "opcoes"   : ["2","3","5","0"],
        "resposta" : "2",
    },
]
#---------------------------------------------------------------------------------------
#                               obtendo as perguntas 
#
for objetos_dentro_da_lista in perguntas:
    print(f"\n Pergunta : {objetos_dentro_da_lista["pergunta"]} \n")
#---------------------------------------------------------------------------------------
#                           obtendo e mostrando o indices das perguntas 
#
    for indice, opcoes_de_escolha_do_num in enumerate(objetos_dentro_da_lista["opcoes"]):
        print(f"{indice}) {opcoes_de_escolha_do_num}")
#---------------------------------------------------------------------------------------
#                           Entrada de dados para verificar acertos
#    
    digito_do_usuario = input("\n Insira o numero da resposta : ")
#---------------------------------------------------------------------------------------
#                           Verificando os acertos 
#
    if digito_do_usuario == objetos_dentro_da_lista["resposta"]:
        qtd_acertos += 1
#---------------------------------------------------------------------------------------
#                           definindo cores e acertos 
#
        print( cor.VERDE + "\n Você acertou, parabéns \n " + cor.RESET)
        input("Insira enter para continuar")
#---------------------------------------------------------------------------------------
#                           definindo cores e erros 
#
    else: 
        input(cor.VERMELHO + "\n você errou " + cor.RESET + " \n \n insira algo para continuar : ")
        qtd_erros += 1
        continue
#---------------------------------------------------------------------------------------
#                       configurando a quantidade de erros e acertos 
#
print(f" \n \n quantidade de acertos : " + cor.VERDE + f"{qtd_acertos} \n" + cor.RESET + f" \n quantidade de erros : " + cor.VERMELHO + f"{qtd_erros} \n" + cor.RESET)

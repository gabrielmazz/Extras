#pip install cowsay

import cowsay, random, sys, time, os, string

arquivo = open("senhas.txt", "a+")   #Abre o arquivo e salva a senha que serão inseridas
os.system("cls")    #Limpa o terminal para uma melhor visualização

#Caracteres para definição
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()"

#Soma todas as definições para depois aleatorizar
for_pass = lower_case + upper_case + number + symbol

teste = False
while(teste != True):
    
    #Pede quantas casa a senha terá (1 / 70)
    teste2 = False
    while(teste2 != True):
        houses_number = (int)(input("Determine quantas casas a senha deverá ter (1/70 caracteres)?\n"))
        
        if((houses_number > 70) or (houses_number < 1)):
            print("Valor inválido, digite um número entre 1 e 70 novamente...")
            time.sleep(2)
            os.system("cls")
        else:
            teste2 = True
            continue
    
    #Determina qual será o lugar de destino da senha
    os.system("cls")
    destino = (str)(input("Qual o destino da senha?\n"))

    #Randomiza uma senha
    password = "".join(random.sample(for_pass, houses_number))

    #Insere numa lista o destino e a senha
    lista = [destino, ": ", password, "\n"]

    #Escreve no arquivo a senha randomizada e o nome do destino
    arquivo.writelines(lista)

    #Printa a senha no terminal
    os.system("cls")
    cowsay.cow('Minha senha é: {0} na plataforma {1}' .format(password, destino))
    
    #Pergunta se quer continuar a adicionar mais senhas
    decisao = (str)(input("\n\nDeseja adicionar mais uma senha?\nDigite 'S para SIM' ou 'N para Não'\n\nR: "))
    
    if(decisao == 'N' or decisao == 'n'):
        teste = True
        break
    else:
        os.system("cls")
        continue

#Fecha o arquivo
arquivo.close()

#Determina o tempo para fechar o programa
os.system("cls")
print("\n\nO programa finalizara em 10 segundos\n\n")

#Finaliza o programa
time.sleep(10)
sys.exit()
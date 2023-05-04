from time import sleep
import random
from unidecode import unidecode

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("********************************* \n")

    print("Escolha seu level de dificudade 1 para Facil, 2 para Médio e 3 para Dificil")

    verdade = True
    level = 0
    '''level != 1 or level != 2 or level != 3'''

    '''if verdade:
        print("Por favor digite apenas 1 , 2 ou 3 para selecionar o nivel de dificudade")
        jogar()'''

    while verdade:
        level = int(input("Qual o nivel de dificuldade que deseja: "))
        verdade = (1, 2, 3).__contains__(level)
        if not verdade:
            print("Por favor digite apenas 1 , 2 ou 3 para selecionar o nivel de dificudade")
            verdade = True
        else:
            verdade = False

    arquivo = open('palavras.txt', 'r',  encoding='utf-8')

    palavras = []

    for palavra in arquivo:
        palavras.append(palavra)

    palavra_secreta = random.choice(palavras).strip()

    arquivo.close()

    '''frutas = ['Maçã', 'Banana', 'Aranha', 'Paralelepipedo', 'Caminhão', 'Corrida', 'Aventura', 'Game', 'Computador']
    palavra_secreta = random.choice(frutas)'''

    print(palavra_secreta)

    enforcou = False
    acertou = False

    preenchendo = [" "] * len(palavra_secreta)

    dificudade = 0

    if(level == 1):
        dificudade = len(palavra_secreta) + 10
    elif(level == 2):
        dificudade = len(palavra_secreta) + 5
    else:
        dificudade = len(palavra_secreta) + 2

    print("\nDigite uma letra para descobrir a palavra!")

    while(not enforcou and not acertou):

        chute = input(f"Palavra com {len(palavra_secreta)} letras, Qual é letra?: ")
        chute = chute.strip()

        print('PROCESSANDO...')

        sleep(.5)

        if(len(chute) > 1):
            print('Por favor digite apenas um caractere \n')
            continue

        palavra_sem_caracter = ''.join(filter(str.isalpha, unidecode(palavra_secreta)))
        if(not chute.upper() in palavra_sem_caracter.upper()):
            print(f'Não existe a letra {chute} na palavra secreta \n')
            dificudade -= 1
            if (dificudade == 0):
                print("Que pena numero de tentativas se esgotou :( ")
                break
            continue

        index = 0

        for letra in palavra_secreta:
            letra_sem_caracter = letra.join(filter(str.isalpha, unidecode(letra)))
            if(chute.upper() == letra_sem_caracter.upper()):
                print(f"Encontrei a letra {chute} na posição {index+1}")
                for i in range(len(preenchendo)):
                    if i == index:
                        preenchendo[i] = letra
            index += 1

        dificudade -= 1
        letras_acertadas = ''.join(preenchendo)
        print(f"{letras_acertadas.replace(' ', '_')}")

        if " " not in preenchendo:
            print("Parabéns, você ganhou! \n")
            break


    print("Final de Jogo!")


if (__name__ == "__main__"):
    jogar()
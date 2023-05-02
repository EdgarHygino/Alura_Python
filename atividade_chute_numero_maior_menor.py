'''
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

entrada = int(input("Digite um número: "))
numSecreto = 35

acertou = entrada == numSecreto
maior = entrada > numSecreto
menor = entrada < numSecreto

if acertou:
    print('Parabens voce acertor')
else:
    if maior:
        print('O seu número é maior que o número secreto')
    elif menor:
        print('O seu número é menor que o número secreto')

print("Fim do jogo")
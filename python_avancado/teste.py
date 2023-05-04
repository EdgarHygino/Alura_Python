string = ""

letra_1 = input("Digite a letra para a posição 1: ")
letra_3 = input("Digite a letra para a posição 3: ")
letra_5 = input("Digite a letra para a posição 5: ")

for i in range(len(string)):
    if i == 0:
        string += letra_1
    elif i == 2:
        string += letra_3
    elif i == 4:
        string += letra_5
    else:
        string += " "

print(string)
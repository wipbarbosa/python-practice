matriz = []

for i in range(3):

    linha = []

    for j in range(3):
        numeros = int(input("Digite 3 numeros:"))
        linha.append(numeros)

    matriz.append(linha)

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()
        
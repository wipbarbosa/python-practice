matriz = []
pares = []

for i in range(3):
    linha = []
    print(f"{i + 1}ª linha.")
    for j in range(3):
        numero = int(input(f"Digite o {j + 1}º numero: "))
        linha.append(numero)

    matriz.append(linha)

print(matriz)

for i in range(3):
    for j in range(3):
        if matriz [i][j] % 2 == 0:
            pares.append(matriz)
    

print(pares)

matriz = []

for i in range(3):
    linha = []

    print(f'{i + 1}ª linha')
    for j in range(3):
        numero = int(input(f"Digite o {j+1}º numero: "))
        linha.append(numero)

    matriz.append(linha)


for i in range(3):
    maior = matriz [i][0]
    for j in range(3):
        if matriz [i][j] > maior:
            maior = matriz [i][j]

    print(f'Maior da linha {i + 1}: {maior}')

for j in range(3):
    maior = matriz [0][j]
    for i in range(3):
        if matriz [i][j] > maior:
            maior = matriz [i][j]

    print(f'Maior da coluna {j + 1}: {maior}')

matriz = []

for i in range(3):
    linha = []
    print(f'{i + 1}ª linha')

    for j in range(3):
        numero = int(input(f"Digite o {j + 1}º número: "))
        linha.append(numero)

    matriz.append(linha)


for i in range(3):
    soma = 0

    for j in range(3):
        soma += matriz[i][j]

    print(f'Soma da linha {i + 1}: {soma}')

for j in range(3):
    soma = 0

    for i in range(3):
        soma += matriz[i][j]

    print(f'Soma da coluna {j + 1}: {soma}')
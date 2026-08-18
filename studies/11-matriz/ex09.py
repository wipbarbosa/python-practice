matriz = []
soma = 0

for i in range(3):
    linha = []

    print(f'{i + 1}ª linha')
    for j in range(3):
        numero = int(input(f"Digite o {j+1}º numero: "))
        linha.append(numero)

    matriz.append(linha)


for i in range(3):
    soma += matriz[i][2 - i]

print(f'{soma}')

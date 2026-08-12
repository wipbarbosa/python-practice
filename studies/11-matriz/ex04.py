matriz = []
soma_diagonal = 0

for i in range(3):

    linha = []
    print(f'\n{i+1}ª linha')

    for j in range(3):
        numero = int(input(f'Digite o {j+1} numero: '))
        linha.append(numero)

    matriz.append(linha)

for i in range(3):
    soma_diagonal += (matriz[i][i])

print(soma_diagonal)
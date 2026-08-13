matriz = []
soma = 0

for i in range(4):
    linha = []
    print(f'{i + 1}ª linha.')

    for j in range(4):
        numero = int(input(f'Digite o {j + 1}º número: '))
        linha.append(numero)

    matriz.append(linha)

maiores = []

for j in range(4):
    maior = matriz[0][j]

    for i in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

    maiores.append(maior)

for numero in maiores:
    soma += numero

media = soma / len(maiores)

for linha in matriz:
    for numero in linha:
        print(numero, end=" ")
    print()
print(maiores)
print(soma)
print(media)
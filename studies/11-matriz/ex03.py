matriz = []
soma = 0

for i in range(3):

    linha = []
    print(f"{i+1}ª linha")

    for j in range(3):
        numero = int(input("Digite 3 numeros: "))
        linha.append(numero)

    matriz.append(linha)

maior = matriz [0][0]
menor = matriz [0][0]

for i in range(3):
    for j in range(3):
        soma += matriz[i][j]

        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]

media = soma / 9

print(
    f'Soma: {soma}\n'
    f'Média: {media}\n'
    f'Maior: {maior}\n'
    f'Menor: {menor}\n'
    )

'''numeros = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print (numeros[2][1])'''


'''numeros = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

soma = 0

for linha in numeros:
    for numero in linha:
        soma += numero
'
print(soma)'''


'''numeros = [
    [10, 20, 30],
    [40, 51, 60],
    [70, 81, 90]
]

for linha in numeros:
    for numero in linha:
        if numero % 2 == 0:
            print(numero)'''

'''numeros = [
    [10, 20, 30],
    [40, 51, 60],
    [70, 81, 90]
]

maior = numeros [0][0]

for linha in numeros:
    for numero in linha:
        if numero > maior:
            maior = numero

print (maior)'''

matriz = []

for i in range(2):
    linha = []

    for j in range(2):
        numero = int(input("Digite um numero:"))
        linha.append(numero)

    matriz.append(linha)

for linha in matriz:
    for numero in linha:
        print(numero, end=" ")
    print()

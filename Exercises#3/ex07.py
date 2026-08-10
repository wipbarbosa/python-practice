# 7. A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor máximo e o valor mínimo
# de uma amostra. Elabore um programa que leia um vetor de 10 posições inteiras e então mostre o valor máximo, o valor
# mínimo e a amplitude amostral do conjunto fornecido.

lista = []
primeiro = int(input('Digite o 1° numero inteiro: '))
lista.append(primeiro)

maior = primeiro
menor = primeiro


for i in range(1,10):
    numero = int(input(f'Digite o {i + 1}º numero inteiro: '))
    lista.append(numero)

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

amplitude = maior - menor

print(
    f'Lista de números inteiros digitados: {lista}\n'
    f'Máximo: {maior}\n'
    f'Mínimo: {menor}\n'
    f'Amplitude: {amplitude}'
    )
# 9. Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido. Depois, crie dois outros
# vetores: vPares, contendo somente os números pares de vLido, e vImpares contendo somente os números ímpares de vLido.
# Os vetores vPares e vLido não deverão conter zeros. Mostre então os três vetores.

vLido = []
vPares = []
vImpares = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))

    if numero != 0:
        vLido.append(numero)

        if numero % 2 == 0:
            vPares.append(numero)
        else:
            vImpares.append(numero)

print(
    f'Todos: {vLido}\n'
    f'Pares: {vPares}\n'
    f'Ímpares: {vImpares}'
    )
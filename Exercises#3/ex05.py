# 5. Ler 4 números inteiros e calcular a soma dos que forem par.

pares = 0

for i in range(4):
    numeros = int(input(f"Digite o {i + 1}º número inteiro: "))

    if numeros % 2 == 0:
        pares += numeros

print (f'A soma dos números pares inseridos é de: {pares}')
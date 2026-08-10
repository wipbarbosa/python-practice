# 11. Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra um conjunto de 6
# números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do usuário (sem repetição) e indique quantos
# acertos ele teve.
import random

print('===== MEGA SENA =====')

computador = []
usuario = []
acertos = 0

while len(computador) < 6:
    aleatorio = random.randint(1,60)

    if aleatorio not in computador:
        computador.append(aleatorio)

while len(usuario) < 6:
    entrada = int(input(f'Digite 6 números inteiros: '))

    if entrada <= 0 or entrada > 60:
        print("Número invalido")

    elif entrada not in usuario:
        usuario.append(entrada)

for aletorio in computador:
    if aleatorio in usuario:
        acertos += 1


print(f'Resultado: {computador}')
print(f'Números do usuário: {usuario}')
print(f'Número de acertos: {acertos}')

if acertos == 6:
    print('===== PARABÉNS, VOCÊ GANHOU! ===== ')
else:
    print('===== Não foi dessa vez! =====')


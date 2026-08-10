# 10. Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas valores positivos. Modifique
# então o vetor de forma que, tenhamos primeiro todos os números pares, depois, os números impares. Mostre o vetor antes de
# depois da modificação

lista = []
lista_final = []

for i in range(1,11):
    numero = int(input(f'Digite o {i}º número:'))

    while numero <= 0:
        print('Número inválido!')
        numero = int(input(f'Digite o {i}º número:'))
    
    lista.append(numero)

for numero in lista:
    if numero % 2 == 0:
        lista_final.insert(0, numero) 
    else:
        lista_final.append(numero)

print(lista)
print (lista_final)
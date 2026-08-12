'''nomes = ["Ana", "Carlos", "Pedro", "Maria", "João"]

for i , nome in enumerate(nomes):
    if i  % 2 ==  0:
        print (nome)'''

'''numeros = [10, 5, 20, 8]

print(sum(numeros))
print(min(numeros))
print(max(numeros))'''

'''numeros = [1, 2, 3, 4, 5, 6]

dobro = [numero + numero for numero in numeros]
print (dobro)'''

'''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0 ]

print (pares)

impares = [numero for numero in numeros if numero % 2 == 1 ]

print (impares)'''


'''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maiores = [numero for numero  in numeros if numero > 5]

print (maiores)'''


'''numeros = [1, 2, 3, 4, 5, 6]

dobro_pares = [numero * 2 for numero in numeros if numero % 2 == 0]

print(dobro_pares)'''

import random

lista = []

while True:
    numero = random.randint(1, 10)
    
    if numero not in lista:
        lista.append(numero)

    if len(lista) == 10:
        break
    
print(lista)

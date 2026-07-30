lista = []
contador_pares = 0

numero_inicial = int(input(f"Olá, Digite o 1º número inteiros: "))
soma = numero_inicial
maior = numero_inicial
menor = numero_inicial
lista.append(numero_inicial)

for i in range (4):
    numero = int(input(f"Digite o {i + 2}º  número inteiros: "))
    lista.append(numero)
    soma += numero

    if numero <= menor:
        menor = numero
    if numero >= maior:
        maior = numero



print(f"==Lista digitada==")
for numero in lista:
    print(f"--{numero}")
print( "=" * 20)

for numero in lista:

    if numero %2 == 0:
        print(f"{numero}: É par.")
        contador_pares += 1
print( "=" * 20)

print(
    f"Soma dos numeros digitados: {soma}\n"
    f"Maior numero digitado: {maior}\n"
    f"Menor numero digitado: {menor}\n"
    f"Quantidade de números pares: {contador_pares}"
    )




    


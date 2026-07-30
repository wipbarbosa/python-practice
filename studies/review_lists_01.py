lista = []
numero_inicial = int(input(f"Olá, Digite o 1º  número inteiros: "))
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




print(f"\nLista digitada: {lista}\n")

for numero in lista:

    if numero %2 == 0:
        print(f"{numero} é par")

print(
    f"A soma dos numeros digitados é: {soma}\n"
    f"O maior numero digitado é {maior}\n"
    f"O menor numero digitado é {menor}"
      )




    


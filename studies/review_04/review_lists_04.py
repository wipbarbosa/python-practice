lista = []
soma = 0
pares = 0
impares = 0

primeiro_numero = int(input(f"Digite o 1º número (entre 1 e 100): "))
    
while primeiro_numero < 1 or primeiro_numero > 100:
    primeiro_numero = int(input("Número inválido! Digite um número entre 1 e 100: "))

if primeiro_numero % 2 == 0:
    pares += 1
else:
    impares += 1

soma = soma + primeiro_numero
lista.append(primeiro_numero)

maior_numero = primeiro_numero
menor_numero = primeiro_numero

for i in range(4):
    numero = int(input(f"Digite o {i + 2}º número (entre 1 e 100): "))
    
    while numero < 1 or numero > 100:
        numero = int(input("Número inválido! Digite um número entre 1 e 100: "))

    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

    if numero % 2 == 0:
        pares +=1
    else:
        impares += 1
    
    soma = soma + numero
    lista.append(numero)



print("\nLista final de números válidos:")
print(
    f"{'=' * 20}\n"
    f"Resultado\n"
    f"{'=' * 20}\n"
    )
print (f"\nLista{lista}")
print (f"Soma: {soma}")
print (f"Média: {soma / 5}")
print (f"Quantidade de números Pares: {pares}")
print (f"Quantidade de números Ímpares: {impares}")
print (f"Maior número: {maior_numero}")
print (f"menor numero: {menor_numero}")

print (f"\n{'='* 20}")
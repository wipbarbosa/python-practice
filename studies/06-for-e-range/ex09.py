pares = 0
impares = 0

for i in range(10):
    numeros = int(input("Digite 10 numeros: "))
    if numeros % 2 == 0:
        pares += 1
    else:
        impares += 1

print (f"Pares: {pares}")
print (f"Impares: {impares}")




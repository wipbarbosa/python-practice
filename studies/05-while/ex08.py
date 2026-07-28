contador = 0
pares = 0

while contador < 10:

    numeros = int(input("Digite 10 numeros"))
    if numeros  % 2 == 0:
        pares += 1


    contador += 1

print (f"foram digitados {pares} numeros pares")

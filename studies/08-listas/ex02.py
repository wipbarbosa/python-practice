lista = []

for _ in range (5):
    entrada = int(input("Digite 5 numeros"))
    lista.append(entrada)

for numeros in lista:
    if numeros % 2 == 0:
        print (numeros)
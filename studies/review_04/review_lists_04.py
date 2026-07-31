lista = []

for i in range(5):
    numero = int(input("Digite 5 numeros"))
    if numero > 100 or numero < 1:
        print("Numero invalido")
        while numero > 100 or numero < 1:
            int(input("Numero invalido"))
    lista.append(numero)
print (lista)
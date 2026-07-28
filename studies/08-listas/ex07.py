#Exercicio 10
lista = []

for i in range(5):
    numeros = int(input("Digite 5 numeros: "))
    lista.append(numeros)

lista.sort()
print (lista)

#Exercicio 11

lista = ["Ana", "Carlos", "Pedro", "Ana"]

print (lista.count("Ana"))
print (lista.index("Ana"))


#Exercicio 12

lista1 = [100, 200, 300]

lista2 = lista1.copy()

lista2.append(400)

print(f"verdadeira = {lista1}")
print(f"cópia = {lista2}")
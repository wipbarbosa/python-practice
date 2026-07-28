lista = []

for i in range(5):
    numeros = int(input("Digite numeros desejados: "))
    lista.append(numeros)
print (lista)


for i in lista:

    remover = int(input("Qual numero deseja remover? "))
    while remover != i:
         remover = int(input("numero nao encontrado, digite novamente: "))
         
    i.remove(remover)
    print(lista)





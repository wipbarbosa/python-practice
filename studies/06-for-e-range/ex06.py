inicial = int(input("Digite 5 numeros"))

maior =  inicial
menor = inicial

for _ in range (4):
    numeros = int(input("Digite 5 numeros"))
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros

print(maior)
print (menor)

soma = 0

for i in range (5):
    numeros = int(input("Digite 5 numeros"))
    if i == 0:

        maior = numeros
        menor = numeros

    if numeros > maior:
        maior = numeros
    
    if numeros < menor:
        menor = numeros

    soma += numeros


media = soma /5

print (soma)
print (media)
print (maior)
print (menor)

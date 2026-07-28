soma = 0
notas_sete = 0

for i in range (0,10):
    numeros =  int(input("Digite 10 notas entre 0 e 10: "))


    while numeros < 0 or numeros > 10:
        print("Nota invalido")
        numeros =  int(input("Digite 10 notas entre 0 e 10: "))

    if i == 0:

        maior = numeros
        menor = numeros

    if numeros > maior:
        maior = numeros
    
    if numeros < menor:
        menor = numeros
    
    if numeros >= 7:
        notas_sete += 1
    
    soma = soma + numeros

media = soma / 10


print(f"Soma: {soma}")
print(f"Media: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Notas setesou maiores: {notas_sete}")
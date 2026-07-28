numero = int(input("Digite um numero"))
contador = -0
maior = numero
menor = numero
soma =  numero





if numero == 0:
    print("Fim")
else:
    while numero != 0:
        numero = int(input("Digite um numero"))
        contador = contador +1
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        soma = numero + soma
        

print(contador)
print(menor)
print(maior)
print(soma)


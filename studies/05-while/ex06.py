cinco_numeros = 0
maior = 0

while cinco_numeros < 5:
        numero = int(input("Digite um numero"))
        cinco_numeros = cinco_numeros +1
        if numero > maior:
            maior = numero
print (maior)
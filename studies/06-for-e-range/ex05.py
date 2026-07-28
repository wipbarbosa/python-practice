for inicial in range(1):
    inicial = int(input("Digite 5 numeros"))

maior = inicial

for _ in range(4):
    numero = int(input("Digite 5 numeros"))
    if numero > maior:
        maior = numero
        
print(maior)
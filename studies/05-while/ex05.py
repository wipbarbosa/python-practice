numero = int(input("Digite um numero"))
numero_correto = 0
contador = 0
if numero != 0:
        contador = contador + 1


while numero != numero_correto:
    numero = int(input("tente novamente"))
    if numero != 0:
        contador = contador + 1

print(f"Numero correto! tentativas = [{contador}]")
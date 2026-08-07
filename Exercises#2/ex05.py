#5. Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário

entrada = int(input("Escreva até qual numero o contador deve ir: "))
contador = 0

while contador < entrada:
    contador += 1

    if contador %2 == 1:
        print(contador)

entrada = int(input("Escreva até qual número o contador deve ir: "))

for i in range(1, entrada + 1):
    if i % 2 == 1:
        print(i)       
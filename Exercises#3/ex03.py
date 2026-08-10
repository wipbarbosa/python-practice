# 3. Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

entrada = int(input('Digite o 1º número inteiro: '))
soma = 0

for i in range (2):
    numero1 = entrada

    numeros = int(input(f'Digite o {i +2}º número inteiro: '))

    soma += numeros

if soma > numero1:
    print (f"A soma dos dois segundos {soma} numeros é meior que o primeiro{entrada}")
else:
    print(f"A soma dos dois segundos numeros {soma} é menor que o primeiro {entrada}")




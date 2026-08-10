# 3. Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

primeiro = int(input('Digite o 1º número inteiro: '))
soma = 0

for i in range (2):
    numero = int(input(f'Digite o {i +2}º número inteiro: '))
    soma += numero

if primeiro > soma:
    print(f"O primeiro número ({primeiro}) é maior que a soma dos outros dois ({soma}).")
else:
    print(f"O primeiro número ({primeiro}) não é maior que a soma dos outros dois ({soma}).")
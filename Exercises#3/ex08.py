# 8. Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um número que ele gostaria de
# pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is) posição(ões) ele foi encontrado e quantas ocorrências
# foram detectadas.

lista = []
posicoes = []

# 1. Leitura dos 10 números
for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número: '))
    lista.append(numero)

# 2. Leitura do número a ser pesquisado
pesquisa = int(input('Qual número deseja pesquisar? '))

# 3. Pesquisa no vetor
for i in range(10):
    if lista[i] == pesquisa:
        posicoes.append(i + 1)  # Guarda o índice (posição) onde o número foi encontrado

# 4. Exibição dos resultados
if len(posicoes) > 0:
    print(f"\nO número {pesquisa} foi encontrado!")
    print(f"Quantidade de ocorrências: {len(posicoes)}")
    print(f"Posição(ões) no vetor: {posicoes}")
else:
    print(f"\nO número {pesquisa} não foi encontrado no vetor.")
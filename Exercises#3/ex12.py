# 12. Desenvolva um programa que leia um lsita de 20 posições inteiras e o coloque em ordem crescente, utilizando a seguinte
# estratégia de ordenação:
# • selecione o elemento do lsita de 20 posições que apresenta o menor valor;
# • troque este elemento pelo primeiro;
# • repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de menor valor com a segunda
# posição), depois os 18 elementos (trocando o de menor valor com a terceira posição), depois os 17, 16 e assim por diante,
# até restar um único elemento, o maior deles.
# Observação: este método de ordenação é conhecido como “Seleção Direta”

lista = []

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista.append(numero)

for i in range(len(lista) - 1):

    menor = i

    for j in range(i + 1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j

    lista[i], lista[menor] = lista[menor], lista[i]


print(lista)
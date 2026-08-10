# 6. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é
# triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.

numero = int(input('digite um numero para verficar se ele é triangular: '))

x = 1
produto = x * (x + 1) * (x + 2)

while produto < numero:
    x += 1
    produto =  x * (x + 1) * (x + 2)

if produto == numero:
    print(
    f"O número {numero} É TRIANGULAR! "
    f"({x} * {x + 1} * {x + 2} = {produto})"
    )
else:
    print(f"O número {numero} NÃO é triangular.")
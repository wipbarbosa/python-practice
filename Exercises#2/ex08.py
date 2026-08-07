#8. Elabore um algoritmo que leia um conjunto de 10 números inteiros.
#  Mostre então qual o valor da soma e da média aritmética do conjunto.

print(f"===== Soma e média de 10 números inteiros =====")


soma = 0


for i in range(1,11):
    numero = int(input(f"\nDigite o {i}º número: "))
    soma += numero


media = soma / 10

print(f"\nA soma dos valores é: {soma}\n"
      f"A média dos valores é: {media:.2f}\n")

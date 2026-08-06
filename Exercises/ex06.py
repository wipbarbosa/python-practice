#   6. Faça um algoritmo que calcule a quantidade de latas de tintas necessárias para pintar um tanque cilindro,
#   em que são fornecidas sua altura e raio, sabendo que:
#   a. A lata de tinta custa R$ 50,00
#   b. Cada lata contém 5 litros
#   c. Cada litro de tinta pinta 3 metros quadrados
#   d. Entrada do programa: altura e raio do cilindro
#   e. Saída: valor em reais e quantidade de latas

import math

custo_lata = 50

metros_por_litro = 3

litros_lata = 5

altura = float(input("Digite a altura do cilindro"))

raio = float(input("digite o raio do cilindro"))

area = 2 * math.pi * raio * (raio + altura)

print (f"A área do cilindro é de: {area}")

litros_necessarios = area / metros_por_litro

latas = math.ceil(litros_necessarios / litros_lata)


valor = latas * custo_lata

print (f"Será necessário {latas} latas de tinta para pintar {area:.2f} mt². \n"
       f"Valor total: R$ {valor:.2f}."
)
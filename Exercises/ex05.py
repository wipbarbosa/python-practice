#5. Faça um algoritmo que calcule o consumo médio de um automóvel (medido em km/l),
#   solicitando como entrada a distância total percorrida (KM)
#   e o volume de combustível consumido para percorrê-la (litros).

print ("====== CÁLCULO PARA CONSUMO MÉDIO DE COMBUSTÍVEL  =====\n")


distancia = float(input("Distância percorrida em KM:"))
while distancia <= 0:
    distancia = float(input("\nDigite um valor maior que zero para o combustível: "))

combustivel = float(input("\nCombustivel gasto em litros: "))

while combustivel <= 0:
    combustivel = float(input("\nDigite um valor maior que zero para o combustível: "))

media = distancia / combustivel

print(f"Consumo médio: {media:.2f} km/L")
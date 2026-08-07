#6. Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de 1 a 20 polegadas.
# A conversão entre estas duas unidades é dada por: centímetro = polegada × 2,54.

print("===== TABELA DE CONVERSÃO DE POLEGADAS PARA CM =====")

for i in range(1, 21):
    print(f"{i} polegadas = {i * 2.54:.2f} cm")
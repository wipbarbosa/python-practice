matriz = [
    [10, 80, 30],
    [40, 50, 90],
    [70, 20, 60]
]

maior = matriz[0][0]

for i in range(3):
    if matriz[i][0] > maior:
        maior = matriz[i][0]

print (maior)

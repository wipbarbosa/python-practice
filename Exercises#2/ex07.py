#7. Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela de conversão de
# metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10 quilômetros.

uma_milha = 1609.344

for i in range(20, 170, 10):
    metros = i * 1000
    milhas = metros / uma_milha

    print(
        f"{i} km = {metros:,.0f} metros = {milhas:.2f} milhas"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
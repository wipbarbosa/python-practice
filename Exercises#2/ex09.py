#9. Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final).
#  Os valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao intervalo, ou seja, intervalo aberto.

inicial = int(input("Digite o número inicial: "))
final = int(input("Digite o número final:  "))

for i in range(inicial +1, final):
    if i % 3 == 0:
        print (f"Entre o intervalo de {inicial} e {final} os números múltiplos de 3 são: {i}")
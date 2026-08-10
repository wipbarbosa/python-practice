# 4. Leia dois valores reais do teclado, calcular e imprimir na tela:
# a) A soma destes valores b) O produto deles c) O quociente entre eles

print(f"===== PROGRAMA DE SOMA, PRODUTO E QUOCIENTE DE DOIS VALORES REAIS =====")

numero1 = float(input(f'Digite o primeiro número: '))
numero2 = float(input(f'Digite o segundo número: '))

soma = numero1 + numero2
produto = numero1 * numero2
quociente = numero1 / numero2



print(
    f'===== RESULTADO =====\n'
    f'Soma: {soma}\n'
    f'Produto: {produto}\n'
    f'Quociente: {quociente}'
    )




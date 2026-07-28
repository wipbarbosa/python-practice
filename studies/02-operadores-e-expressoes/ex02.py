print("=== Calculadora ===")
numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2 
divisao = numero1 / numero2 
divisao_inteira = numero1 // numero2
resto_da_divisao = numero1 % numero2
potencia = numero1 ** numero2

print(f"======= RESULTADOS =======")
print()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}")
print(f"Resto: {resto_da_divisao}")
print(f"Potência: {potencia}")
print()
print(f"==========================")
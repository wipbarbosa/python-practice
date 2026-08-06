#3. Faça um algoritmo que receba o salário de um profissional e calcule quantos salário mínimos ele recebe.

SALARIO_MINIMO = 1621
print("===== CÁLCULO QUANTIA DE SALÁRIO MÍNIMO =====\n")
print("=" * 30)

salario_usuario = float(input("Digite o seu salário atual: "))
print("=" * 30)


resultado = salario_usuario / SALARIO_MINIMO

print(f"\nVocê recebe {resultado:.2f} salários mínimos.")

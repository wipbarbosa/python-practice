#2. Faça um algoritmo que leia o ano de nascimento de uma pessoa e calcule a idade que completará até o final de 2025.

print("===== IDADE DO USUÁRIO AO FINAL DO ANO DE 2025 =====\n")

ANO_REFERENCIA = 2025

ano_nascimento = int(input("Digite o ano do seu nascimento: "))

idade = ANO_REFERENCIA - ano_nascimento

print(f"\nSua idade ao final do ano de 2025 será de {idade}")
print("=" * 40)
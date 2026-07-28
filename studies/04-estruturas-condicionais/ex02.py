nota = int(input("Digite a sua nota de 0 a 10"))

if nota >= 7:
    print(f"Sua nota é {nota} você está aprovado!")
elif nota >=5:
    print(f"Sua nota é {nota} você está de recuperação!")
else:
    print(f"Sua nota é {nota} você está Reprovado!")
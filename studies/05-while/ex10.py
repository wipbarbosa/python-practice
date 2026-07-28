nota1 = int(input("Digite a primeira nota"))
nota2 = int(input("Digite a segunda nota"))
nota3 = int(input("Digite a terceira nota"))
nota4 = int(input("Digite a quarta nota"))
nota5 = int(input("Digite a quinta nota"))
soma =  nota1 + nota2 + nota3 + nota4 + nota5
media = soma / 5

while nota1 and nota2 and nota3 and nota4 and nota5 > 10 or nota1 and nota2 and nota3 and nota4 and nota5 < 0:
    print("Somente aceitas notas entre 0 e 10")

    nota1 = int(input("Digite a primeira nota"))
    nota2 = int(input("Digite a segunda nota"))
    nota3 = int(input("Digite a terceira nota"))
    nota4 = int(input("Digite a quarta nota"))
    nota5 = int(input("Digite a quinta nota"))

    soma = nota1 + nota2 + nota3 + nota4 + nota5
    media = soma / 5


print (soma)

print (media)



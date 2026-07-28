print(f"Idade mínima Permitida: 18 anos")
idade = int(input("Digite a sua idade"))
ingresso = input("Voce tem ingresso?")


if idade < 18:
        print (f"Sua idade é de{idade}anos, entrada não permitida para menores de idade!")
elif ingresso == ("nao"):
        print (f"necessario ingresso , entrada não permitida!")
else:
        print (f"entrada permitida!")


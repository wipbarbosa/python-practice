lista = []

primeiro_nome = input("Digite o 1º Nome: ").lower()
lista.append(primeiro_nome)

maior_nome = len(primeiro_nome)
menor_nome = len(primeiro_nome)

for i in range(4):
    nomes = input(f"Digite o {i + 2}º nome: ").lower()
    lista.append(nomes)

print(f"==Lista de nomes==\n")
for nomes in lista:
    print(f"--{nomes}\n"
          f"({"=" * 20})"
          )
print(f"({"=" * 20})")
    

for nomes in lista:
    if len(nomes) > 5:
        print(f"{nomes}: tem mais que 5 letras.")

print (maior_nome)
print (menor_nome)
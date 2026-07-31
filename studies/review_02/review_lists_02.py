lista = []

primeiro_nome = input("Digite o 1º Nome: ").lower()
lista.append(primeiro_nome)

maior_nome = primeiro_nome
menor_nome = primeiro_nome

for i in range(4):
    nome_input = input(f"Digite o {i + 2}º nome: ").lower()
    lista.append(nome_input)
    
    if len(nome_input) > len(maior_nome):
        maior_nome = nome_input 
    
    if len(nome_input) < len(menor_nome):
        menor_nome = nome_input

print("==Lista de nomes==")
for nome in lista:
    print(f"--{nome}")
print(f"{'=' * 20}\n")

for nome in lista:
    if len(nome) > 5:
        print(f"{nome}: tem mais que 5 letras.")
print(f"{'=' * 20}\n")

for nome in lista:
    if nome.startswith("a"):
        print(f"{nome} começa com A")
print(f"{'=' * 20}\n")

print(f"O maior nome é: {maior_nome}")
print(f"O menor nome é: {menor_nome}\n")
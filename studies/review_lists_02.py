lista = []

primeiro_nome = input("Digite o 1º Nome: ").lower()
lista.append(primeiro_nome)

maior_nome = primeiro_nome
menor_nome = primeiro_nome

for i in range(4):
    nomes = input(f"Digite o {i + 2}º nome: ").lower()
    lista.append(nomes)
    if len(nomes) > len(maior_nome):
        maior_nome = nomes 
    
    if len(nomes) < len(menor_nome):
        menor_nome = nomes

print(f"==Lista de nomes==\n")
for nomes in lista:
    print(f"--{nomes}\n")
print(f"{'=' * 20}")
    

for nomes in lista:
    if len(nomes) > 5:
        print(f"{nomes}: tem mais que 5 letras.")

for nomes in lista:
    if nomes.startswith("a"):
        print(f"{nomes} começa com A")


print (f"O maior nome é: {maior_nome}")
print (f"O menor nome é: {menor_nome}")
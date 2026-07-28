nome = input("Digite um nome: ").lower()

print(
    f"Começa com a? {nome.startswith('a')}  \n"
    f"Termina com o? {nome.endswith('o')}" 
)

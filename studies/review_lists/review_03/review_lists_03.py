lista = []

palavras_A = 0
palavras_B = 0
quantidade_acima = 0
quantidade_abaixo = 0


primeira_palavra = input("Digite a 1ª palavra: ").lower()
lista.append(primeira_palavra)

maior_palavra = primeira_palavra
menor_palavra = primeira_palavra

if primeira_palavra.startswith("a"):
    palavras_A += 1
if primeira_palavra.startswith("b"):
    palavras_B += 1

if len(primeira_palavra) > 5:
    quantidade_acima += 1
if len(primeira_palavra) <= 5:
    quantidade_abaixo += 1


for i in range(7):
    palavra_input = input(f"Digita a {i + 2}ª palavra: ").lower()
    lista.append(palavra_input)

    if len(palavra_input) > len(maior_palavra):
        maior_palavra = palavra_input
    if len(palavra_input) < len(menor_palavra):
        menor_palavra = palavra_input

    if palavra_input.startswith("a"):
        palavras_A += 1
    if palavra_input.startswith("b"):
        palavras_B += 1

    if len(palavra_input) > 5:
        quantidade_acima += 1
    if len(palavra_input) <= 5:
        quantidade_abaixo += 1


print(f"Lista de palavras: ")
print(f"{lista}")

print (f"Quantidade de palvras acima de 5 letras: {quantidade_acima}")
print (f"Quantidade de palavras abaixo de 5 letras: {quantidade_abaixo}")
print (f"Quantidade de palavras começadas com a letra A: {palavras_A}")
print (f"Quantidade de palavras começadas com a letra B :{palavras_B}")
print (f"Maior palavra: {maior_palavra}")
print (f"Menor palavra: {menor_palavra}")

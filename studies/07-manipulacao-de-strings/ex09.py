frase = input("Digite uma frase: ").lower()
print (f"A frase é: {frase}")

palavra = input("Digite uma palavra da frase: ").lower()
print (f"A palavra é: {palavra}")

print (f"a palavra: \"{palavra}\" aparece na posição {frase.find(palavra)} da frase: \"{frase}\"")
print("===== QUESTIONÁRIO PARA HABILITAÇÃO =====")
print("Digite True para sim e False para não.")
print()
idade = int(input("Qual a sua idade?"))
tem_carteira = input("Tem carteira? (True/False): ") == "True"
maior_de_idade= idade >= 18
pode_dirigir = maior_de_idade and tem_carteira 


print(f"=========RESULTADO=========")
print(f"Maior de idade: {maior_de_idade}")
print(f"Tem carteira: {tem_carteira}") 
print(f"Pode dirigir: {pode_dirigir}")
print(f"===========================")

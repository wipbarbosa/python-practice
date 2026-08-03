produtos = {
    "arroz": 25.50,
    "feijao": 8.00,
    "macarrao": 6.50,
    "leite": 5.00
}

while  True:

    print(f"Sua lista de produtos é: {produtos}")

    print(
            
            f"1 - Mostrar todos os produtos e preços.\n"
            f"2 - Adicionar um novo produto.\n"
            f"3 - Alterar o preço de um produto existente.\n"
            f"4 - Mostrar somente os nomes dos produtos.\n"
            f"5 - Mostrar somente os preços.\n"
            f"6 - Calcular o valor total dos produtos.\n"
            f"7 - Encontrar o produto mais caro.\n"
            f"8 - Encontrar o produto mais barato.\n"
            f"9 - Sair"
        )
    entrada =  int(input(f"Digite a opção desejada:"))

    if entrada == 1:
        for produto, preço in produtos.items():
            print(f"Produto: {produto} Preço: {preço}")

    if entrada == 2:
        nome = input(f"Digite o nome do produto que deseja adicionar")
        novo_preço = float(input(f"Digite o preço do novo produto"))

        produtos[nome] = novo_preço

    if entrada == 3:
        produto_preco_novo = input(f"Digite o nome do produto a ser alterado")

        if produto_preco_novo in produtos:
            novo_preço = float(input("Digite o novo preço"))

            produtos[produto_preco_novo] = novo_preço
        else:
            print("produto não econtrado")

    if entrada == 4:
        for produto in produtos.keys():
            print(produto)

    if entrada == 9:
        break
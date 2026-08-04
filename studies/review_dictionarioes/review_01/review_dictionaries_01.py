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

    elif entrada == 2:
        nome = input(f"Digite o nome do produto que deseja adicionar")
        novo_preço = float(input(f"Digite o preço do novo produto"))

        produtos[nome] = novo_preço

    elif entrada == 3:
        produto_preco_novo = input(f"Digite o nome do produto a ser alterado")

        if produto_preco_novo in produtos:
            novo_preço = float(input("Digite o novo preço"))

            produtos[produto_preco_novo] = novo_preço
        else:
            print("produto não econtrado")

    elif entrada == 4:
        for produto in produtos.keys():
            print(produto)

    elif entrada == 5:
        for preço in produtos.values():
            print(preço)

    elif entrada == 6:
        valortotal = 0
        
        for preço in produtos.values():
            valortotal += preço

        print(f"Valor total dos produtos: R$ {valortotal:.2f}")

    elif entrada == 7:
        maior_valor = 0
        for produto, preço in produtos.items():
            if preço > maior_valor:
                maior_valor = preço
                produto_mais_caro = produto

        print(f"Produto mais caro: {produto_mais_caro}")
        print(f"Preço: R$ {maior_valor:.2f}")

    elif entrada == 8:
        menor_valor = None
        for produto, preço in produtos.items():
            if menor_valor is None or preço < menor_valor:
                menor_valor = preço
                produto_mais_barato = produto

        print(f"Produto mais barato: {produto_mais_barato}")
        print(f"Preço: R$ {menor_valor:.2f}")

    elif entrada == 9:
        break
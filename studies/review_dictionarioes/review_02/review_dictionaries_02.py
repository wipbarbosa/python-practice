alunos = []

while True:

    print (
        f"===== SISTEMA DE ALUNOS ====\n"

        f"1 - Cadastrar aluno\n"
        f"2 - Mostrar todos os alunos\n"
        f"3 - Mostrar somente os nomes\n"
        f"4 - Calcular média das notas\n"
        f"5 - Mostrar aluno com maior nota\n"
        f"6 - Mostrar aluno com menor nota\n"
        f"7 - Procurar aluno pelo nome\n"
        f"8 - Mostrar alunos aprovados\n"
        f"9 - Sair"
        )

    entrada = int(input(f"Escreva a opção desejada: "))
    while entrada < 1 or entrada > 9:
        entrada = int(input("Entrada inválida, tente novamente: "))

    if entrada == 1:
        print("-" * 20)

        print("Cadastro de novo aluno")

        print("-" * 20)

        novo_aluno = input("Escreva o nome do novo aluno: ").lower()

        while novo_aluno == "":
            novo_aluno = input("Escreva o nome do novo aluno").lower()

        idade_novo_aluno = int(input("Digite a idade do novo aluno: "))

        while idade_novo_aluno <= 0:
            idade_novo_aluno = int(input("Idade inválida,Digite uma idade válida"))

        nota_novo_aluno = float(input("Digite a nota do novo aluno: "))

        while nota_novo_aluno < 0 or nota_novo_aluno > 10:
            nota_novo_aluno  = float(input("Nota inválida! Digite uma nota entre 0 e 10: "))

        aluno = {
            "nome": novo_aluno,
            "idade": idade_novo_aluno,
            "nota": nota_novo_aluno
        }

        alunos.append(aluno)

    elif entrada == 2:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:

            for aluno in alunos:
                print (f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")

    elif entrada == 3:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
        else:
            for aluno in alunos:
                print(
                    f"Lista de alunos: \n"
                    f"Nome: {aluno['nome']}")

    elif entrada == 4:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:
            
            contador = 0
            media = 0

            for aluno in alunos:
                contador += 1
                media += aluno["nota"]

            media = media / contador

            print(f"Média das notas: {media:.2f}")

    elif entrada == 5:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:

            maior_nota = 0
            aluno_maior_nota = None

            for aluno in alunos:
                if aluno['nota'] > maior_nota:
                    maior_nota = aluno['nota']
                    aluno_maior_nota = aluno['nome']

            print(f"A maior nota Registrada é {maior_nota} do aluno {aluno_maior_nota}")

    elif entrada == 6:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:

            menor_nota = 10
            aluno_menor_nota = None

            for aluno in alunos:
                if aluno['nota'] < menor_nota:
                    menor_nota = aluno['nota']
                    aluno_menor_nota = aluno['nome']

            print(f"A menor nota Registrada é {menor_nota} do aluno {aluno_menor_nota}")

    elif entrada == 7:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:
            busca_aluno = input("Nome do aluno:").lower()
            aluno_encontrado = False

            for aluno in alunos:
                if busca_aluno == aluno['nome']:
                    print(
                        f"Aluno cadastrado\n"
                        f"Nome: {aluno['nome']}\n"
                        f"Idade: {aluno['idade']}\n"
                        f"Nota: {aluno['nota']}\n"
                    )

                    aluno_encontrado = True


            if not aluno_encontrado:
                print("Aluno não cadastrado")

    elif entrada == 8:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)

        else:
            aprovado_encontrado = False
            for aluno in alunos:

                if aluno["nota"] >= 6:
                    aprovado_encontrado = True
                    print(
                        f"Nome: {aluno['nome']}\n"
                        f"Idade: {aluno['idade']}\n"
                        f"Nota: {aluno['nota']}\n"
                        f"Situação: Aprovado"
                        print("-" * 20)"
                )
            if not aprovado_encontrado:
                print("Sem alunos aprovados")
                print("-" * 20)

    elif entrada == 9:
        print("programa encerrado.")
        break                
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
    print("=" * 30)

    entrada = int(input(f"Selecione a opção: "))
    while entrada < 1 or entrada > 9:
        entrada = int(input("Entrada inválida, tente novamente: "))

    if entrada == 1:
        print("-" * 20)

        print("===== CADASTRO DE NOVO ALUNO =====")

        novo_aluno = input("Escreva o nome do novo aluno: ").lower()
        print("-" * 20)

        while novo_aluno == "":
            novo_aluno = input("Escreva o nome do novo aluno").lower()
            print("-" * 20)

        idade_novo_aluno = int(input("Digite a idade do novo aluno: "))
        print("-" * 20)

        while idade_novo_aluno <= 0:
            idade_novo_aluno = int(input("Idade inválida,Digite uma idade válida"))
            print("-" * 20)

        nota_novo_aluno = float(input("Digite a nota do novo aluno: "))
        print("-" * 20)

        while nota_novo_aluno < 0 or nota_novo_aluno > 10:
            nota_novo_aluno  = float(input("Nota inválida! Digite uma nota entre 0 e 10: "))
            print("-" * 20)

        aluno = {
            "nome": novo_aluno,
            "idade": idade_novo_aluno,
            "nota": nota_novo_aluno
        }

        alunos.append(aluno)
        print(f"===== ALUNO CADASTRADO COM SUCESSO =====")
        print("=" * 30)

    elif entrada == 2:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:

            for aluno in alunos:
                print(f"===== LISTA DE ALUNOS CADASTRADOS =====\n")
                print (f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}\n")
                print("=" * 30)

    elif entrada == 3:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:
            for aluno in alunos:
                print(
                    f"===== NOMES DE ALUNOS CADASTRADOS =====: \n"
                    f"Nome: {aluno['nome']}")
                print("=" * 30)

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
            print(f"===== MÉDIA DE NOTAS =====")
            print(f"Média das notas: {media:.2f}")
            print("=" * 30)

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
            print("=" * 30)

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
            print("=" * 30)

    elif entrada == 7:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)
        else:
            print("===== BUSCA ALUNO PELO NOME =====")
            busca_aluno = input("Nome do aluno:").lower()
            print("-" * 20)
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
                    print("=" * 30)


            if not aluno_encontrado:
                print("Aluno não cadastrado")
                print("=" * 30)

    elif entrada == 8:
        if len(alunos) == 0:
            print("Sem alunos cadastrados")
            print("-" * 20)

        else:
            print("===== LISTA DE ALUNOS APROVADOS =====")
            aprovado_encontrado = False
            for aluno in alunos:

                if aluno["nota"] >= 6:
                    aprovado_encontrado = True
                    print(
                        f"Nome: {aluno['nome']}\n"
                        f"Idade: {aluno['idade']}\n"
                        f"Nota: {aluno['nota']}\n"
                        f"Situação: Aprovado"
                        )
                    print("-" * 20)

            if not aprovado_encontrado:
                print("Sem alunos aprovados")
                print("-" * 20)

    elif entrada == 9:
        print("programa encerrado.")
        break                
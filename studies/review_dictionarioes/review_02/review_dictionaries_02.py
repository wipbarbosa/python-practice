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
    while entrada < 1 or entrada > 10:
        entrada = int(input("Entrada inválida, tente novamente: "))

    if entrada == 1:
        print("Cadastro de novo aluno")

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
 
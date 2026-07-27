tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Ordenar tarefas")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nSuas tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa para remover.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")

            numero = int(input("Digite o número da tarefa que deseja remover: "))

            if numero >= 1 and numero <= len(tarefas):
                removida = tarefas.pop(numero - 1)
                print(f"Tarefa removida: {removida}")
            else:
                print("Número de tarefa inválido.")

    elif opcao == "4":
        tarefas.sort()
        print("Tarefas ordenadas!")            

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
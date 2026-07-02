from tarefas import GerenciadorTarefas

sistema = GerenciadorTarefas()

while True:

    print("\n===== MENU =====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Digite a tarefa: ")
        sistema.criar(nome)

    elif opcao == "2":

        tarefas = sistema.listar()

        if len(tarefas) == 0:
            print("Sem tarefas")

        for tarefa in tarefas:
            print("-", tarefa)

    elif opcao == "3":

        nome = input("Digite tarefa para remover: ")
        sistema.remover(nome)

    elif opcao == "4":

        print("Sistema encerrado")
        break
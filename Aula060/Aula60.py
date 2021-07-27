"""
    Exercício - Undo e Redo
"""
tarefas = []
while True:
    opcao = input('[1] = Adicionar tarefa\n'
                  '[2] = Lista tarefas?\n'
                  '[3] = Desfazer Tarefa\n'
                  '[4] = Refazer Tarefa\n')
    if opcao == '1':
        nova_tarefa = input('Adicionar tarefa ')
        tarefas.append(nova_tarefa)
    elif opcao == '2':
        print(sorted(tarefas))
    elif opcao == '3':
        if not tarefas:
            print('Nada a desfazer')
        else:
            tarefas.remove(nova_tarefa)
    elif opcao == '4':
        tarefas.append(nova_tarefa)



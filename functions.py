def show_op(todo_list):
    print()
    print()
    print('Tarefas: ')
    for i in todo_list:
        print(i)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer!')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)

def do_add(todo, todo_list):
    todo_list.append(todo)




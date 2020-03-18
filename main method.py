from functions import  do_add,do_redo,do_undo,show_op

if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa, undo para desfazer, redo para refazer, ls para mostrar e quit para sair: ')
        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue
        elif todo == 'quit':
            break

        do_add(todo, todo_list)
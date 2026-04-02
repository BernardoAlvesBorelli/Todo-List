import funcs
import sys

def print_lista(t):
    print("=================================================")
    print(f"ID: {t["id"]}")
    print(f"Descrição: {t["description"]}")
    print(f"Status: {t["status"]}")
    print(f"Criado Em: {t["createdAt"]}")
    print(f"Atualizado em: {t["updatedAt"]}")
    print("=================================================")

def help_screen(fase="start"):
    if fase == "start":
        print("""--- TO-DO LIST ---
Forma de uso:
python todo.py [argumentos]

Argumentos:
list                - lista as tarefas
list todo           - mostra as tarefas ainda não realizadas
list in-progress    - mostra as tarefas em progresso
list done           - mostra as tarefas terminadas
add "tarefa"        - adiciona uma tarefa
update id "tarefa"  - atualiza o nome da tarefa 
mark-in-progress id - atualiza a tarefa como em progresso
mark-done id        - atualiza a tarefa como terminada
delete id           - remove a tarefa""")
        
    if fase == "add":
        print("Forma de uso:\nadd \"tarefa\"")
    
    if fase == "update":
        print("Forma de uso:\nupdate id \"tarefa\"")

    if fase == "progress":
        print("Forma de uso:\nmark-in-progress id")
    
    if fase == "done":
        print("Forma de uso:\nmark-done id")

    if fase == "delete":
        print("Forma de uso:\ndelete id")

todolist = funcs.ToDoList()

if len(sys.argv) < 2:
    help_screen("start")

elif sys.argv[1] == "list":
    lista = todolist.read_file()
    if len(sys.argv) == 2:
        for t in lista:
            print_lista(t)
    elif len(sys.argv) > 2:
        if sys.argv[2] == "todo":
            for t in lista:
                if t["status"] == "todo":
                    print_lista(t)
        elif sys.argv[2] == "in-progress":
            for t in lista:
                if t["status"] == "in-progress":
                    print_lista(t)
        elif sys.argv[2] == "done":
            for t in lista:
                if t["status"] == "done":
                    print_lista(t)
        else:
            for t in lista:
                print_lista(t)

elif sys.argv[1] == "add":
    if len(sys.argv) == 3:
        todolist.add_task(sys.argv[2], "todo")
    else:
        help_screen("add")

elif sys.argv[1] == "update":
    if len(sys.argv) == 4:
        todolist.update_task_desc(sys.argv[2], sys.argv[3])
    else:
        help_screen("update")

elif sys.argv[1] == "mark-in-progress":
    if len(sys.argv) == 3:
        todolist.update_task_status(sys.argv[2], "in-progress")
    else:
        help_screen("progress")

elif sys.argv[1] == "mark-done":
    if len(sys.argv) == 3:
        todolist.update_task_status(sys.argv[2], "done")
    else:
        help_screen("done")

elif sys.argv[1] == "delete-done":
    if len(sys.argv) == 3:
        todolist.remove_task(sys.argv[2])
    else:
        help_screen("delete")
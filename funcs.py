import json
import datetime
import os

class ToDoList:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_dir, "todolist.json")
        self.lista = []
        self.load_file()

    def load_file(self):
        if not os.path.exists(self.filename):
            self.write_file()
        else:
            self.lista = self.read_file()

    def write_file(self):
        listfile = open(self.filename, "wt")
        listfile.write(json.dumps(self.lista))
        listfile.close()

    def read_file(self):
        listfile = open(self.filename, "rt")
        try:
            with open(self.filename, "rt") as listfile:
                # json.load (sem 's') lê o ARQUIVO, não a STRING do nome
                self.lista = json.load(listfile)
        except (json.JSONDecodeError, FileNotFoundError):
            self.lista = []
        return self.lista

    def add_task(self, description, status):
        actual_datetime = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        task = {"id": max((t["id"] for t in self.lista), default=0) + 1, "description": description, "status": status, "createdAt": actual_datetime, "updatedAt": actual_datetime}
        self.lista.append(task)
        self.write_file()
        print("Tarefa criada com sucesso!")

    def update_task_status(self, id, status):
        actual_datetime = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        exists = False
        for t in self.lista:
            if t["id"] == int(id):
                t["status"] = status
                t["updatedAt"] = actual_datetime
                exists = True
        if exists:
            self.write_file()
            print("Tarefa atualizada com sucesso!")
        else:
            error_msg("ERRO! Tarefa não encontrada!")

    def update_task_desc(self, id, description):
        actual_datetime = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        exists = False
        for t in self.lista:
            if t["id"] == int(id):
                t["description"] = description
                t["updatedAt"] = actual_datetime
                exists = True
        if exists:
            self.write_file()
            print("Tarefa atualizada com sucesso!")
        else:
            error_msg("ERRO! Tarefa não encontrada!")

    def remove_task(self, id):
        original_len = len(self.lista)
        lista_nova = []
        for t in self.lista:
            if t["id"] != int(id):
                lista_nova.append(t)
        
        self.lista = lista_nova
        
        if len(self.lista) < original_len:
            self.write_file()
            print("Tarefa removida com sucesso!")
        else:
            error_msg("ERRO! Tarefa não encontrada!")


def error_msg(msg):
    print(f"\033[31m{msg}\033[m")

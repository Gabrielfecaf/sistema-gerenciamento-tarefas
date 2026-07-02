class GerenciadorTarefas:

    def __init__(self):
        self.tarefas = []

    def criar(self, nome):
        self.tarefas.append(nome)

    def listar(self):
        return self.tarefas

    def remover(self, nome):
        if nome in self.tarefas:
            self.tarefas.remove(nome)
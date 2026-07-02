from src.tarefas import GerenciadorTarefas

def test_criar_tarefa():
    sistema = GerenciadorTarefas()
    sistema.criar("Estudar Python")
    assert "Estudar Python" in sistema.listar()

def test_remover_tarefa():
    sistema = GerenciadorTarefas()
    sistema.criar("Teste")
    sistema.remover("Teste")
    assert "Teste" not in sistema.listar()
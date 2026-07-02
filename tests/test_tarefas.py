import sys
import os

# Adiciona o caminho da pasta 'src' ao sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tarefas import GerenciadorTarefas

def test_criar_tarefa():
    sistema = GerenciadorTarefas()
    sistema.criar("Estudar Python")
    assert "Estudar Python" in sistema.listar()

def test_remover_tarefa():
    sistema = GerenciadorTarefas()
    sistema.criar("Teste")
    sistema.remover("Teste")
    assert "Teste" not in sistema.listar()
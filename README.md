# Sistema de Gerenciamento de Tarefas

Projeto desenvolvido em Python para a disciplina de Controle de Código-Fonte.

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Remover tarefas
- Encerrar o sistema

## Tecnologias utilizadas

- Python 3
- Pytest
- Git
- GitHub

## Estrutura do projeto

```
sistema-gerenciamento-tarefas/
│
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
├── src/
│   ├── app.py
│   └── tarefas.py
├── tests/
│   └── test_tarefas.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Como executar

1. Abra o terminal.
2. Entre na pasta `src`.

```
cd src
```

3. Execute o programa.

```
python app.py
```

## Como executar os testes

Na pasta principal do projeto execute:

```
pytest
```

## Autor

Gabriel de Souza Cordeiro

## Exemplo de execução

```
====== MENU ======

1 - Criar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Sair
```
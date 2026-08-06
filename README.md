# Expenses Project

## Estrutura do projeto

- `main.py`
  - Interface gráfica construída com Tkinter.
  - Contém a janela principal, frames, botões, formulários e chamadas para inserir/excluir dados.
  - Cria funções de interação como `inserir_categoria`, `inserir_receitas`, `inserir_despesas`, `deletar_dados`, `percent`, `graphc_bar`, `summary`.

- `view.py`
  - Contém funções de acesso ao banco de dados e geração de dados para exibição.
  - Funções de inserção: `insert_category`, `insert_recipe`, `insert_expenses`.
  - Funções de exclusão: `delete_recipe`, `delete_expenses`.
  - Funções de leitura: `show_category`, `show_recipe`, `show_expenses`, `table`, `bar_value`, `pie_values`, `percent_value`.
  - Usa SQLite (`sqlite3`) e pandas para agregar valores de gráfico.

- `criardb.py`
  - Script de criação do banco de dados SQLite (`dados.db`).
  - Cria as tabelas `Categoria`, `Receitas` e `Gastos`.

- `dados.db`
  - Base de dados SQLite usada pela aplicação.

- `imagens/`
  - Diretório de ativos visuais usados na interface.

- `teste.py`
  - Arquivo presente no projeto; função específica não revisada neste documento.

## Principais funcionalidades

- Cadastro de categorias de despesas.
- Registro de receitas com data e valor.
- Registro de gastos com categoria, data e valor.
- Exclusão de receitas ou despesas selecionadas na tabela.
- Exibição de resultados em gráficos:
  - gráfico de barras para receita, despesas e saldo.
  - gráfico de pizza para distribuição de despesas por categoria.
- Cálculo de porcentagem de receita restante e valores totais.

## Banco de dados

- Tabela `Categoria`:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  - `nome` (TEXT)

- Tabela `Receitas`:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  - `categoria` (TEXT)
  - `adicionado_em` (DATE)
  - `valor` (DECIMAL)

- Tabela `Gastos`:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  - `categoria` (TEXT)
  - `retirado_em` (DATE)
  - `valor` (DECIMAL)



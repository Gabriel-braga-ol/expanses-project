import sqlite3 as lite

con = lite.connect('dados.db')

# Criando a tabela categoria
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)"
    )

# Criando a tabela receitas
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionando_em DATE, valor DECIMAL)"
    )

# Criando a tabela gastos
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)"
    )

import sqlite3 as lite

con = lite.connect('dados.db')

#funções de inserção
#inserindo categoria
def insert_category(nome):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, nome)
        # cur.execute("DELETE FROM Categoria WHERE nome = 1") 

# Inserindo receitas        
def insert_recipe(nome):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, nome)

# Inserindo gastos        
def insert_recipe(nome):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, nome)

# funções para deletar
def delete_recipe(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id = ?"
        cur.execute(query, i)

# função para deletar gastos
def delete_expenses(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id = ?"
        cur.execute(query, i)

# Funções para ver dados

# ver categoria
def show_category():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver receitas
def show_recipe():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver gastos
def show_expenses():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# função para ver dados do gráfico de barra
def bar_value():
    receitas = show_recipe()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])
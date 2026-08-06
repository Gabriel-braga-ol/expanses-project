import sqlite3 as lite
import pandas as pd 

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
def insert_expenses(nome):
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

# função para dados da tabela
def table():
    expenses = show_expenses()
    recipes = show_recipe()

    table_list = []

    for i in expenses:
        table_list.append(i)

    for i in recipes:
        table_list.append(i)

    return table_list

# função para ver dados do gráfico de barra
def bar_value():
    # pegando a receita total
    receitas = show_recipe()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3]) # pegando o valores da coluna valor da tabela receitas

    receitas_total = sum(receitas_lista)

    # despesa total
    gastos = show_expenses()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3]) # pegando o valores da coluna valor da tabela gostas

    gasto_total = sum(gastos_lista)

    saldo_total = receitas_total - gasto_total

    return [receitas_total, gasto_total, saldo_total]

# função grafico pie
def pie_values():
    gastos = show_expenses()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i)

    dataframe = pd.DataFrame(gastos_lista, columns= ['id', 'Categoria', 'Data', 'Valor'])
    dataframe = dataframe.groupby('Categoria')['Valor'].sum()

    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return ([lista_categorias, lista_quantias])

# função para ver dados do gráfico de porcentagem
def percent_value():
    pct = show_recipe()
    pct_lista = []

    for i in pct:
        pct_lista.append(i[3]) 

    receitas_total = sum(pct_lista)

    # despesa total
    gastos = show_expenses()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3]) 

    gasto_total = sum(gastos_lista)

    total = ((receitas_total - gasto_total) / gasto_total) * 100

    return [total]
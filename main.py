from tkinter import *
from tkinter import Tk, ttk

# Importando pillow
from PIL import Image, ImageTk
#Importando barra de progresso do Tkinter
from tkinter.ttk import Progressbar

# Importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#ffffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#crinado uma janela vazia
janela = Tk()
janela.title()
janela.geometry('900x650') #largura e altura
janela.configure(background='#e9edf5')

janela.resizable(width=False, height=False) # permite mudar a largura e altura com o mouse
style = ttk.Style(janela)
style.theme_use('clam')

# criando frames para divisão da tela
frame_cima = Frame(janela, width=1043, height=50, background=co1, relief='flat')
frame_cima.grid(row=0, column=0) #cabeçalho

frame_meio = Frame(janela, width=1043, height=361, background='#e9edf5', pady=20, relief='raised')
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW) #meio

frame_baixo = Frame(janela, width=1043, height=00, background='#e9edf5', relief='flat')
frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW) #rodapé

frame_graphc_pie = Frame(frame_meio, width=580, height=250, background='#e9edf5')
frame_graphc_pie.place(x=435, y=5)

# Trabalhando no frame cima - acessando imagem

app_img = Image.open('imagens/log.png')
app_img = app_img.resize((45,45)) #redimensiona a imagem(largura,altura)
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief='raised', anchor=NW, font=('verdana 20 bold'), background='#ffffff', fg='#000000')
app_logo.place(x=0,y=0)
app_logo.Image = app_img # guardando a imagem em uma variável para não sumir
 
# barra percentagem

def percent():
    progress_bar = Label(frame_meio, text='Porcentagem da receita gasta', height=1, anchor=NW, font=('verdana 12'), background='#e9edf5', fg=co0)
    progress_bar.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("color.Horizontal.TProgressbar", background='#e06636') # "nome_estilo.Horizontal.TProgress" ou "nome_estilo.vertical.TProgress"
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frame_meio, length=180, style='color.Horizontal.TProgressbar')

    bar.place(x=10,y=35)
    bar['value'] = 50

    valor = 50

    pct = Label(frame_meio, text="{:,.2f}%".format(valor), anchor=NW, font=('verdana 12'), background='#e9edf5', fg=co0)
    pct.place(x=200, y=38)

# gráfico de barras usando o matplotlib

def graphc_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6236]

    # Criando a figura
    figura = plt.Figure(figsize=(4, 3.45), dpi=60, facecolor='#e9edf5')
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    # create a list to collect the plt.patches data

    # adicionando valor em cima da barra
    c = 0
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='black')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16) #define os rótulos mostrados no eixo X

    ax.patch.set_facecolor('#e9edf5')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=10, y=70)


# Função de resumo total
def summary():
    valor = [500, 600, 480]

    l_linha = Label(frame_meio, text='', width=215, height=1, anchor=NW, font=('Arial 1'), background='#545454')
    l_linha.place(x=309, y=52)
    l_linha2 = Label(frame_meio, text='Total Renda Mensal     '.upper(), anchor=NW, font=('Verdana 12'), background='#e9edf5', foreground='#83a9e6')
    l_linha2.place(x=309, y=35)
    l_linha3 = Label(frame_meio, text=f'R$ {valor[0]:,.2f}', anchor=NW, font=('Arial 17'), background='#e9edf5', foreground='#545454')
    l_linha3.place(x=309, y=70)

    l_linha4 = Label(frame_meio, text='', width=215, height=1, anchor=NW, font=('Arial 1'), background='#545454')
    l_linha4.place(x=309, y=132)
    l_linha5 = Label(frame_meio, text='Total despesas mensais'.upper(), anchor=NW, font=('Verdana 12'), background='#e9edf5', foreground='#83a9e6')
    l_linha5.place(x=309, y=115)
    l_linha6 = Label(frame_meio, text=f'R$ {valor[1]:,.2f}', anchor=NW, font=('Arial 17'), background='#e9edf5', foreground='#545454')
    l_linha6.place(x=309, y=150)
    
    l_linha7 = Label(frame_meio, text='', width=215, height=1, anchor=NW, font=('Arial 1'), background='#545454')
    l_linha7.place(x=309, y=207)
    l_linha8 = Label(frame_meio, text='Total saldo da caixa   '.upper(), anchor=NW, font=('Verdana 12'), background='#e9edf5', foreground='#83a9e6')
    l_linha8.place(x=309, y=190)
    l_linha9 = Label(frame_meio, text=f'R$ {valor[2]:,.2f}', anchor=NW, font=('Arial 17'), background='#e9edf5', foreground='#545454')
    l_linha9.place(x=309, y=220)


# função gráfico pie
def graphc_pie():
    figura = plt.Figure(figsize=(5, 3), dpi=90, facecolor='#e9edf5')
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_graphc_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


percent()
graphc_bar()
summary()
graphc_pie()

# Criando frames dentro do frame_baixo

frame_renda = Frame(frame_baixo, width=300, height=250, background=co1, relief='flat')
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frame_baixo, width=220, height=250, background=co1, relief='flat')
frame_operacoes.grid(row=0, column=1, padx=0)

frame_configuracoes = Frame(frame_baixo, width=220, height=250, background=co1, relief='flat')
frame_configuracoes.grid(row=0, column=2, padx=0)

# Tabela renda mensal
app_tabela = Label(frame_meio, text='Tabela de receitas e despesas', anchor=NW, font=('Verdana 12'), background='#e9edf5', foreground=co0) 
app_tabela.place(x=5, y=309)

# Função para mostrar tabela
def show_table():
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

show_table()

janela.mainloop() # mostrar na tela?

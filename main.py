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
co1 = "#feffff"  # branca
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
frame_cima = Frame(janela, width=1043, height=50, background='#808080', relief='flat')
frame_cima.grid(row=0, column=0) #cabeçalho

frame_meio = Frame(janela, width=1043, height=361, background='#808080', pady=20, relief='raised')
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW) #meio

frame_baixo = Frame(janela, width=1043, height=00, background='#808080', relief='flat')
frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW) #rodapé

# Trabalhando no frame cima - acessando imagem

app_img = Image.open('imagens/log.png')
app_img = app_img.resize((45,45)) #redimensiona a imagem(largura,altura)
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief='raised', anchor=NW, font=('verdana 20 bold'), background='#ffffff', fg='#000000')
app_logo.place(x=0,y=0)
app_logo.Image = app_img # guardando a imagem em uma variável para não sumir
 
# barra percentagem

def percent():
    progress_bar = Label(frame_meio, text='Porcentagem da receita gasta', height=1, anchor=NW, font=('verdana 12'), background='#808080', fg=co1)
    progress_bar.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("color.Horizontal.TProgressbar", background='#e06636') # "nome_estilo.Horizontal.TProgress" ou "nome_estilo.vertical.TProgress"
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frame_meio, length=180, style='color.Horizontal.TProgressbar')

    bar.place(x=10,y=35)
    bar['value'] = 50

    valor = 50

    pct = Label(frame_meio, text="{:,.2f}%".format(valor), anchor=NW, font=('verdana 12'), background='#808080', fg=co1)
    pct.place(x=200, y=38)

# gráfico de barras usando o matplotlib

def graphc_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6236]

    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    # create a list to collect the plt.patches data

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
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
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=10, y=70)


percent()
graphc_bar()
janela.mainloop() # mostrar na tela?

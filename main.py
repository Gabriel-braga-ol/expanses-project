from tkinter import *
from tkinter import Tk, ttk

# Importando pillow
from PIL import Image, ImageTk


colors = []

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
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=1043, height=361, background='#808080', pady=20, relief='raised')
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1043, height=00, background='#808080', relief='flat')
frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

# Trabalhando no frame cima - acessando imagem

app_img = Image.open('imagens/log.png')
app_img = app_img.resize((45,45)) #reduzindo o tamanho da imagem(largura,altura)
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text=" Orçamento pessoal", width=900, compound=LEFT, padx=5, relief='raised', anchor=NW, font=('verdana 20 bold'), background='#ffffff', fg='#000000')
app_logo.place(x=0,y=0)
 


janela.mainloop() # mostrar na tela?

    # lista_categorias = ['Renda', 'Despesas', 'Saldo']
    # lista_valores = [3000, 2000, 6236]

    # # Criando a figura
    # figura = plt.Figure(figsize=(4, 3.45), dpi=60, facecolor='#808080')
    # ax = figura.add_subplot(111)
    # # ax.autoscale(enable=True, axis='both', tight=None)

    # ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    # # create a list to collect the plt.patches data

    # # adicionando valor em cima da barra
    # c = 0
    # for i in ax.patches:
    #     # get_x pulls left or right; get_height pushes up or down
    #     ax.text(i.get_x()-.001, i.get_height()+.5,
    #             str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='black')
    #     c += 1

    # ax.set_xticklabels(lista_categorias,fontsize=16) #define os rótulos mostrados no eixo X

    # ax.patch.set_facecolor('#808080')
    # ax.spines['bottom'].set_color('#CCCCCC')
    # ax.spines['bottom'].set_linewidth(1)
    # ax.spines['right'].set_linewidth(0)
    # ax.spines['top'].set_linewidth(0)
    # ax.spines['left'].set_color('#CCCCCC')
    # ax.spines['left'].set_linewidth(1)

    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # ax.tick_params(bottom=False, left=False)
    # ax.set_axisbelow(True)
    # ax.yaxis.grid(False)
    # ax.xaxis.grid(False)

    # canva = FigureCanvasTkAgg(figura, frame_meio)
    # canva.get_tk_widget().place(x=10, y=70)

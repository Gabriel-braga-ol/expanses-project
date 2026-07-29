class Expanses:
    def __init__(self):
        self.gastos = []

def menu():
    print('1. Adicionar despesas')
    print('2. Atualizar despesas')
    print('4. deletar despesas')
    print('3. Vizualizar todas despesas')
    print('5. Resumo das despesas')
    print('6. Resume das despesas (Mês específico)')
    print('7. Sair')

def add(self):
    produto = str(input('Insira o produto'))
    valor = float(input('Insira o valor: '))
    data = str(input('Insira a data da compra: '))

    novo_gasto = {'Produto': produto, 'Valor': valor, 'data': data}
    self.gastos.append(novo_gasto)

def update(self):
    pass


def delete():
    pass

def show():
    pass
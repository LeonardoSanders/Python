import math
import os
from tkinter import *

class VendingMachine:
    def __init__(self, num_itens, item_price):
        self.num_itens = num_itens
        self.item_price = item_price
        
    def buy(self, req_items=7, money=100):
        coins = money
        
        if req_items > self.num_itens:
            raise ValueError('Not enough items in the machine')
        if req_items <= self.num_itens and coins < (self.item_price * req_items):
            raise ValueError('Not enough coins')
        
        for i in range(req_items):
            if self.num_itens >= 1 and coins >= self.item_price:
                self.num_itens -= 1
                coins -= self.item_price
            
        texto_resultado['text'] = f'Seu troco é R$ {coins}'
    

vd = VendingMachine(10, 2)
# result = vd.buy(7, 100)
# print(result)


janela = Tk()
janela.title("Máquina de Venda")
janela.geometry('400x400')

descricao1 = Label(janela, text='Temos 10 Salgadinhos disponíveis a R$ 2.')
descricao1.grid(column=0, row=0, padx=10, pady=10)

descricao2 = Label(janela, text='Você deseja comprar 7 Salgadinhos com R$ 100.')
descricao2.grid(column=0, row=1, padx=10, pady=10)

descricao3 = Label(janela, text='Clique no botão para comprar!')
descricao3.grid(column=0, row=2, padx=10, pady=10)

texto_resultado = Label(janela, text='')
texto_resultado.grid(column=0, row=4, padx=10, pady=10)

botao = Button(janela, text='Comprar Salgadinho', command=vd.buy)
botao.grid(column=0, row=3, padx=10, pady=10)



janela.mainloop()
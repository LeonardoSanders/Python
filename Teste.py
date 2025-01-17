import math
import os

class VendingMachine:
    def __init__(self, num_itens, item_price):
        self.num_itens = num_itens
        self.item_price = item_price
        
    def buy(self, req_items, money):
        coins = money
        
        if req_items > self.num_itens:
            raise ValueError('Not enough items in the machine')
        if req_items <= self.num_itens and coins < (self.item_price * req_items):
            raise ValueError('Not enough coins')
        
        for i in range(req_items):
            if self.num_itens >= 1 and coins >= self.item_price:
                self.num_itens -= 1
                coins -= self.item_price
            
             
        return coins
    

vd = VendingMachine(10, 2)
result = vd.buy(7, 100)
print(result)
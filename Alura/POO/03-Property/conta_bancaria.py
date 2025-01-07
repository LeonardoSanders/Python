class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return 'Conta ativa' if self._ativo else 'Conta inativa'
    
    @ativo.setter
    def ativo(self, status):
        self._ativo = status
    
    def __str__(self):
        return f'Olá {self._titular} seu Saldo Bancário é de R$ {self._saldo} e sua conta está {self.ativo}!'


p1 = ContaBancaria('João', 5000)
p2 = ContaBancaria('Pedro', 1500)
print(p1)
print(p2)
p3 = ContaBancaria('Lucas', 10000)
p3.ativo = True
print(p3)
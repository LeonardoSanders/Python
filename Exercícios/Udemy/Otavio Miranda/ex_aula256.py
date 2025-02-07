from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, saldo, limite, agencia, numero):
        self.saldo = saldo
        self.limite = limite
        self.agencia = agencia
        self.numero = numero

    @abstractmethod
    def sacar(self):
        pass

    def deposito(self, valor):
        self.saldo += valor
        return f'Depósito de {valor} realizado. Seu saldo atual é de R$ {self.saldo}'


class ContaCorrente(Conta):

    def sacar(self, saque, valor):
        if saque:
            if valor > self.saldo:
                print("O valor desejado excede o Saldo da Conta!")
            else:
                self.saldo - valor
                print(f'Saque de {valor} realizado. Seu saldo atual é de R$ {self.saldo}')
        else:
            print('Você nao tem autorizacao para sacar!')

    
class ContaPoupanca(Conta):

    def sacar(self, valor):
        if valor > self.saldo:
            print("O valor desejado excede o Saldo da Conta")
        else:
            self.saldo -= valor
            return f'Saque de {valor} realizado. Seu saldo atual é de R$ {self.saldo}'
    

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = []

    def definir_tipo_conta(self, *contas):
        for dados in contas:
            self.conta.append(dados)
        print(f'{self.conta[0].__class__.__name__} definida com sucesso!')

class Banco:

    def __init__(self, agencia, num_contas):
        self.agencia = agencia
        self.num_conta = num_contas
        self.clientes = []
        self.contas = []

    def definir_clientes(self, *clientes):
        for cliente in clientes:
            self.clientes.append(cliente)
        

    def definir_contas(self, *contas):
        for conta in contas:
            self.contas.append(conta)
        
    
    def autenticar(self, nome) -> bool:
        verificador = 0
        for conta in self.contas:
            if conta.agencia == self.agencia:
                verificador += 1
            if conta.numero == self.num_conta:
                verificador += 1
        for cliente in self.clientes:
            if cliente.nome == nome:
                verificador += 1
        if verificador == 3:
            print('Dados autenticados com sucesso. Saque autorizado!')
            return True
        else:
            print('Erro na autenticacão dos dados. Saque não autorizado!')
            return False



Cliente_1 = Cliente('Leonardo', 30)
conta_corrente_1 = ContaCorrente(2000, 5000, 2905, 921938)
Cliente_1.definir_tipo_conta(conta_corrente_1)
Banco_1 = Banco(2905, 921938)
Banco_1.definir_contas(conta_corrente_1)
Banco_1.definir_clientes(Cliente_1)
saque = Banco_1.autenticar(Cliente_1.nome)
conta_corrente_1.sacar(saque, 1000)
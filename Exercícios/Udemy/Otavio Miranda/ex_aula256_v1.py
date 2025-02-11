from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, saldo: float, agencia: int, numero: int):
        self.saldo = saldo
        self.agencia = agencia
        self.numero = numero

    @abstractmethod
    def sacar(self):
        pass

    def deposito(self, valor) -> float:
        self.saldo += valor
        print(f'Depósito de {valor} realizado. Seu saldo atual é de R$ {self.saldo}!')
        return self.saldo


class ContaCorrente(Conta):

    def __init__(self, saldo, agencia, numero, limite=1000):
        super().__init__(saldo, agencia, numero)
        self.limite = limite
    
    def dados_conta(self):
        print(f'Conta Corrente, n. {self.numero}, ag. {self.agencia}')
        print(f'Saldo correntista: {self.saldo}')

    def sacar(self, saque, valor) -> float:
        saldo = self.saldo - valor
        limite_maximo = -self.limite

        if saque:
            if saldo >= limite_maximo:
                self.saldo -= valor
                print(f'Saque de {valor} realizado. Seu saldo atual é de R$ {self.saldo}!')
                return self.saldo
            else:
                print("O valor desejado excede o Limite de Saque da Conta!")
        else:
            print('Você nao tem autorizacao para sacar!')

    
class ContaPoupanca(Conta):

    def sacar(self, saque, valor) -> float:
        saldo = self.saldo
        if saque:
            if valor > self.saldo:
                print("O valor desejado excede o Saldo da Conta!")
            else:
                self.saldo = saldo - valor
                print(f'Saque de {valor} realizado. Seu saldo atual é de R$ {self.saldo}!')
                return self.saldo
        else:
            print('Você nao tem autorizacao para sacar!')
    

class Pessoa:

    def __init__(self, nome: str, idade: int):
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
conta_corrente_1 = ContaCorrente(2000, 2905, 921938)
Cliente_1.definir_tipo_conta(conta_corrente_1)
Banco_1 = Banco(2905, 921938)
Banco_1.definir_contas(conta_corrente_1)
Banco_1.definir_clientes(Cliente_1)
conta_corrente_1.dados_conta()
saque = Banco_1.autenticar(Cliente_1.nome)
conta_corrente_1.sacar(saque, 3000)
conta_corrente_1.deposito(1000)
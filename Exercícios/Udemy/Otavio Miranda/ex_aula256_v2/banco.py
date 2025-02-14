import contas
import pessoas

class Banco:

    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None = None,
                 contas: list[contas.Conta] | None = None,
                 ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def autenticar_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('Agencia Ok!')
            return True
        print('Agencia errada!')
        return False
    
    def autenticar_clientes(self, cliente):
        if cliente in self.clientes:
            print('Cliente Ok!')
            return True
        print('Cliente errado!')
        return False
    
    def autenticar_conta(self, conta):
        if conta in self.contas:
            print('Conta Ok!')
            return True
        print('Conta errada!')
        return False
    
    def autenticar_conta_cliente(self, conta, cliente):
        if conta is cliente.conta:
            print('Conta/Clientet Ok!')
            return True
        print('Conta/Cliente errada!')
        return False
    
    def autenticar(self, cliente, conta):
        return self.autenticar_agencia(conta) and \
        self.autenticar_clientes(cliente) and \
        self.autenticar_conta(conta) and \
        self.autenticar_conta_cliente(conta, cliente)
    

if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)
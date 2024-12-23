class Carro():
    def __init__(self, nome, motor, fab):
        self.carro = nome
        self.motor = Motor(motor)
        self.fab = Fabricante(fab)


    def nome_carro(self):
        return f"O modelo do carro é {self.carro}"
    
    def nome_fabricante(self):
        return f"O fabricante é {self.fab}"
    
    def modelo_motor(self):
        return f"O modelo do motor é {self.motor}"


class Motor():
    def __init__(self, motor):
        self.motor = motor
    
    def __repr__(self):
        return f"{str(self.motor)}"
    
    
class Fabricante:
    def __init__(self, nome):
        self.fabricante = nome

    def __repr__(self):
        return f"{str(self.fabricante)}"

motor1 = Motor("V8")
fabricante1 = Fabricante("Chevrolet")
carro1 = Carro("Onix", motor1, fabricante1)
print(carro1.nome_carro())
print(carro1.modelo_motor())
print(carro1.nome_fabricante())

carro2 = Carro("Prisma", motor1, fabricante1)
print(carro2.nome_carro())
print(carro2.modelo_motor())
print(carro2.nome_fabricante())

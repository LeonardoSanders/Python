from modulo.veiculo import Veiculo
from modulo.carro import Carro
from modulo.moto import Moto


Prisma = Carro('Chevrolet', 'Prisma', 4)
Celta = Carro('Chevrolet', 'Celta', 2)
Cg = Moto('Honda', 'CG - 150', 'Casual')




def main():
    print(Prisma)
    print(Celta)
    print(Cg)

if __name__ == '__main__':
    main()
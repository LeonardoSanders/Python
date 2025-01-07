from carros import Carro

c1 = Carro('Onix', 'Preto', 2025)
# c2 = Carro('Corsa', 'Vermelho', 2015)
# c3 = Carro('Celta', 'Branco', 2005)

c1.receber_avaliacao('Tecnologia Automotiva', 9.5)
c1.receber_avaliacao('AutoSport', 10)

def main():
    Carro.listar_carros()

if __name__ == '__main__':
    main()
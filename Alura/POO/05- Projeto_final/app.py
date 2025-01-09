from restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato
from cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Manga', 10, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2, 'O melhor pao da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_item_no_cardapio(bebida_suco)
restaurante_praca.adicionar_item_no_cardapio(prato_paozinho)
pudim = Sobremesa('Pudim', 25, 'Doce', 'Fatia', 'Deliciosa fatia de pudim com calda')
restaurante_praca.adicionar_item_no_cardapio(pudim)

def main():
    restaurante_praca.listar_cardapio

if __name__ == '__main__':
    main()
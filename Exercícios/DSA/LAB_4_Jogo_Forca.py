from random import choice
lista_palavras = ['banana', 'uva', 'laranja', 'manga', 'abacaxi']

palavra_certa = choice(lista_palavras)


def display_hangman(error):
    display = [ 
        """
        ---------
        |       |
        |       
        |
        |
        |
        _
        """,
        """
        ---------
        |       |
        |       O
        |
        |
        |
        _
        """,
        """
        ---------
        |       |
        |       O
        |       |
        |       |
        |      / \\
        _
        """,
        """
        ---------
        |       |
        |       O
        |      \|/
        |       |
        |      / \\
        _
        """,
    ]
    return display[error]

class Hangman:

    def __init__(self, palavra):
        self.palavra = palavra
        self.palavra_usuario = ['_' for letra in self.palavra]
        self.letras_erradas = []
    
    def advinha_letra(self, letra):
        for i, letras in enumerate(self.palavra):
            if letra == letras:
                self.palavra_usuario[i] = letra

    def letra_errada(self, letra, erros):
        if letra not in self.palavra:
            self.letras_erradas.append(letra)
            erros += 1
            return erros

    def jogo_terminou(self, erros):
        if erros == 3:
            print(display_hangman(erros))
            print('\nVocê perdeu, tente novamente!')
            return True
    
    def jogador_venceu(self):
        if '_' not in self.palavra_usuario:
            print('\n', ' '.join(self.palavra_usuario))
            print('\nParabéns, você acertou! A palavra era: ', ''.join(self.palavra_usuario).upper())
            return True
        
    def imprimir_status(self, erros):
        print(display_hangman(erros))
        print('\n', ' '.join(self.palavra_usuario))
        print(f'\nChances restante: {3 - erros}')
        print('Letras erradas: ', ' '.join(self.letras_erradas))

    def verifact_letter(a, letra):
        while letra.isalpha() is False:
            print('Você não digitou uma letra!')
            letra = input('\nDigite uma letra: ')
        return letra
    
    def letra_repetida(self, letra):
        while letra in self.letras_erradas or letra in self.palavra_usuario:
            letra = input('\nVocê já digitou essa letra. Digite uma letra: ')
        return letra

    


def main():
    
    erros = 0 

    game = Hangman(palavra_certa)

    while True:
        game.imprimir_status(erros)

        tentativa = input('\nDigite uma letra: ')
        letra = game.verifact_letter(tentativa)
        letra = game.letra_repetida(letra)

        game.advinha_letra(letra)
        game.letra_errada(letra, erros)

        if game.jogador_venceu() or game.jogo_terminou(erros):
            break

if __name__ == '__main__':
    main()
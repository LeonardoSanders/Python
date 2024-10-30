from random import choice
lista_palavras = ['banana', 'uva', 'laranja', 'manga', 'abacaxi']

palavra_certa = choice(lista_palavras)
palavra_usuario = ['_' for letra in palavra_certa]
letras_erradas = []

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


def game():
    print('Bem bindo ao jogo da forca!')
    print('Advinhe a palavra abaixo:')
    erros = 0

    while True:
        print(display_hangman(erros))
        print('\n', ' '.join(palavra_usuario))
        print(f'\nChances restante: {3 - erros}')
        print('Letras erradas: ', ' '.join(letras_erradas))

        letra = input('\nDigite uma letra: ')

        while letra in letras_erradas or letra in palavra_usuario:
            letra = input('\nVocê já digitou essa letra. Digite uma letra: ')

        if letra not in palavra_certa:
            letras_erradas.append(letra)
            erros += 1

        for i, letras in enumerate(palavra_certa):
            if letra == letras:
                palavra_usuario[i] = letra

        if '_' not in palavra_usuario:
            print('\n', ' '.join(palavra_usuario))
            print('\nParabéns, você acertou! A palavra era: ', ''.join(palavra_usuario).upper())
            break

        if erros == 3:
            print(display_hangman(erros))
            print('\nVocê perdeu, tente novamente!')
            break

game()
from random import choice

lista_palavras = ['banana', 'uva', 'laranja', 'manga', 'abacaxi']

with open('Exercícios/DSA/jogo_forca.txt', 'w+') as arquivo:
    for palavra in lista_palavras:
        arquivo.write(str(palavra) + '\n')

with open('Exercícios/DSA/jogo_forca.txt', 'r') as arquivo:
    linha = arquivo.readlines()
    random_linha = choice(linha).strip()

palavra_certa = random_linha
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

def verifact_letter(letra):
    while letra.isalpha() is False:
        print('Você não digitou uma letra!')
        letra = input('\nDigite uma letra: ')
    return letra

def game():
    print('Bem bindo ao jogo da forca!')
    print('Advinhe a palavra abaixo:')
    erros = 0
    
    while True:
        print(display_hangman(erros))
        print('\n', ' '.join(palavra_usuario))
        print(f'\nChances restante: {3 - erros}')
        print('Letras erradas: ', ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ')
        letra = verifact_letter(tentativa)

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
def palavra_reversa(palavra):
    def interna():
        for letras in palavra:
            ...
        return palavra[::-1]
    return interna


def verificar_str():
    ...


palavra = palavra_reversa('Leonardo')
print(palavra())

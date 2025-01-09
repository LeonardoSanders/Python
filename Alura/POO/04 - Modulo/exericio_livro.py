class Livro:
    lista_livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_livros.append(self)
    
    def __str__(self):
        return f'Livro: {self._titulo}, Autor: {self._autor} e ano de publicação: {self._ano_publicacao}'

    def emprestar(self):
        self._disponivel = False
    
    def disponibilidade(self):
        print(f'Livro disponível' if self._disponivel else 'Livro indisponível')

    @classmethod
    def verificar_disponibilidade(cls, ano):
        print('Livros Disponíveis:')
        for livro in cls.lista_livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                print(f'{livro._titulo}, {livro._autor} - {livro._ano_publicacao}')


livro_1 = Livro('Harry Potter e a Pedra Filosofal', 'J.K Rolling', 1997)
livro_2 = Livro('Harry Potter e a Câmara Secreta', 'J.K Rolling', 1998)

# print(livro_1)
# # print(livro_2)

# livro_1.disponibilidade()
# livro_1.emprestar()
# livro_1.disponibilidade()
class Musica:

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    
    def __str__(self):
        return f'Música: {self.nome} | Artista: {self.artista} | Duração: {self.duracao} min'


music_1 = Musica('Faroeste Caboclo', 'Renato Russo', 9.36)
print(music_1)
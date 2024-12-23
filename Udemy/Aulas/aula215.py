# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, objeto):
        self._ferramenta = objeto

    def nome_escritor(self):
        return f"{self.nome}"


class Ferramenta:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f"Está usando a {self.nome} para escrever"
    
escritor = Escritor("Carlos Drummond")
caneta = Ferramenta("Caneta")
escritor.ferramenta = caneta

print(escritor.nome_escritor())
print(escritor.ferramenta.escrever())
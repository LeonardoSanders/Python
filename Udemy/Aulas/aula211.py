class Connection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

#É possível criar uma variavel no classmethod para receber os atributos da propria classe e dessa forma, utilizar estes atributos para receberem uma nova definição
#que será passada para o objeto no momento em que for chamada a classe + classmethod.

c1 = Connection()
c1.set_user('Worlorn')
c1.set_password(9513)

print(c1.user, c1.password)

c2 = Connection.create_with_auth('Leo', 123)
print(c2.user, c2.password)
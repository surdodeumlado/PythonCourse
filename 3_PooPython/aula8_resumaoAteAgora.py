# method vs @classmethod vs @staticmethod
# method <------------ self, metodo de instancia
# @classmethod <------ cls, metodo de classe
# @staticmethod <----- metodos estáticos (sem self, sem cls, mesma coisa q uma função avulsa)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):  # Um método normal recebe um self
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod  # Um método de classe recebe a própria classe
    def create_with_auth(cls, user, password):
        Connection = cls()
        Connection.user = user
        Connection.password = password
        return Connection

    @staticmethod  # sem acesso ao self, sem acesso ao cls
    def log(msg):
        return 'LOG', msg


c1 = Connection.create_with_auth('Daniel', '12345abcd')
c1.set_user('Daniel')
print(c1.user)
print(Connection.log('Esta é a mensagem de login.'))

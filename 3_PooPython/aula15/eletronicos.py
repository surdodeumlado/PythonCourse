from log import LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogFileMixin):  # HERANÇA MULTIPLA
    # P.S.: SEMPRE PREFIRA COMPOSIÇÃO AO INVÉS DE HERANÇA

    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado.'
            self.log_sucess(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado.'
            self.log_sucess(msg)

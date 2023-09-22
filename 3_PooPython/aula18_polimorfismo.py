# Polimorfismo em Python Orientado a Objetos

# Polimorfismo é o princípio que permite que classes deridavas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.

# Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)

# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod


class Notificacao:
    def __init__(self, msg) -> None:  # deve retornar algo (a frente do ->)
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:  # deve retornar bool
        ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail enviando:', self.msg)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS enviando:', self.msg)
        return True


def notificar(notificacao: Notificacao):  # esses : str está dizendo para minha ide, para meu python que: este parâmetro que está sendo passado é do tipo str. O python não vai necessariamente fazer algo com isso, ele apenas vai facilitar pra gente na hora de escrever e vai deixar o nosso código mais facil de ler para programadores que estarão vendo isso daqui. Caso passarmos algum parametro de outro tipo dentro de notificacao, nada vai acontecer (ao menos que a gente tente usar um método de string em um bool/int por exemplo)

    # Como o método .enviar() retornaria um bool ( -> bool ), essa operação será de tipo boolean
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')

    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('Testando Email.')
notificar(notificacao_email)
notificar(NotificacaoEmail)

# Classes abstratas - Abstract Base Class (abc)

# ABCs são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos concretos (metodos que tem corpo). Também podem ter métodos concretos por elas mesmas.

# @abstractmethods são métodos que não têm corpo.

# As regras para classes abstratas com métodos

# abstratos é que elas NÃO PODEM ser instânciadas diretamente.

# Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).

# Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.

# É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod como decorator mais interno.

from abc import ABC, abstractmethod

# class Log(metaclass=ABCMeta) <----- esta forma de fazer nossa classe herdar a classe abstrata também está correta, mas a mais utilizada é a que tá escrita abaixo


class Log(ABC):

    @abstractmethod  # decorator que torna minha classe completamente abstrata
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogPrintMixin(Log):  # Pelo principio da herança, LogPrintMixin é um Log
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('Oi')

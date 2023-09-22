# Abstração
# Herança - é um
# Log
from pathlib import Path

# pega o caminho para esse nosso arquivo.
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):

        # este trecho inteiro se chama de 'assinatura do método"
        raise NotImplementedError('implemente o metodo log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):  # Pelo principio da herança, LogFileMixin é um Log
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'

        print('Salvando no log.')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')


class LogPrintMixin(Log):  # Pelo principio da herança, LogPrintMixin é um Log
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':  # assim podemos testar diretamente o log, sem instanciar ele automaticamente em outros arquivos

    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_sucess('Qualquer coisa')

    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_sucess('qualquer coisa')
# Isso se chama abstração. Estamos fazendo isso pra caso não queiramos que a pessoa use esta classe diretamente. Se a pessoa quiser tentar usar o LOG diretamente o programa dará erro. Só conseguimos usar métodos do LOG se estivermos usando ele como super classe e instanciarmos seus métodos e funções dentro de sub classes.

# mantendo estados dentro de clase

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):

        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return  # return sem nada só pra parar a execução

        print(f'{self.nome} está filmando...')
        self.filmando = True

        return self.filmando

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando.')
            return

        print('Parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} NÃO pode gravar enquanto filma.')
            return

        print(f'{self.nome} está fotografando.')


camera1 = Camera('Canon')
camera1.filmar()
camera1.filmar()
camera1.parar_filmar()
camera1.parar_filmar()
camera1.fotografar()
camera1.filmar()
camera1.fotografar()
camera1.parar_filmar()
camera1.fotografar()

camera2 = Camera('Sony')

print(camera1.filmando)
print(camera2.filmando)

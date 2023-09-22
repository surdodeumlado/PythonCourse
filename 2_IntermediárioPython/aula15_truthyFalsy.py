# Valores truthy e Falsy
# Podem ser com valores mutaveis e imutaveis
# Imutáveis () "" 0 0.0 None False range(0,10)

lista = []  # ------------> Falsy
dicionario = {}  # -------> Falsy
conjunto = set()  # ------> Falsy
tupla = ()  # ------------> Falsy
string = ''  # -----------> Falsy
inteiro = 0  # -----------> Falsy
flutuante = 0.0  # -------> Falsy
nada = None  # -----------> Falsy
boolean = False  # -------> Falsy
intervalo = range(0)  # --> Falsy

# Qualquer tipo mutável ou imutável que tenha QUALQUER COISA dentro já é considerada truthy

lista = [0]  # -------------------> True
dicionario = {'numero': 0}  # ----> True
conjunto = set(0)  # -------------> True
tupla = (0, 0)  # ----------------> True
string = ' '  # ------------------> True
inteiro = 1  # -------------------> True
flutuante = 0.1  # ---------------> True
boolean = True  # ----------------> True
intervalo = range(0, 1)  # -------> True


def falsy(valor):
    return 'Falsy' if not valor else 'Truthy'

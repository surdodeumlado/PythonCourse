from os import system


def adicionar_tarefa_na_Lista(tarefa, lista=None):
    if lista == None:
        lista = []

    lista.append(tarefa)
    return lista


def remover_tarefa_da_lista(lista, lista_removidos):
    if lista == []:
        raise Exception("Lista está vazia.")

    lista_removidos.append(lista[len(lista) - 1])
    lista.pop()
    return lista


def retornar_lista(lista):
    if lista == None or lista == []:
        raise Exception("Lista está vazia.")
    print('Tarefas a fazer: ')
    print()

    for i in lista:
        print('-', i)
    print()


def reaver_valor_removido(lista, lista_removidos):
    if lista_removidos == []:
        raise Exception("Nenhum valor removido da lista.")

    lista.append(lista_removidos[len(lista_removidos) - 1])
    lista_removidos.pop()

    return lista


def letreiro():
    str = '==Lista de afazeres==\n=Selecione sua opção=\n[1] Listar ----------\n[2] Adicionar -------\n[3] Remover ---------\n[4] Reaver ----------\n[5] Sair ------------\n'

    return str


def valor_invalido():
    system('cls')
    print('===Valor inválido.===')
    print()


lista = []
lista_removidos = []

while True:
    print(letreiro())
    try:
        resposta = int(input(''))
    except ValueError:
        valor_invalido()
        continue

    match resposta:

        case 1:
            try:
                system('cls')
                retornar_lista(lista)
            except Exception:
                print('==Lista ainda vazia==')
                print()
                continue
        case 2:
            system('cls')

            tarefa = str(input('Tarefa para adicionar: '))
            adicionar_tarefa_na_Lista(tarefa, lista)
        case 3:

            try:
                system('cls')
                remover_tarefa_da_lista(lista, lista_removidos)
                print('Ultima tarefa removida')
                print()
                continue

            except Exception:
                system('cls')
                print('==Lista ainda vazia==')
                print()
                continue

        case 4:

            try:
                system('cls')
                reaver_valor_removido(lista, lista_removidos)
                print('Ultima tarefa removida\nAdicionada novamente.')
                print()
                continue

            except Exception:
                system('cls')
                print('Nenhuma tarefa foi removido ainda')
                print()
                continue

        case 5:
            system('cls')
            print('PROGRAMA FINALIZADO.')
            break

        case _:
            valor_invalido()
            continue

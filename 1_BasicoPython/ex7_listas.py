import os

print('Selecione uma opção para listar:\n')
dentro_do_While = True
lista_de_compras = []

while dentro_do_While:

    opcao_de_escolha = input(
        '[1] Inserir item na Lista\n[2] Apagar item da lista\n[3] Mostrar Lista\n[4] Sair\n\n'
    )

    if opcao_de_escolha not in '1234':

        os.system('cls')
        print('Opção inválida.\nSelecione uma opção:')
        continue

    match opcao_de_escolha:

        case '1':

            os.system('cls')
            item_para_adcionar = input('Insira o nome do item: ')
            lista_de_compras.append(item_para_adcionar)
            print('Item adicionado!\n\nSelecione uma opção para listar:')

        case '2':

            if len(lista_de_compras) == 0:
                os.system('cls')
                print(
                    'Lista vazia. Não é possível completar a operação.\n\nSelecione uma opção:')
                continue

            try:
                os.system('cls')
                item_para_apagar = int(input(
                    'Insita o valor do índice para apagar: '))
                del lista_de_compras[item_para_apagar]

                os.system('cls')
                print('Item apagado!')
                print('Selecione uma opção:')

            except ValueError:
                os.system('cls')
                print(
                    'Valor inválido.\nPor favor, digite apenas números inteiros.\n\nSelecione uma opção:')
            except IndexError:
                os.system('cls')
                print(
                    'Valor inválido.\nPor favor, digite apenas valores de índices existentes.\n\nSelecione uma opção: ')
            except Exception:
                os.system('cls')
                print('Valor inválido.\nErro Desconhecido.\n\nSelecione uma opção:')

        case '3':

            if len(lista_de_compras) == 0:
                os.system('cls')
                print('Lista vazia.\n\nSelecione uma opção:')

            os.system('cls')
            for valor_indice, item in enumerate(lista_de_compras):
                print(f'índice: {valor_indice}, Item: {item}')
            print('\nSelecione um item:')

        case '4':
            os.system('cls')
            print('Finalizado !')
            dentro_do_While = False

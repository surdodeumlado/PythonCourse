respostas_acertadas = 0

perguntas = [
    {
        'Pergunta:': 'Quanto é 2+2 ?',
        'Opções:': [1, 2, 3, 4],
        'Resposta:': 4
    },

    {
        'Pergunta:': 'Quanto é 5*5 ?',
        'Opções:': [25, 55, 10, 51],
        'Resposta:': 25
    },

    {
        'Pergunta:': 'Quanto é 10/2 ?',
        'Opções:': [4, 5, 3, 2],
        'Resposta:': 5
    }
]

for chave in perguntas:
    for indices in chave:

        if chave[indices] == chave['Pergunta:']:
            print(indices, chave[indices])

        elif chave[indices] == chave['Opções:']:
            print('Opções: ')
            parametro = 0
            opcoes = ['A)', 'B)', 'C)', 'D)']
            for valores in chave['Opções:']:
                print(f'{opcoes[parametro]} {chave[indices][parametro]}')
                parametro += 1

        else:
            resposta = str(input('Resposta: '))
            if (resposta == str(chave[indices])):
                print('Certa resposta 👌')
                respostas_acertadas += 1
                continue

            print('Resposta errada ☠️', end=' ')
            
    print('\n')

print(f'Fim do jogo!\nRespostas acertadas: {respostas_acertadas}')

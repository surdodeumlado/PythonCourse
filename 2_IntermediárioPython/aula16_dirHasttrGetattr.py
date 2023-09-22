# hasattr ---> checa se um determinado atributo tem um determinado nome lá dentro

string = 'Daniel'
metodo = 'upper1'
if hasattr(string, metodo):
    print('Existe upper!')
    print(getattr(string, metodo)())
else:
    print(f'Sem método o método {metodo}.')

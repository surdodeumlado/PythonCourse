# Este é o arquivo de inicialização do package
# é executado assim que o package é importado
# em que ter esse EXATO nome __init__.py

from aula23_package.modulo import *
from aula23_package.modulo_b import *
print('Você importou o package', __name__)

# Ambientes virtuais em Python (venv)

# Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.

# É importante termos um ambiente virtual para controle de versão. Por exemplo, se em um projeto usamos uma versão mais desatualizada do Django, e em outro uma versão mais Atualizada, podemos ter 2 djangos instalados, 1 em cada ambiente virtual. Isso não seria posssível se instalassemos o django globalmente, pois poderiamos ter uma versão apenas.

# venv é o módulo que vamos usar para criar ambientes virtuais.
# Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são: venv env .venv .env

# python -v -----------------> vê a versão do python
# python -m venv venv -------> o primeiro venv cria o ambiente virtual, o 2° venv é o nome da pasta (venv)

# gcm python.exe ------------> Vê diretorio do python
# gcm python -Syntax --------> Também mostra o diretório, usar caso não esteja aparecendo inteiro

# quando o ambiente não está ativo, ele usa este diretório
# :\Users\danie\AppData\Local\Microsoft\WindowsApps\python.exe
# (este é o python global, do SO)

# quando o ambiente está ativo, ele usa este outro diretório
# C:\Users\danie\OneDrive\Área de Trabalho\PythonCourse\venv\Scripts\python.exe
# (este é o python local, do nosso proprio virtual enviroment(venv))

# .\venv\Scripts\activate ----> ativa o venv
# deactivate -----------------> desativa o venv

# Caso venv esteja ativado, o pip usado vai ser desse diretório:
# pip 23.2.1 from C:\Users\danie\OneDrive\Área de Trabalho\PythonCourse\venv\Lib\site-packages\pip
# (diretório local)

# Caso venv esteja desativado, o pip usado vai ser deste outro diretório:
# pip 23.2.1 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib\site-packages\pip (python 3.11)
# (diretório global)

# Quando usamos o pip do sistema, instalamos bibliotecas GLOBALMENTE, caso estejamos usando o pip do venv, estaremos instalando bibliotecas LOCALMENTE

# Pra conseguir usar o ambiente virtual, temos que mudar a versão do python no canto inferior direito do vscode e definir o interpretador python como a nossa pasta venv.

# =============================================================================================================
# COMO INSTALAR BIBLIOTECAS COM O PIP =========================================================================
# =============================================================================================================

# Oquê é o pip ?
# Pip é um instalador de pacotes do python package index (bibliotecas que não vem com o python). O pip já vem dentro do nosso ambiente virtual

# Pra instalar com o pip algum framework ou alguma biblioteca, temos que ir no site e pegar o comando de instalação. Exemplo:
# pip install Django
# pip install pymysql

# Pra saber todas as versões de algum framework/biblioteca, usamos esse comando:
# pip index versions (nome da biblioteca/framework)
# pip index versions autopep8
# pip index versions Django

# Se quisermos instalar uma versão específica, digitamos assim:
# pip install (framework/biblioteca) == (versão)
# pip install autopep8 == 2.0.2 (atualmente estamos na versão 2.0.4)

# Caso dê erro na hora da instalação, pode ser que usar o comando assim ajude:
# python.exe -m pip install Django
# python.exe -m pip install pymysql

# Pra desinstalar alguma coisa com o nosso pip, podemos digitar assim:
# pip uninstall pymysql
# pip uninstall Django

# Pra saber o quê temos instalado no nosso ambiente virtual:
# pip freeze -----------> Além de mostrar oq temos instalado, podemos criar um arquivo >requirements.txt<

# =============================================================================================================
# REQUIREMENTS.TXT ============================================================================================
# =============================================================================================================

# É um tipo de arquivo usado para recarregar nosso ambiente virtual
# Um requirements.txt é criado quando usamos este comando:
# pip freeze > requirements.txt
# P.s.: o nome do requirements podemos escolher, mas por PADRÃO o nome deve se manter requirements

# Dentro do arquivo requirements possui tudo que importamos para o nosso ambiente virtual (basicamente tudo que aparece no pip freeze)

# Estes requirements geralmente, em um repositório git, é o que compartilhamos.
# Nós não mandamos o nosso ambiente virtual para o git, nós mandamos os requirements, e caso alguem queira baixar nosso programa e ver o quê é preciso ter na venv própria pra rodar nosso código, é só olhar nos requirements e botar ele pra rodar

# Pra instalar um requirements, é só digitar o seguinte comando:
# pip install -r .\requirements.txt

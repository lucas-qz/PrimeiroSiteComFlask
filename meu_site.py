# 1) instalar e importar o flask ---------------------------------------------------------------------------------------
from flask import Flask, render_template
"""
Flask = biblioteca do flask pra criar paginas, libnks, etc
render_template = biblioteca do flask pra vincular as paginas criadas com seu respectivo html que está na pasta templates
"""

# 2) padrão do Flask para indicar que está criando um site -------------------------------------------------------------
app = Flask(__name__)

# 3) criar páginas do site ---------------------------------------------------------------------------------------------
"""
--- toda pagina terá um 'route' e uma 'função':
route  -> é a rota daquela pagina (/ = home)(/nome_da_pagina = outras páginas)
função -> nessa função vai ficar oque vai aparecer na página
"""
# pagina 1 --------------------------------------------------
@app.route("/")  # esse é o route
def homepage():  # essa é a função
    return render_template("home.html") # render_template
# pagina 2 --------------------------------------------------
@app.route("/contatos")  # esse é o route
def contatos():          # essa é a função
    return render_template("contatos.html")
# pagina 3 --------------------------------------------------
@app.route("/usuarios/<nome_usuario>") # <nome_usuario> = é uma variável, indicando q essa página terá um nome dinâmico
def usuarios(nome_usuario): # recebo a variável <nome_usuario> como parâmetro dessa função
    return render_template("usuarios.html", usuario=nome_usuario) # dessa forma eu passo para o usuarios.html
                                                                  # uma variavel chamada 'usuario' que recebe o parâmetro 'nome_usuario'

# 4) colocar o site no ar ----------------------------------------------------------------------------------------------
"""
app.run() # dessa forma, pra atualizar o site tenho sempre que dar Stop e Play aqui no PyCharm
app.run(debug=True) # dessa forma, não preciso é só dar Play
if __name__ == "__main__": #colocar dentro dessa função é necessário pra funcionar na hospedagem
"""

if __name__ == "__main__":
    app.run(debug=True)

"""
Pasta templates = padrão do Python para se colocar os arquivos html
"""

## SOBRE O ARQUIVO Procfile -----------
"""
web: gunicorn meu_site:app
# serve pra conseguir mandar seu site pra uma hospedagem
# é padrão do flask, a unica coisa que deve mudar é o nome da pagina python, que nesse caso é 'meu_site'
"""

## SOBRE O ARQUIVO requeriments.txt -----------
"""
# cria ele pelo terminal digitando:
pip freeze > requirements.txt

# ele vai listar tudo que seu site está usando pra funcionar (ex: flask, etc)
# dessa forma o servidor de hospedagem vai saber oque ele precisa instalar pro site rodar lá também

"""
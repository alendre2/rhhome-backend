from flask import Flask

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define uma "rota" ou "endpoint". É a URL que aciona nossa função.
# O decorator '@' associa a URL '/' com a função 'home'.
@app.route('/')
def home():
    # O que essa função retorna é o que será exibido no navegador.
    return "<h1>Backend da RH Home Imobiliária está no ar!</h1>"

# Esta verificação garante que o servidor só vai rodar quando o script for executado diretamente.
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento. debug=True faz com que ele reinicie automaticamente
    # a cada alteração no código, o que é ótimo para desenvolver.
    app.run(debug=True)
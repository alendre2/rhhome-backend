from flask import Flask
# Importamos o nosso blueprint do arquivo de controller
from controllers.lead_controller import lead_blueprint

# Cria a instância da aplicação
app = Flask(__name__)

# Registra o blueprint de leads na nossa aplicação principal
app.register_blueprint(lead_blueprint)

# A rota home pode continuar aqui ou ser movida para um "home_controller" no futuro
@app.route('/')
def home():
    return "<h1>Backend da RH Home Imobiliária está no ar! (Versão Refatorada)</h1>"

if __name__ == '__main__':
    app.run(debug=True)
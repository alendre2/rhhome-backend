from flask import Flask
from flask_migrate import Migrate # Importamos o Migrate
from database import db # Importaremos nosso objeto db
from controllers.lead_controller import lead_blueprint
from controllers.broker_controller import broker_blueprint

# Cria a instância da aplicação
app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
# Define a URI do banco de dados. Para SQLite, é o caminho do arquivo.
# 'sqlite:///project.db' significa que o arquivo se chamará 'project.db' e
# ficará na pasta principal do projeto.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desativa uma feature que não usaremos

# Inicializa o SQLAlchemy com a nossa aplicação
db.init_app(app)
# Inicializa o Migrate com nosso app e nosso db
migrate = Migrate(app, db)
# ------------------------------------

# Registra os blueprints
app.register_blueprint(lead_blueprint)
app.register_blueprint(broker_blueprint)

@app.route('/')
def home():
    return "<h1>Backend da RH Home Imobiliária está no ar!</h1>"

# Não precisamos mais do if __name__ == '__main__' porque usaremos o 'flask run'
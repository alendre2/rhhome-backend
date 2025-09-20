from flask import Flask
from flask_migrate import Migrate

# Importo as instâncias que criamos em arquivos separados (pra organizar melhor)
from database import db
from extensions import bcrypt, jwt

# Importo os modelos pra que o Flask-Migrate consiga ver e criar as tabelas no banco
from models.user_model import User
from models.lead_model import Lead
from models.broker_model import Broker

# Importo os controllers/blueprints pra organizar as rotas
from controllers.lead_controller import lead_blueprint
from controllers.broker_controller import broker_blueprint
from controllers.user_controller import user_blueprint

# Crio a instância da aplicação Flask
app = Flask(__name__)

# --- CONFIGURAÇÕES ---
# Chave secreta do JWT (em produção, isso deve ficar em variável de ambiente e ser bem segura)
app.config["JWT_SECRET_KEY"] = "sua-chave-secreta-super-dificil" 
# Configuro o banco de dados (SQLite só pra exemplo)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- INICIALIZAÇÃO DAS EXTENSÕES ---
# Conecto as extensões com a aplicação
db.init_app(app)
migrate = Migrate(app, db)
bcrypt.init_app(app)  # pra gerar e verificar hashes de senha
jwt.init_app(app)     # pra cuidar da autenticação via JWT
# ------------------------------------

# Registro os blueprints, separando as rotas por módulo
app.register_blueprint(lead_blueprint)
app.register_blueprint(broker_blueprint)
app.register_blueprint(user_blueprint)

# Rota simples de teste
@app.route('/')
def home():
    return "<h1>Backend da RH Home Imobiliária está no ar!</h1>"

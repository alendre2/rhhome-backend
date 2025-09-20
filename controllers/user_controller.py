from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
# Importo o bcrypt que criamos no arquivo de extensões
from extensions import bcrypt
import repositories.user_repository as user_repository


# Crio o blueprint do usuário pra organizar as rotas
user_blueprint = Blueprint('user_controller', __name__)

# ------------------ ROTA DE REGISTRO ------------------
@user_blueprint.route('/register', methods=['POST'])
def register():
    # Pego os dados enviados pelo cliente
    user_data = request.get_json()

    # Verifico se já existe um usuário com esse username
    if user_repository.find_user_by_username(user_data['username']):
        return jsonify({"message": "Username already exists"}), 400

    # Crio o usuário usando o repositório (senha já vai criptografada)
    new_user = user_repository.create_user(user_data)

    # Retorno os dados do novo usuário (sem a senha)
    return jsonify(new_user.to_dict()), 201


# ------------------ ROTA DE LOGIN ------------------
@user_blueprint.route('/login', methods=['POST'])
def login():
    # Pego os dados enviados pelo cliente
    user_data = request.get_json()
    username = user_data['username']
    password = user_data['password']

    # Busco o usuário no banco pelo username
    user = user_repository.find_user_by_username(username)

    # Verifico se o usuário existe e se a senha confere com o hash do banco
    if user and bcrypt.check_password_hash(user.password, password):
        # Se estiver tudo certo, gero um token JWT
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)

    # Se deu errado, retorno erro de autenticação
    return jsonify({"message": "Invalid username or password"}), 401

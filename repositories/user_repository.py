from database import db
from models.user_model import User
# Importo o bcrypt que está no arquivo de extensões
from extensions import bcrypt

def create_user(user_data):
    # Pego a senha pura que veio do cliente
    plain_text_password = user_data['password']
    # Crio o hash da senha com bcrypt (nunca salvo a senha real no banco)
    password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    # Crio o usuário com o username e a senha já criptografada
    new_user = User(
        username=user_data['username'],
        password=password_hash
    )
    # Salvo o usuário no banco
    db.session.add(new_user)
    db.session.commit()

    # Retorno o objeto criado
    return new_user

def find_user_by_username(username):
    # Procuro um usuário pelo username
    return User.query.filter_by(username=username).first()

from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # A senha não vai ser salva pura, aqui vai ficar o hash (por isso precisa de bastante espaço)
    password = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        # Importante: nunca devolver a senha quando for transformar o objeto em dicionário
        return {
            "id": self.id,
            "username": self.username
        }

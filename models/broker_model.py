from database import db

class Broker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    creci = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20))

    # Relacionamento
     # Esta linha não cria uma coluna no banco. É uma propriedade "mágica" do SQLAlchemy
    # que nos permite acessar a lista de leads associados a este corretor.
    # Ex: meu_corretor.leads
    leads = db.relationship('Lead', backref='broker', lazy=True)
    # ------------------------------------

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "creci": self.creci,
            "phone": self.phone
        }
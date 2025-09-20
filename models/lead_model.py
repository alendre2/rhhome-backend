from database import db

class Lead(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    region_of_interest = db.Column(db.String(100))
    status = db.Column(db.String(50), nullable=False, default='Novo')

    # Chave estrangeira
    # Esta coluna vai guardar o ID do corretor.
    # db.ForeignKey('broker.id') cria a conexão com a coluna 'id' da tabela 'broker'.
    broker_id = db.Column(db.Integer, db.ForeignKey('broker.id'), nullable=False)
    # ------------------------------------


    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "cpf": self.cpf,
            "phone": self.phone,
            "email": self.email,
            "region_of_interest": self.region_of_interest,
            "status": self.status
        }
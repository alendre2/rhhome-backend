from database import db

class Lead(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    region_of_interest = db.Column(db.String(100))
    status = db.Column(db.String(50), nullable=False, default='Novo')


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
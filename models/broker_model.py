from database import db

class Broker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    creci = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "creci": self.creci,
            "phone": self.phone
        }
class Broker:

    def __init__(self, id, name, creci, phone):

        self.id = id
        self.name = name
        self.creci = creci
        self.phone = phone

    def to_dict(self):
    
        return{
        "id": self.id,
        "name": self.name,
        "creci": self.creci,
        "phone": self.phone
        }
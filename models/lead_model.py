class Lead:

    def __init__(self, id, name, cpf, phone, email, region_of_interest, status="Novo"):
        
        self.id = id
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.email = email
        self.region_of_interest = region_of_interest
        self.status= status


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
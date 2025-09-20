from database import db
from models.lead_model import Lead

def get_all():
    # Busca todos os leads no banco (equivalente a um SELECT * FROM lead)
    return Lead.query.all()

def get_by_id(lead_id):
    # Busca um lead pelo ID (query.get é otimizado pra chave primária)
    return Lead.query.get(lead_id)


def create(lead_data):
    # Aqui eu monto um novo objeto Lead usando os dados já validados pelo schema
    new_lead_object = Lead(
        name=lead_data['name'],
        cpf=lead_data['cpf'],
        phone=lead_data['phone'],
        email=lead_data['email'],
        region_of_interest=lead_data['region_of_interest'],
        broker_id=lead_data['broker_id']
    )
    # Adiciono no banco e confirmo a transação
    db.session.add(new_lead_object)
    db.session.commit()
    
    # Retorno o objeto criado pra poder exibir no response
    return new_lead_object


def update(lead_id, updated_data):
    # Procura o lead pelo ID
    lead_to_update = get_by_id(lead_id)
    if not lead_to_update:
        return None
    
    # Atualiza apenas os campos que foram enviados
    lead_to_update.name = updated_data.get('name', lead_to_update.name)
    lead_to_update.cpf = updated_data.get('cpf', lead_to_update.cpf)
    lead_to_update.phone = updated_data.get('phone', lead_to_update.phone)
    lead_to_update.email = updated_data.get('email', lead_to_update.email)
    lead_to_update.region_of_interest = updated_data.get('region_of_interest', lead_to_update.region_of_interest)
    lead_to_update.status = updated_data.get('status', lead_to_update.status)
    
    # Só dar commit já basta, o SQLAlchemy já sabe que o objeto foi alterado
    db.session.commit()
    return lead_to_update

def delete(lead_to_delete):
    # Remove o lead e confirma no banco
    db.session.delete(lead_to_delete)
    db.session.commit()

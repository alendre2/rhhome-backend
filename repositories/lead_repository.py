from database import db
from models.lead_model import Lead

def get_all():
    """
    Retorna todos os leads do banco de dados.
    Lead.query.all() se traduz em 'SELECT * FROM lead' e retorna uma lista de objetos Lead.
    """
    return Lead.query.all()

def get_by_id(lead_id):
    """
    Retorna um único lead pelo seu ID.
    Lead.query.get(lead_id) é uma forma otimizada de buscar pela chave primária.
    """
    return Lead.query.get(lead_id)

def create(lead_data):
    """Cria um novo lead e o salva no banco de dados."""
    new_lead = Lead(
        name=lead_data['name'],
        cpf=lead_data['cpf'],
        phone=lead_data['phone'],
        email=lead_data['email'],
        region_of_interest=lead_data['region_of_interest']
    )
    # db.session.add() 'prepara' o objeto para ser salvo.
    db.session.add(new_lead)
    # db.session.commit() efetivamente salva todas as alterações preparadas no banco.
    db.session.commit()
    return new_lead

def update(lead_id, updated_data):
    """Encontra um lead e atualiza seus dados no banco."""
    lead_to_update = get_by_id(lead_id)
    if not lead_to_update:
        return None
    
    lead_to_update.name = updated_data.get('name', lead_to_update.name)
    lead_to_update.cpf = updated_data.get('cpf', lead_to_update.cpf)
    lead_to_update.phone = updated_data.get('phone', lead_to_update.phone)
    lead_to_update.email = updated_data.get('email', lead_to_update.email)
    lead_to_update.region_of_interest = updated_data.get('region_of_interest', lead_to_update.region_of_interest)
    lead_to_update.status = updated_data.get('status', lead_to_update.status)
    
    # Apenas damos o commit, pois o SQLAlchemy já sabe que o objeto foi modificado.
    db.session.commit()
    return lead_to_update

def delete(lead_to_delete):
    """Deleta um lead do banco de dados."""
    # db.session.delete() prepara a remoção.
    db.session.delete(lead_to_delete)
    # db.session.commit() efetiva a remoção.
    db.session.commit()
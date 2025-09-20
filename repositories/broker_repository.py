from database import db
from models.broker_model import Broker

def get_all():
    """Retorna todos os corretores do banco de dados."""
    return Broker.query.all()

def get_by_id(broker_id):
    """Retorna um único corretor pelo seu ID."""
    return Broker.query.get(broker_id)

def create(broker_data):
    """Cria um novo corretor e o salva no banco de dados."""
    new_broker = Broker(
        name=broker_data['name'],
        creci=broker_data['creci'],
        phone=broker_data['phone']
    )
    db.session.add(new_broker)
    db.session.commit()
    return new_broker

def update(broker_id, updated_data):
    """Encontra um corretor e atualiza seus dados no banco."""
    broker_to_update = get_by_id(broker_id)
    if not broker_to_update:
        return None
    
    broker_to_update.name = updated_data.get('name', broker_to_update.name)
    broker_to_update.creci = updated_data.get('creci', broker_to_update.creci)
    broker_to_update.phone = updated_data.get('phone', broker_to_update.phone)
    
    db.session.commit()
    return broker_to_update

def delete(broker_to_delete):
    """Deleta um corretor do banco de dados."""
    db.session.delete(broker_to_delete)
    db.session.commit()
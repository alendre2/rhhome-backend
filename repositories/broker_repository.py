from models.broker_model import Broker

_broker_db = [
    Broker(id=1, name="Alendre Maciel", creci= "12345-F/PE", phone="81992584670"),
    Broker(id=2, name="Cibelly Gomes", creci="54321-F/PE", phone="81985801670")
]
_next_id = 3

def get_all():

    return _broker_db

def get_by_id(broker_id):

    for broker in _broker_db:

        if broker.id == broker_id:
            return broker
    return None

def create(broker_data):

    global _next_id

    new_broker = Broker(
        id=_next_id,
        name=broker_data['name'],
        creci=broker_data['creci'],
        phone=broker_data['phone']
    )
    _broker_db.append(new_broker)
    _next_id += 1
    return new_broker

def update(broker_id, update_data):

    broker_to_update = get_by_id(broker_id)
    if not broker_to_update:
        return None
    
    broker_to_update.name = update_data.get('name', broker_to_update.name)
    broker_to_update.creci= update_data.get('creci', broker_to_update.creci)
    broker_to_update.phone= update_data.get('phone', broker_to_update.phone)

    return broker_to_update

def delete(broker_to_delete):

    _broker_db.remove(broker_to_delete)

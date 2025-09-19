# MOCK DATABASE
_leads_db = [
    {
        "id": 1,
        "name": "Maria Joaquina",
        "cpf": "111.222.333-44",
        "phone": "8199999-1111",
        "email": "maria@email.com",
        "region_of_interest": "Boa Viagem",
        "status": "Novo"
    },
    {
        "id": 2,
        "name": "José Almeida",
        "cpf": "222.333.444-55",
        "phone": "8198888-2222",
        "email": "jose.a@email.com",
        "region_of_interest": "Casa Forte",
        "status": "Em Contato"
    }
]
_next_id = 3

# Repository functions
def get_all():
    """Returns all leads from the database."""
    return _leads_db

def get_by_id(lead_id):
    """Returns a single lead by its ID, or None if not found."""
    for lead in _leads_db:
        if lead.get('id') == lead_id:
            return lead
    return None

def create(lead_data):
    """Creates a new lead and adds it to the database."""
    global _next_id
    new_lead = {
        "id": _next_id,
        "name": lead_data['name'],
        "cpf": lead_data['cpf'],
        "phone": lead_data['phone'],
        "email": lead_data['email'],
        "region_of_interest": lead_data['region_of_interest'],
        "status": "Novo"
    }
    _leads_db.append(new_lead)
    _next_id += 1
    return new_lead

def delete(lead_to_delete):
    """Deletes a lead from the database."""
    _leads_db.remove(lead_to_delete)

def update(lead_id, updated_data):
    """Finds a lead by its ID and updates it with new data."""
    #Aqui vamos encontrar primeiro o lead que vamos atualizar
    lead_to_update = get_by_id(lead_id)

    # Se o lead não for encontrado , retornaremos None
    if not lead_to_update:
        return None
    
    # Atualizamos os dados do lead encontrado com os novos dados
    # O método update() de dicionários é perfeito para isso.
    lead_to_update.update(updated_data)

    # Garantimos que o status e o id não sejam sobrescritos se não vierem nos dados
    # (O id nunca deve mudar)
    lead_to_update['id'] = lead_id

    return lead_to_update
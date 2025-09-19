# Primeiro, importamos a classe que acabamos de criar
from models.lead_model import Lead

# Nossa 'base de dados' agora é uma lista de OBJETOS Lead
_leads_db = [
    Lead(id=1, name="Maria Joaquina", cpf="111.222.333-44", phone="8199999-1111", email="maria@email.com", region_of_interest="Boa Viagem", status="Novo"),
    Lead(id=2, name="José Almeida", cpf="222.333.444-55", phone="8198888-2222", email="jose.a@email.com", region_of_interest="Casa Forte", status="Em Contato")
]
_next_id = 3

def get_all():
    """Retorna todos os leads como objetos Lead."""
    return _leads_db

def get_by_id(lead_id):
    """Retorna um único objeto Lead pelo seu ID."""
    for lead in _leads_db:
        # Agora acessamos os dados como atributos de um objeto (lead.id)
        if lead.id == lead_id:
            return lead
    return None

def create(lead_data):
    """Cria um novo objeto Lead e o adiciona à base de dados."""
    global _next_id
    # Criamos uma nova INSTÂNCIA da classe Lead, em vez de um dicionário
    new_lead = Lead(
        id=_next_id,
        name=lead_data['name'],
        cpf=lead_data['cpf'],
        phone=lead_data['phone'],
        email=lead_data['email'],
        region_of_interest=lead_data['region_of_interest']
        # O status "Novo" já é o padrão no construtor da classe
    )
    _leads_db.append(new_lead)
    _next_id += 1
    return new_lead

def update(lead_id, updated_data):
    """Encontra um objeto Lead e atualiza seus atributos."""
    lead_to_update = get_by_id(lead_id)
    if not lead_to_update:
        return None
    
    lead_to_update.name = updated_data.get('name', lead_to_update.name)
    lead_to_update.cpf = updated_data.get('cpf', lead_to_update.cpf)
    lead_to_update.phone = updated_data.get('phone', lead_to_update.phone)
    lead_to_update.email = updated_data.get('email', lead_to_update.email)
    lead_to_update.region_of_interest = updated_data.get('region_of_interest', lead_to_update.region_of_interest)
    lead_to_update.status = updated_data.get('status', lead_to_update.status)
    
    return lead_to_update

def delete(lead_to_delete):
    """Deleta um objeto Lead da base de dados."""
    _leads_db.remove(lead_to_delete)
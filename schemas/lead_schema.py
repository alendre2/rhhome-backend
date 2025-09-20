from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.lead_model import Lead

class LeadSchema(SQLAlchemyAutoSchema):
    """
    Este Schema serve a dois propósitos:
    1. Validar os dados que chegam nas requisições POST e PUT.
    2. Serializar os objetos Lead, convertendo-os para JSON de forma segura.
    """
    class Meta:
        # O SQLAlchemyAutoSchema vai inspecionar a classe Lead
        # e criar os campos de validação automaticamente.
        model = Lead
        # Inclui a chave estrangeira (broker_id) na validação/serialização.
        include_fk = True
        # Quando carregamos dados (load), ele nos devolve um objeto Lead, e não um dicionário.

# Instância para validar/serializar um único lead
lead_schema = LeadSchema()

# Instância para validar/serializar uma lista de leads
leads_schema = LeadSchema(many=True)
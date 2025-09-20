from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from database import db
import repositories.lead_repository as lead_repository
from schemas.lead_schema import lead_schema, leads_schema
from flask_jwt_extended import jwt_required


lead_blueprint = Blueprint('lead_controller', __name__)

@lead_blueprint.route('/leads', methods=['GET'])
def get_leads():
    # Busco todos os leads no repositório e transformo em JSON com o schema
    all_leads = lead_repository.get_all()
    return jsonify(leads_schema.dump(all_leads))

@lead_blueprint.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    # Procuro um lead pelo ID
    lead = lead_repository.get_by_id(lead_id)
    if lead:
        return jsonify(lead_schema.dump(lead))
    # Se não achar, retorno erro 404
    return jsonify({"error": "Lead not found"}), 404

@lead_blueprint.route('/leads', methods=['POST'])
@jwt_required()
def create_lead():
    lead_data = request.get_json()
    try:
        # Aqui o schema valida os dados e já devolve um dicionário pronto
        validated_data = lead_schema.load(lead_data, session=db.session)
    except ValidationError as err:
        # Se a validação falhar, retorno 400 com os erros
        return jsonify(err.messages), 400

    # Se deu certo, mando pro repositório criar o lead
    new_lead = lead_repository.create(validated_data)
    
    # Retorno o lead criado no formato JSON e status 201
    return jsonify(lead_schema.dump(new_lead)), 201

@lead_blueprint.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    updated_data = request.get_json()
    try:
        # Valido os dados antes de atualizar
        validated_data = lead_schema.load(updated_data, session=db.session)
    except ValidationError as err:
        return jsonify(err.messages), 400
        
    # Mando pro repositório atualizar
    updated_lead = lead_repository.update(lead_id, validated_data)
    if not updated_lead:
        return jsonify({"error": "Lead not found"}), 404
    return jsonify(lead_schema.dump(updated_lead)), 200

@lead_blueprint.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    # Procuro o lead pelo ID
    lead_to_delete = lead_repository.get_by_id(lead_id)
    if not lead_to_delete:
        return jsonify({"error": "Lead not found"}), 404
    
    # Se encontrei, mando o repositório deletar
    lead_repository.delete(lead_to_delete)
    return jsonify({"message": f"Lead with id {lead_id} has been deleted successfully."}), 200

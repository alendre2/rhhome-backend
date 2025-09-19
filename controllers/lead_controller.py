from flask import Blueprint, request, jsonify
# Importamos as funções que criamos no nosso repositório
import repositories.lead_repository as lead_repository

from repositories.lead_repository import get_all, get_by_id, create, delete, update


# Blueprint é como um "mini-app" que agrupa as rotas relacionadas a leads.
lead_blueprint = Blueprint('lead_controller', __name__)

@lead_blueprint.route('/leads', methods=['GET'])
def get_leads():
    all_leads = lead_repository.get_all()
    return jsonify(all_leads)

@lead_blueprint.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    lead = lead_repository.get_by_id(lead_id)
    if lead:
        return jsonify(lead)
    return jsonify({"error": "Lead not found"}), 404

@lead_blueprint.route('/leads', methods=['POST'])
def create_lead():
    # Renomeamos as funções para o padrão inglês
    lead_data = request.get_json()
    new_lead = lead_repository.create(lead_data)
    return jsonify(new_lead), 201

@lead_blueprint.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    lead_to_delete = lead_repository.get_by_id(lead_id)
    if not lead_to_delete:
        return jsonify({"error": "Lead not found"}), 404
    
    lead_repository.delete(lead_to_delete)
    return jsonify({"message": f"Lead with id {lead_id} has been deleted successfully."}), 200



@lead_blueprint.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    updated_data = request.get_json()

    # Chama a função de update do repositório
    updated_lead = lead_repository.update(lead_id, updated_data)

    # Se o lead não foi encontrado, o repositório retornou None
    if not updated_lead:
        return jsonify({"error": "Lead not found"}), 404
    
    # Se deu tudo certo, retorna o lead com os dados atualizados
    return jsonify(updated_lead), 200


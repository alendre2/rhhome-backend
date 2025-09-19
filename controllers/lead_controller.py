from flask import Blueprint, request, jsonify
import repositories.lead_repository as lead_repository

lead_blueprint = Blueprint('lead_controller', __name__)

@lead_blueprint.route('/leads', methods=['GET'])
def get_leads():
    all_leads = lead_repository.get_all()
    # Convertemos cada objeto Lead em um dicionário antes de 'jsonificar'
    return jsonify([lead.to_dict() for lead in all_leads])

@lead_blueprint.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    lead = lead_repository.get_by_id(lead_id)
    if lead:
        # Convertemos o objeto Lead em um dicionário
        return jsonify(lead.to_dict())
    return jsonify({"error": "Lead not found"}), 404

@lead_blueprint.route('/leads', methods=['POST'])
def create_lead():
    lead_data = request.get_json()
    new_lead = lead_repository.create(lead_data)
    return jsonify(new_lead.to_dict()), 201

@lead_blueprint.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    updated_data = request.get_json()
    updated_lead = lead_repository.update(lead_id, updated_data)
    if not updated_lead:
        return jsonify({"error": "Lead not found"}), 404
    return jsonify(updated_lead.to_dict()), 200

@lead_blueprint.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    lead_to_delete = lead_repository.get_by_id(lead_id)
    if not lead_to_delete:
        return jsonify({"error": "Lead not found"}), 404
    
    lead_repository.delete(lead_to_delete)
    return jsonify({"message": f"Lead with id {lead_id} has been deleted successfully."}), 200
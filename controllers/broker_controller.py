from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import repositories.broker_repository as broker_repository


broker_blueprint = Blueprint('broker_controller', __name__)

@broker_blueprint.route('/brokers', methods=['GET'])
def get_brokers():
    all_brokers = broker_repository.get_all()
    
    return jsonify([broker.to_dict() for broker in all_brokers])

@broker_blueprint.route('/brokers/<int:broker_id>', methods=['GET'])
def get_broker(broker_id):
    broker = broker_repository.get_by_id(broker_id)
    if broker:

        return jsonify(broker.to_dict())
    return jsonify({"error": "Broker not found"}), 404

@broker_blueprint.route('/brokers', methods=['POST'])
@jwt_required()
def create_broker():
    broker_data = request.get_json()
    new_broker = broker_repository.create(broker_data)
    return jsonify(new_broker.to_dict()), 201

@broker_blueprint.route('/brokers/<int:broker_id>', methods=['PUT'])
@jwt_required()
def update_broker(broker_id):
    update_data = request.get_json()
    update_broker = broker_repository.update(broker_id, update_data)
    if not update_broker:
        return jsonify({"error": "Broker not found"}), 404
    return jsonify(update_broker.to_dict()), 200

@broker_blueprint.route('/brokers/<int:broker_id>', methods=['DELETE'])
@jwt_required()
def delete_broker(broker_id):
    broker_to_delete = broker_repository.get_by_id(broker_id)
    if not broker_to_delete:
        return jsonify({"error": " Broker not found"}), 404
    
    broker_repository.delete(broker_to_delete)
    return jsonify({"messge": f"Broker with id {broker_id} has been deleted successfully. "}), 200

    




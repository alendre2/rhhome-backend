from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Nosso "Banco de Dados" Temporário ---
leads_db = [
    {
        "id": 1,
        "nome": "Maria Joaquina",
        "cpf": "111.222.333-44",
        "telefone": "8199999-1111",
        "email": "maria@email.com",
        "regiao_interesse": "Boa Viagem",
        "status": "Novo"
    },
    {
        "id": 2,
        "nome": "José Almeida",
        "cpf": "222.333.444-55",
        "telefone": "8198888-2222",
        "email": "jose.a@email.com",
        "regiao_interesse": "Casa Forte",
        "status": "Em Contato"
    },
    {
        "id": 3,
        "nome": "Ana Clara",
        "cpf": "333.444.555-66",
        "telefone": "8197777-3333",
        "email": "ana.clara@email.com",
        "regiao_interesse": "Boa Viagem",
        "status": "Novo"
    }
]
# -----------------------------------------

@app.route('/')
def home():
    return "<h1>Backend da RH Home Imobiliária está no ar!</h1>"

# GET /leads - Retorna a lista de todos os leads
@app.route('/leads', methods=['GET'])
def get_leads():
    return jsonify(leads_db)

# GET /leads/<id> - Retorna um lead específico
@app.route('/leads/<int:lead_id>', methods=['GET'])
def get_lead_by_id(lead_id):
    for lead in leads_db:
        if lead.get('id') == lead_id:
            return jsonify(lead)
    return jsonify({"error": "Lead not found"}), 404

# POST /leads - Adiciona um novo lead à lista
@app.route('/leads', methods=['POST'])
def create_lead():
    new_lead_data = request.get_json()
    last_id = leads_db[-1]['id'] if leads_db else 0
    new_id = last_id + 1
    new_lead = {
        "id": new_id,
        "nome": new_lead_data['nome'],
        "cpf": new_lead_data['cpf'],
        "telefone": new_lead_data['telefone'],
        "email": new_lead_data['email'],
        "regiao_interesse": new_lead_data['regiao_interesse'],
        "status": "Novo"
    }
    leads_db.append(new_lead)
    return jsonify(new_lead), 201

# DELETE /leads/<id> - Deleta um lead específico
@app.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    lead_to_delete = None
    for lead in leads_db:
        if lead['id'] == lead_id:
            lead_to_delete = lead
            break

    if not lead_to_delete:
        return jsonify({"error": "Lead not found"}), 404
    
    leads_db.remove(lead_to_delete)

    return jsonify({"message": f"Lead with id {lead_id} has been deleted successfully."}), 200
# -----------------------------------

if __name__ == '__main__':
    app.run(debug=True)
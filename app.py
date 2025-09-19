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

# --- NOSSA NOVA ROTA DE CRIAÇÃO ---
# POST /leads - Adiciona um novo lead à lista
@app.route('/leads', methods=['POST'])
def create_lead():
    # Pega os dados JSON que foram enviados no corpo (body) da requisição
    new_lead_data = request.get_json()

    # Lógica simples para gerar um novo ID
    # Encontra o maior ID atual e soma 1
    last_id = leads_db[-1]['id'] if leads_db else 0
    new_id = last_id + 1

    # Cria o dicionário completo do novo lead
    new_lead = {
        "id": new_id,
        "nome": new_lead_data['nome'],
        "cpf": new_lead_data['cpf'],
        "telefone": new_lead_data['telefone'],
        "email": new_lead_data['email'],
        "regiao_interesse": new_lead_data['regiao_interesse'],
        "status": "Novo"  # Todo novo lead começa com o status "Novo"
    }

    # Adiciona o novo lead à nossa "base de dados"
    leads_db.append(new_lead)

    # Retorna o lead que acabamos de criar e o código de status 201 (Created)
    return jsonify(new_lead), 201
# -----------------------------------

if __name__ == '__main__':
    app.run(debug=True)
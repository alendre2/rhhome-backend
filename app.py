from flask import Flask, jsonify

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

# Rota principal (página inicial)
@app.route('/')
def home():
    return "<h1>Backend da RH Home Imobiliária está no ar!</h1>"

# Rota para retornar a lista de todos os leads
@app.route('/leads')
def get_leads():
    return jsonify(leads_db)

# --- NOSSA NOVA ROTA DINÂMICA ---
# Esta rota vai buscar um lead específico pelo seu ID
@app.route('/leads/<int:lead_id>')
def get_lead_by_id(lead_id):
    # Nós percorremos cada 'lead' na nossa lista 'leads_db'
    for lead in leads_db:
        # Verificamos se o valor da chave 'id' do lead atual é igual ao 'lead_id' que recebemos da URL
        if lead.get('id') == lead_id:
            # Se encontrarmos o lead, nós o retornamos como JSON e encerramos a função
            return jsonify(lead)
    
    # Se o loop terminar e não encontrarmos o lead, retornamos uma mensagem de erro.
    # O número 404 é o código de status HTTP para "Não Encontrado".
    # Isso é muito importante para APIs profissionais.
    return jsonify({"erro": "Lead não encontrado"}), 404
# -----------------------------

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# --- Nosso "Banco de Dados" Temporário ---
# No futuro, isso virá de um banco de dados de verdade.
# Por agora, é uma lista de dicionários Python.
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


# --- NOSSA NOVA ROTA DA API ---
# Esta rota vai retornar a lista de todos os leads
@app.route('/leads')
def get_leads():
    # A função 'jsonify' do Flask converte nossa lista Python para o formato JSON
    # e prepara a resposta para o navegador. É a forma correta de retornar APIs.
    return jsonify(leads_db)
# -----------------------------


if __name__ == '__main__':
    app.run(debug=True)
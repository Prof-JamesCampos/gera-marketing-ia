# app.py

import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a Flask app
app = Flask(__name__)

# Configura a API do Google Gemini com a chave do arquivo .env
try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
except AttributeError:
    print("Erro: A chave de API não foi encontrada.")
    print("Por favor, crie um arquivo .env e adicione GOOGLE_API_KEY='SUA_CHAVE'.")
    exit()

# Rota principal que renderiza a nossa página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota que vai receber os dados, processar com a IA e devolver a resposta
@app.route('/gerar', methods=['POST'])
def gerar_marketing():
    # Pega os dados enviados pelo frontend
    dados = request.json
    nome_produto = dados.get('produto')
    caracteristicas = dados.get('caracteristicas')
    publico = dados.get('publico')

    # Validação simples para ver se os dados chegaram
    if not nome_produto or not caracteristicas or not publico:
        return jsonify({'erro': 'Todos os campos são obrigatórios!'}), 400

    # Monta o prompt usando a técnica que aprendemos (Papel, Tarefa, Contexto)
    prompt = f"""
        Aja como um redator de marketing especialista em lançamentos de produtos de tecnologia.
        Sua tarefa é criar um texto de marketing curto e impactante.

        **Produto:** {nome_produto}
        **Características principais:** {caracteristicas}
        **Público-alvo:** {publico}

        Crie um texto com um título chamativo e um parágrafo de descrição que desperte o desejo de compra no público-alvo, destacando os benefícios das características informadas.
    """

    try:
        # Configura o modelo que vamos usar
        model = genai.GenerativeModel('gemini-pro')
        
        # Envia o prompt para a IA e obtém a resposta
        response = model.generate_content(prompt)
        
        # Retorna a resposta da IA em formato JSON para o frontend
        return jsonify({'texto_marketing': response.text})

    except Exception as e:
        # Em caso de erro na API, retorna uma mensagem amigável
        return jsonify({'erro': f'Ocorreu um erro ao contatar a IA: {e}'}), 500

# Roda o servidor quando o script é executado
if __name__ == '__main__':
    app.run(debug=True)
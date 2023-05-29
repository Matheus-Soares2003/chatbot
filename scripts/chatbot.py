from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    response = handle_request(data)
    return jsonify(response)

def handle_request(request):
    # Aqui você pode implementar a lógica do seu chatbot
    # e retornar uma resposta no formato esperado pelo seu widget de chat
    return {
        'type': 'text',
        'content': 'Olá! Eu sou um chatbot criado em Python.'
    }

if __name__ == '__main__':
    app.run()
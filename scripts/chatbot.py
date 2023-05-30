from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message'] #aqui é onde eu recebo a mensagem do front-end
    response = handle_request(message)
    return jsonify(response)

def handle_request(mensagem):
    # Aqui você pode implementar a lógica do seu chatbot
    # e retornar uma resposta no formato esperado pelo seu widget de chat
    return {
        'type': 'text',
        'content': mensagem #aqui é o que eu vou retornar
    }

if __name__ == '__main__':
    app.run()
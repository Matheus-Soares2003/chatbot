from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from random import randint
import json

with open('dados/times.json', 'r', encoding="utf8") as arquivo:
    dados = json.load(arquivo)

app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message'] #aqui é onde eu recebo a mensagem do front-end
    response = handle_request(message)
    return jsonify(response)

def handle_request(mensagem):
    
    pergunta = mensagem.lower().replace(',', ' ')
    palavras_chave = pega_palavras_chave(pergunta)

    if len(palavras_chave) < 2:
        resposta = "Desculpe, não posso te ajudar com isso agora."
    else:
        chave = palavras_chave[0]
        time = palavras_chave[1]
        resposta = mostra_mensagem(chave, time, dados[0][chave][time])

    return {
        'type': 'text',
        'content': resposta #aqui é o que eu vou retornar
    }

def jaccard_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    similarity = intersection / union
    return similarity

def remove_char_especial(palavra):
    nova_pal = ''
    char_especial = {'a':'áàâã', 'e':'éê', 'i':'í', 'o':'óõô', 'u':'ú', 'c': 'ç'}
    for letra in palavra:
        for chave, valor in char_especial.items():
            if letra in valor:
                letra = chave

        nova_pal += letra

    return nova_pal

def pega_palavras_chave(pergunta):
    #chaves = [] -> quando implementar a função de perguntar de mais de uma coisa de cada vez
    #times = [] -> quando implementar a função de perguntar de mais de um time de uma vez
    pal_chave = []
    frase_sep = pergunta.split() 
    frase_sep = [remove_char_especial(palavra) for palavra in frase_sep]

    #Junta o nome dos times que tem nome composto como por exemplo "São Paulo" e "Ponte Preta"
    for c in range(len(frase_sep)):
        if c != len(frase_sep) - 1:
            primeira_pal = frase_sep[c].lower()
            pal_seguinte = frase_sep[c + 1].lower()
            if (primeira_pal == 'sao' and pal_seguinte == 'paulo') or (primeira_pal == 'ponte' and pal_seguinte == 'preta') or (primeira_pal == 'sampaio' and pal_seguinte == 'correa') or (primeira_pal == 'vila' and pal_seguinte == 'nova'):
                frase_sep[c] = ''.join(frase_sep[c] + frase_sep[c + 1])

    #Pega as palavras chaves do json para busca de informações
    for k in dados[0].keys():
        for palavra in frase_sep:
            similaridade = jaccard_similarity(remove_char_especial(k), palavra)
            if similaridade >= 0.77 and len(pal_chave) == 0 and palavra.capitalize() not in dados[0]['times']:
                pal_chave.append(k)
    
    #Pega o time a ser pesquisado
    for time in dados[0]["times"]:
        for palavra in frase_sep:
            similaridade = jaccard_similarity(time.lower(), palavra.lower())
            if remove_char_especial(palavra).lower() == remove_char_especial(time).lower() and len(pal_chave) == 1:
                pal_chave.append(time)

    return pal_chave

def mostra_mensagem(chave, time, valor):
    if chave == 'idolos':
        return f"Alguns dos ídolos do {time} são os seguintes:\n{valor}"
    elif chave == 'rivais':
        return f'Os maiores rivais do {time} são: \n{valor}'
    elif chave == 'mascote':
        return f'O mascote do {time} é o(a) {valor}'
    elif chave == 'jogadores':
        return f'Esses jogadores estão compondo o elenco do {time}: \nGoleiros: \n{dados[0]["goleiros"][time]} \nJogadores: \n{valor}'
    elif chave == 'curiosidades':
        num_curiosidade = randint(0, 2)
        return valor[num_curiosidade]
    elif chave == 'historia':
        return valor
    elif chave == 'titulos':
        return valor
    else:
        return "Desculpe, não entendi a pergunta, poderia repetir?"

if __name__ == '__main__':
    app.run()
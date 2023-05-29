document.addEventListener("keydown", (e) => {
    if(e.key === "Enter"){
        sendMessage()
    }
})

function sendMessage(){
    var mensagem = document.querySelector("#mensagem")
    if (!mensagem.value){
        mensagem.style.border = '1px solid rgb(124, 7, 7)'
        return
    }
    mensagem.style.border = "none"
    fetch("http://localhost:5000/chatbot", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: mensagem.value
        })
    })
    .then(response => response.json())
    .then(addMessage(mensagem.value, 'user'))
    .then(response => addMessage(response.content, 'bot'))
    mensagem.value = ""
}

function addMessage(mensagem, sender){
    var historico = document.querySelector("#message-container")

    if (sender === 'user'){
        var boxMinhaMensagem = document.createElement('div')
        boxMinhaMensagem.className = 'box-minha-mensagem'
    
        var minhaMensagem = document.createElement('p')
        minhaMensagem.className = 'minha-mensagem'
        minhaMensagem.innerHTML = mensagem
    
        boxMinhaMensagem.appendChild(minhaMensagem)
        historico.appendChild(boxMinhaMensagem)
    } else {
        var boxResposta = document.createElement('div')
        boxResposta.className = 'box-resposta'

        var botMensagem = document.createElement('p')
        botMensagem.className = 'mensagem-bot'
        botMensagem.innerHTML = mensagem

        boxResposta.appendChild(botMensagem)
        historico.appendChild(boxResposta)
    }


    historico.scrollTop = historico.scrollHeight
}
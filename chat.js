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
    showHistoric(mensagem.value, "Aqui vem a mensagem do chatbot")
    mensagem.value = ""
}

function showHistoric(mensagem, resposta){
    var historico = document.querySelector("#message-container")

    // Minhas Mensagens

    var boxMinhaMensagem = document.createElement('div')
    boxMinhaMensagem.className = 'box-minha-mensagem'

    var minhaMensagem = document.createElement('p')
    minhaMensagem.className = 'minha-mensagem'
    minhaMensagem.innerHTML = mensagem

    boxMinhaMensagem.appendChild(minhaMensagem)
    historico.appendChild(boxMinhaMensagem)

    // Respostas

    var boxResposta = document.createElement('div')
    boxResposta.className = 'box-resposta'

    var botMensagem = document.createElement('p')
    botMensagem.className = 'mensagem-bot'
    botMensagem.innerHTML = resposta

    boxResposta.appendChild(botMensagem)
    historico.appendChild(boxResposta)

    historico.scrollTop = historico.scrollHeight
}
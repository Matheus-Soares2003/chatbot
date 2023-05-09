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
    alert(mensagem.value)
}
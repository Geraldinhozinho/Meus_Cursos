// cria uma variável com a data atual
const agora = new Date;

// mostra um alerta na tela
// muda o conteúdo do elemento com id="p1"
document.getElementById("p1").innerHTML = `Agora são ${agora.getHours()}h : ${agora.getMinutes()}min`;


const imagem = document.getElementById("img1");

if (agora.getHours() >= 0 ){
    imagem.src ="https://cdn.pensador.com/img/temas/bo/am/boa_madrugada.jpg"
    document.body.style = "background-color: #5d14ddff"
}
if (agora.getHours() >= 4 ){
    imagem.src ="https://amaluz.com.br/wp-content/uploads/2021/08/Faca-sua-imagem-de-bom-dia-.jpg"
    document.body.style = "background-color: rgb(56, 172, 222)"
}
if (agora.getHours() >= 12 ){
    imagem.src ="https://static.mundodasmensagens.com/upload/listas/m/e/mensagens-de-boa-tarde-ka0z3-fxl.jpg"
    document.body.style = "background-color: rgba(238, 207, 27, 1)"
}
if (agora.getHours() >= 18 ){
    imagem.src ="https://i.pinimg.com/originals/66/8f/bc/668fbc77c03aaf0e279414466af5fb0b.jpg"
    document.body.style = "background-color: rgba(108, 108, 106, 1)"

}



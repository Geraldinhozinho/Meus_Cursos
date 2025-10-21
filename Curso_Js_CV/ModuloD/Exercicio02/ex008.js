const data = new Date()
const ano = data.getFullYear()
const imagem = document.createElement('img')
imagem.style.width = "250px"
imagem.style.height = "250px"
imagem.style.borderRadius = "50%"
imagem.style.objectFit = "cover"
imagem.style.objectPosition = "center"
imagem.style.margin = "auto"

const p1 = document.getElementById('p1')
p1.style.textAlign = "center"

const minhaDiv = document.getElementById('div1')

function mudar() {
    const sexo = document.getElementsByName('inp')
    const oano = document.getElementById('year')
    const idade = ano - Number(oano.value)

    if (sexo[0].checked && Number(oano.value) >= 1930 && Number(oano.value) < ano) {
        imagem.src = "https://uploads.metropoles.com/wp-content/uploads/2023/07/01210110/Uganda-1.jpg"
        p1.innerText = `Homem de ${idade} anos encontrado!`
        minhaDiv.appendChild(imagem)

    }
    else if (sexo[1].checked && Number(oano.value) >= 1930 && Number(oano.value) < ano){
            imagem.src = "https://guiadehospedagem.com.br/wp-content/uploads/2024/06/Firefly-Um-retrato-realista-de-uma-linda-mulher-jovem-72730.jpg"
            p1.innerText = `Mulher de ${idade} anos encontrada!`
            minhaDiv.appendChild(imagem)
        }
    else {
         window.alert('Preencha os campos corretamente!')
    } 
}
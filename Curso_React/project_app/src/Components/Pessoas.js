export function Pessoas (props){
    return(
        <div>
            <h1>Olá, meu nome é: {props.nome}</h1>
            <p>Minha idade é: {props.idade}</p>
            <p>Sou do estado do {props.estado}</p>
        </div>
    )
}
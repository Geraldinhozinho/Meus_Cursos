
import PropTypes from 'prop-types';

Props.propTypes = {
nome: PropTypes.string.isRequired,
idade: PropTypes.number.isRequired,
estado: PropTypes.string.isRequired
}
Props.defaultProps = {
    nome: "Mario",
}
export function Props({nome, idade, estado}){
    return(
        <div>
            <h1>Olá, meu nome é: {nome}</h1>
            <p>Minha idade é: {idade}</p>
            <p>Sou do estado do {estado}</p>
        </div>
    )
    
};




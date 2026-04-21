import logo from './logo.svg';
import './App.css';
import { HelloWorld } from './Components/HelloWorld';
import { Pessoas } from './Components/Pessoas';
function App() {



  return (
    <div className="App">
      <h1>Hello, World!</h1>
      <p>Welcome to my first React project.</p>
      <Pessoas nome="João" idade={30} estado="São Paulo"/>

    </div>
  );
}

export default App;

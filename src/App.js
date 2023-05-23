import './App.css';
import Search from './components/Search';
// import Pokedex from 'pokedex-promise-v2'

// const p = new Pokedex()
// p.getPokemonByName('charmander', (response, error) => {
//   if (!error){
//     console.log(response)
//   }
//   else{
//     console.log(error)
//   }
// })

function App() {
  return (
    <div className="App">
      <Search />
    </div>
  );
}

export default App;

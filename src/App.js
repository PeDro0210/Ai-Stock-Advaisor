import './styles/App.css';
import SymbolSearcher from './components/SymbolSearcher.js'
import './styles/MenuButton.css';
import { useState } from 'react';

function App() {
  // is like a conditional render
  const [showSymbolSearcher, setShowSymbolSearcher] = useState(false);
  
  // Change the state of the menu button
  const toggleSymbolSearcher = () => {
    setShowSymbolSearcher(!showSymbolSearcher);
  };

  return (
    <div className="Stock Adivsor">
      <header className="App-header">
      <button className='MenuButton' onClick={toggleSymbolSearcher}>Menu</button>
      {/* Add some cool css transtition and good to go */}
      {showSymbolSearcher && <SymbolSearcher />}
      </header>
    </div>
  );
}

export default App;

import '../styles/SymbolSearcher.css';
import {useState} from 'react';

function SymbolSearcher(){
    const [symbol, setSymbol] = useState('');
    const [data, setData] = useState([]);

    const handleSearch = () => {
        fetch(`http://127.0.0.1:5000//SymbolSearcher/<${symbol}>`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setData(data);
            })
            .catch(error => {
                console.log(error);
            });
    }

    return(
        <div>
            <input id='symbol-input' type='text' placeholder='Write Symbol' className='SymbolSeacher-textbox' value={symbol} onChange={(e) => setSymbol(e.target.value)} />
            <button id='symbol-searcher-button' className='symbolSearcher-button' onClick={handleSearch}>Search</button>
            <div className = 'ShowSymbolSearcher'> 
                {Array.isArray(data) && data.map((item,index) => (
                    console.log(item),
                    <button  key={index} data-name={item['2. name']}>
                    {item['1. symbol']}, {item['2. name']}
                </button>
                ))}
                
            </div>
        </div>
    )
}

export default SymbolSearcher;

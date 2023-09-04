import '../styles/SymbolSearcher.css';
import {Component} from 'react';


class SymbolSearcher extends Component {
    // Good, now this is a class and now I understand how the use state works
    constructor(props) {
        super(props);
        this.state = {
            symbol: '',
            data: []
        };
    }

    handleSearch = () => {
        fetch(`http://127.0.0.1:5000//SymbolSearcher/<${this.state.symbol}>`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.setState({ data: data });
            })
            .catch(error => {
                console.log(error);
            });
    }

    render() {
        return (
            <div>
                <input id='symbol-input' type='text' placeholder='Write Symbol' className='SymbolSeacher-textbox' value={this.state.symbol} onChange={(e) => this.setState({ symbol: e.target.value })} />
                <button id='symbol-searcher-button' className='symbolSearcher-button' onClick={this.handleSearch}>Search</button>
                <div className='ShowSymbolSearcher'>
                    {Array.isArray(this.state.data) && this.state.data.map((item, index) => (
                        console.log(item),
                        <button key={index} data-name={item['2. name']}>
                            {item['1. symbol']}, {item['2. name']}
                        </button>
                    ))}

                </div>
            </div>
        );
    }
}

export default SymbolSearcher;
import '../styles/SymbolSearcher.css';
import {Component} from 'react';
import StockGraph from './Graph.js';
import Chat from './Chat.js';

class SymbolSearcher extends Component {
    // TODO: Comment in to this shit.
    constructor(props) {
        super(props);
        this.state = {
            symbol: '',
            data: [],
            FoundSymbol:'',
            showGraph: false
            //Used to store the search symbol, data retrived from the search, selected symbol and whether to display de chart
        };
    }

    HandleSearch = () => {
        fetch(`http://127.0.0.1:5000//SymbolSearcher/<${this.state.symbol}>`) //Fetch function to send a GET request to URL
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.setState({ data: data }); // Once it have an anwer back, it's converted into a JSON format and stored in a data state
            })
            .catch(error => {
                console.log(error);
            });
    }

    SelectSymbol = (e) => {
        console.log("Symbol Catch: "+e);
        this.setState({FoundSymbol: e }); //take symbol as an argument and stores it in the "FoundSymbol" state.
    }

    AddGraph = () => { //function used to show the graph related with the selected symbol
        this.setState({showGraph: true});
    }

    render() {
        return (
            <div>

                <input
                    id="symbol-input"
                    type="text"
                    placeholder="Write Symbol"
                    className="SymbolSeacher-textbox"
                    onChange={(e) => this.setState({ symbol: e.target.value })}
                    onKeyDown={(e) => {{if (e.key === 'Enter') 
                        {this.HandleSearch(); 
                        document.getElementById("symbol-input").value = "";}}}}
                />

                <button
                    id="symbol-searcher-button"
                    className="symbolSearcher-button"
                    onClick={this.HandleSearch}
                >
                    Search
                </button>

                <div className="ShowSymbolSearcher">
                    {Array.isArray(this.state.data) &&
                        this.state.data.map((item, index) => {
                            console.log(item);
                            return (
                                <button
                                    key={index}
                                    data-name={item["2. name"]}
                                    onClick={() => {
                                        this.AddGraph();
                                        this.SelectSymbol(item["1. symbol"]);
                                    }}
                                >
                                    {item["1. symbol"]}, {item["2. name"]}
                                </button>
                            );
                        })}

                </div>
                {
                    this.state.showGraph && (
                        <>
                            <StockGraph
                                key={this.state.FoundSymbol}
                                FoundSymbol={this.state.FoundSymbol}
                            />
                            <Chat
                                key={this.state.FoundSymbol}
                                FoundSymbol={this.state.FoundSymbol}
                                data={this.state.data}
                            />
                            {console.log("Create components" + this.state.FoundSymbol)}
                        </>
                    )
                }
            </div>

        );
    }
}

export default SymbolSearcher;  
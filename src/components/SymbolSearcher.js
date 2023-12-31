import '../styles/SymbolSearcher.css';
import { Component } from 'react';
import StockGraph from './Graph.js';
import Chat from './Chat.js';

class SymbolSearcher extends Component {
    constructor(props) {
        super(props);
        this.state = {
            symbol: '',
            data: [],
            FoundSymbol: '',
            showGraph: false
        };
    }

    // Este método realiza una búsqueda utilizando la API y actualiza el estado con los resultados.
    HandleSearch = () => {
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

    // Este método se llama cuando se hace clic en un botón de símbolo y actualiza el estado con el símbolo seleccionado.
    SelectSymbol = (e) => {
        console.log("Symbol Catch: " + e);
        this.setState({ FoundSymbol: e });
    }

    // Este método se llama cuando se hace clic en un botón "AddGraph" y muestra el gráfico.
    AddGraph = () => {
        this.setState({ showGraph: true });
    }

    render() {
        return (
            <div>
                {/* Input para ingresar el símbolo */}
                <input
                    id="symbol-input"
                    type="text"
                    placeholder="Write Symbol"
                    className="SymbolSeacher-textbox"
                    onChange={(e) => this.setState({ symbol: e.target.value })}
                    onKeyDown={(e) => {
                        if (e.key === 'Enter') {
                            this.HandleSearch();
                            document.getElementById("symbol-input").value = "";
                            if (this.state.showGraph) {
                                window.location.reload();
                            }
                        }
                    }}
                />

                {/* Botón de búsqueda */}
                <button
                    id="symbol-searcher-button"
                    className="symbolSearcher-button"
                    onClick={this.HandleSearch}
                >
                    Search
                </button>

                {/* Mostrar los resultados de la búsqueda */}
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
                    {/* TODO: Poner el mensaje mas bonito*/}
                    {this.state.data["Error"] && (
                        <p>No se encontraron resultados</p>
                    )}
                </div>

                {/* Mostrar el gráfico y el chat si showGraph es true */}
                {this.state.showGraph && (
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
                )}
            </div>
        );
    }
}

export default SymbolSearcher;

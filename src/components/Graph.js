import {Component} from 'react';
import '../styles/Graph.css';
import {Line} from 'react-chartjs-2';
import Chart from 'chart.js/auto';
class StockGraph extends Component{
    constructor(props){
        super(props);
        this.state ={
            Symbol: '',
            data : [],
            chart: true
        }
    }

    HandleSearch = () => {
        // All the fetching from the API that ME PEDRO Created
        console.log("Will use: "+this.state.Symbol);
        fetch(`http://127.0.0.1:5000//StockData/<${this.state.Symbol}>`)
            .then(response => response.json())
            .then(data => {
                this.setState({ data: data }, () => {
                    this.createChart();
                }); 
            })
            .catch(error => {
                console.log(error);
            });
    }

    createChart() {
        const ctx = document.getElementById('stockChart').getContext('2d'); // Mira donde esta el canvas para poder hacer el render de la grafica
        
        // Castea todo los precios para poder ser mapeados en la grafica
        const pricesAsFloats = this.state.data.Prices.map(price => parseFloat(price));
        const priceOpenAsFloats = this.state.data.Open.map(price => parseFloat(price));

        this.setState({
            chart: (
                <Line //Crea el component de la libreria de chartjs (Si no fuera por esa libreria dios, ya me hubiera matado lit)
                    data={{
                        labels: this.state.data.Dates.map(data => data), //Mapea los datos para que el componente los pueda leer chido
                        datasets: [
                            // TODO: Add more Data to the graph if possible
                            {
                                label: 'Close',
                                data: pricesAsFloats,
                                borderColor: 'rgba(75, 192, 192, 1)',
                            },
                            {
                                label: 'Open',
                                data: priceOpenAsFloats,
                                borderColor: 'rgba(192, 75, 192, 1)',
                            }
                        ],
                    }}
                    options={{}} //El boiler plate tenia esto, no se si dejarlo o se rompe todo
                    ctx={ctx}
                />
            ),
        });
    }

    componentDidMount() {
        const { FoundSymbol } = this.props;
        this.setState({ Symbol: FoundSymbol }, () => {
            console.log("Found Symbol for Graph " + this.state.Symbol);
            this.HandleSearch();
        });
    }

    render(){
        return(
            <div className='GraphDisplay'>
                <canvas id="stockChart" width="400" height="200"></canvas> {/* Aqui crea el canvas para que despues la grafica pueda ser puesta */} 
                <div>
                    {this.state.chart} {/* Grafica */}
                </div>
            </div>
        )
    }
}

export default StockGraph;

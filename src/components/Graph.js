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

    // Comment all this thing and see how does everything work
    createChart() {
        // Get the context from the canvas element
        const ctx = document.getElementById('stockChart').getContext('2d');
        console.log("Creating Chart");
        console.log(this.state.data);
        console.log(this.state.data.Dates);
        console.log(this.state.data.Prices);
        
        if (Array.isArray(this.state.data.Dates) && Array.isArray(this.state.data.Prices)) {
            console.log("created");
            // Cast Prices as floats
            const pricesAsFloats = this.state.data.Prices.map(price => parseFloat(price));
            const priceOpenAsFloats = this.state.data.Open.map(price => parseFloat(price));
    
            this.setState({
                chart: (
                    <Line
                        data={{
                            labels: this.state.data.Dates.map(data => data), // Use data directly, not data.Dates
                            datasets: [
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
                        options={{}}
                        ctx={ctx}
                    />
                ),
            });
        }
    }


    componentDidMount() {
        const { FoundSymbol } = this.props;
        this.setState({ Symbol: FoundSymbol }, () => {
            console.log("Found Symbol for Graph " + this.state.Symbol);
            this.HandleSearch(); // Call HandleSearch in the callback
        });
    }

    render(){
        return(
            <div className='GraphDisplay'>
                <canvas id="stockChart" width="400" height="200"></canvas>
                <div>
                    {this.state.chart}
                </div>
            </div>
        )
    }
}

export default StockGraph;

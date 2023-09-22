import '../styles/Graph.css';
import {Component} from 'react';

class StockGraph extends Component{
    constructor(props){
        super(props);
        this.state ={
            Symbol: '',
            data : [],
        }
    }

    HandleSearch = () => {
        fetch(`http://127.0.0.1:5000//StockData/<${this.state.Symbol}>`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.setState({ data: data });
                return data;
            })
            .catch(error => {
                console.log(error);
            });
    }


    componentDidMount() {
        const {FoundSymbol} = this.props;
        this.setState({Symbol: FoundSymbol}, () => {
            this.HandleSearch();
            console.log("Found Symnol "+this.state.Symbol)
        });
    }

    render(){
        return(
            <div>
                {Array.isArray(this.state.data) && this.state.data.map((item, index) => (
                    console.log(item)
                    // data["Meta Data"]["Time Series (5min)"][take all the keys and values]
                    
                    // TODO: Do the graph with the data with Chart.js

                    


                ))} 
            <div>
                <h1>Stock Graph</h1>
                <p>Symbol: {this.state.Symbol}</p>
                
            </div>

            </div>
        )
    }
}

export default StockGraph;

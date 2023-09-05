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
            console.log(this.state.data);
        });
    }

    render(){
        return(
            <div className='ShowSymbolSearcher'>
                {Array.isArray(this.state.data) && this.state.data.map((item, index) => (
                    console.log(item)
                    // Look how the json returns the data and based on that (and Ernesto's explanation) see how to graph it.
                ))} 
            </div>
        )
    }
}

export default StockGraph;
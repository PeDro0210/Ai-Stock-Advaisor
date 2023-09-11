import { Component } from 'react';

class Chat extends Component {
    constructor(props) {
        super(props);
        this.state = {
            Symbol: '',
            Prompt:'',
            Data: [],
            ChatgptPrompt: ''
        }
    }

    OpenAiPrompt = () => {
        fetch(`http://127.0.0.1:5000//AskAI/<${this.state.Prompt}>`)
            .then(response => response.json())
            .then(data => {
                // Make a cool looking chat box
                console.log(data);
                this.setState({ ChatgptPrompt: data['message'] });
                return data;
            })
            .catch(error => {
                console.log(error);
            });
    }


    ReadStockData = () => {
        fetch(`http://127.0.0.1:5000//CheckStockData/<${this.state.Symbol}>`)
    }



    componentDidMount() {
        const {FoundSymbol} = this.props;
        const {data} = this.props;
        this.setState({ Symbol: FoundSymbol }, () => {
            console.log("Found Symbol for Chat " + this.state.Symbol)
        });

        this.setState({ Data: data }, () => {
            this.ReadStockData();
        });
    }

        render() {
            return (
                <div>
                    <input onChange={(e) => this.setState({ Prompt: e.target.value })} />

                    <button
                        id="OpenAI-button"
                        onClick={this.OpenAiPrompt}
                    >
                        Ask Advisor
                    </button>

                    <button
                        id="LookStocks-button"
                        onClick={this.ReadStockData}
                    >
                    Look at Stocks
                    </button>
                    
                </div>
            );
        }
    } 

export default Chat;
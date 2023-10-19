import { Component } from 'react';
import "../styles/chat.css"
class Chat extends Component {

    constructor(props) {
        super(props);
        this.state = {
            Symbol: '',
            Prompt:'',
            Data: [],
            ChatgptPrompt: []
        }
    }

    OpenAiPrompt = () => {
        fetch(`http://127.0.0.1:5000//AskAI/<${this.state.Prompt}>`)
            .then(response => response.json())
            .then(data => {
                this.setState((prevState) => ({
                    ChatgptPrompt: [...prevState.ChatgptPrompt,  data.message],
                }));
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
        const { FoundSymbol, data } = this.props;
        this.setState({ Symbol: FoundSymbol, Data: data }, () => {
            console.log("Found Symbol for Chat " + this.state.Symbol);
            this.ReadStockData();
        });
    }

    // TODO: Make it scroll automatically when a new prompt is added

    render() {
        return (
            <div>
                <input onChange={(e) => this.setState({ Prompt: e.target.value })} 
                class="Chat-Textbox" id = "Chat-boxText" 
                onKeyDown={(e) => {{if (e.key === 'Enter') {this.OpenAiPrompt(); document.getElementById("Chat-boxText").value = "";}}}}
                />

                <button
                    id="OpenAI-button"
                    onClick={() => {
                        this.OpenAiPrompt();
                        document.getElementById("Chat-boxText").value = "";
                    }}
                    className="Chat-buttonAskAdvisor"
                >
                    Ask
                </button>

                <button
                    id="LookStocks-button"
                    onClick={this.ReadStockData}
                    className = "Chat-LookStocks"
                >
                Look at Stocks
                </button>

                <div>
                    {
                    <div className='Chat-Box' style={{ overflowY: 'scroll'}} ref ={this.chatBoxRef}>
                        {this.state.ChatgptPrompt.map((item, index) => {
                            console.log(item);
                            return (
                                <div key={index}>
                                    <text class="Chat-prompt">{item}</text>
                                    <br />
                                    <br />
                                </div>
                            );
                        })}
                    </div>
                    }
                </div>
                
            </div>
        );
    }

} 

export default Chat;
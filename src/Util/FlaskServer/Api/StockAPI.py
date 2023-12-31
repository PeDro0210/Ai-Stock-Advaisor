import flask as fl
from flask_cors import CORS
from StockProcess import Stock
import AiAssistant as Ai

app=fl.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/SymbolSearcher/<StockName>")
def SymbolSearcher(StockName):
    StockName = StockName.replace("<", "").replace(">", "")
    return Stock(StockName).SymbolSearcher()

@app.route("/StockData/<StockName>")
def StockData(StockName):
    StockNameClean= StockName.replace("<", "").replace(">", "")
    print(f"Graph {StockNameClean}")
    data = Ai.CreateGraph(Stock(StockNameClean).StockData(StockNameClean))
    return data

@app.route("/DelStock/<StockName>")
def DelStock(StockName):
    return Stock(StockName).DelStock()

@app.route("/AskAI/<Prompt>")
def AskAI(Prompt):
    Prompt = Prompt.replace("<", "").replace(">", "")
    return Ai.ask(Prompt)

@app.route("/CheckStockData/<StockName>")
def CheckStockData(StockName):
    print(f"CheckStockData {StockName}")
    StockName = StockName.replace("<", "").replace(">", "")
    return Ai.CheckStockData(Stock(StockName).StockData(StockName), StockName) 

if __name__ == "__main__":
    app.run(debug=True)


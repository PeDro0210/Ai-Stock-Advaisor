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
    StockName = StockName.replace("<", "").replace(">", "")
    print(StockName)
    data = Stock(StockName).StockData(StockName)
    print(data)
    return data

@app.route("/DelStock/<StockName>")
def DelStock(StockName):
    return Stock(StockName).DelStock()

@app.route("/AskAI/<Prompt>")
def AskAI(Prompt):
    Prompt = Prompt.replace("<", "").replace(">", "")
    print(Prompt)
    return Ai.ask(Prompt)

@app.route("/CheckStockData/<StockName>")
def CheckStockData(StockName):
    StockName = StockName.replace("<", "").replace(">", "")
    return Ai.CheckStockData(Stock(StockName).StockData(StockName))




if __name__ == "__main__":
    app.run(debug=True)
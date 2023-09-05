import flask as fl
from flask_cors import CORS
from StockProcess import Stock

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


if __name__ == "__main__":
    app.run(debug=True)
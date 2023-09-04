import load_dotenv as env
import requests as req 
import os

# Hahaha, Have to make the flask server to make this work, so i can get the data from the front end
class Stock:
    def __init__(self, StockSymbol):
        self.StockSymbol = StockSymbol
        env.load_dotenv()
        self.AlphaKey = os.getenv("AlphaKey")


    # General Methods
    def UrlCreator(self ,StockName, function) -> str:
        match function:
            case "SYMBOL_SEARCH":
                return "https://www.alphavantage.co/query?function="+ function +"&keywords=" + StockName + "&apikey=" + self.AlphaKey
            case "TIME_SERIES_INTRADAY":
                return "https://www.alphavantage.co/query?function="+ function +"&symbol=" + StockName + "&interval=5min"  + "&apikey=" + self.AlphaKey
            case _:
                return ""

    # All Symbol Searchers
    def SymbolSearcher(self):                
        try:
            response = req.get(self.UrlCreator(self.StockSymbol, "SYMBOL_SEARCH"))
            response.raise_for_status()
            data = response.json()
            if "bestMatches" in data:
                if data["bestMatches"] == []:
                    return {"Error": "No results"}
                else:
                    usefulinfo = data["bestMatches"]
                    return usefulinfo
            else:
                return {"Error": "API BUGGINT OUT MAN"}
        
        except req.exceptions.HTTPError as err:
            return "Error"
        except req.exceptions.RequestException as err:
            return "Error"
        
    def StockData(self, StockName):
        try:
            if StockName == "No results found":
                return {"Error": "No results found"}
            
            response = req.get(self.UrlCreator(StockName, "TIME_SERIES_INTRADAY"))
            response.raise_for_status()
            data = response.json()
            return data
        
        except req.exceptions.HTTPError as err:
            return {"Error": "No results found"}
        except req.exceptions.RequestException as err:
            return {"Error": "req.exceptions.RequestException"}
        except data.exceptions.JSONDecodeError as err:
            return {"Error": "data.exceptions.JSONDecodeError"}
        
    def DelStock(self):
        del self


        
  






    



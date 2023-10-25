import openai as ai
import os
import json
import load_dotenv as env



env.load_dotenv()
information_loader = json.load(open('src/Util/Data/initial_information.json','r'))
ai.api_key = os.getenv("AI_API")
initial_info = {"role":"system","content":f"{information_loader['AiPrompt']}"}
chat_log = [initial_info]

# TODO: make a function for having the conversations saved in a json file

def CheckStockData(StockData, StockName):

    StockData = StockData['Time Series (5min)'] #Just some specific symbols have this key 
    AllStocks = {"Open":[],"Close":[]}
    for i in StockData:

        StockDataOpen = StockData[i]['1. open']
        StockDataClose = StockData[i]['4. close']
        chat_log.append({"role":"system","content":f"Symbol: {StockName} Open: {StockDataOpen} Close: {StockDataClose}"})
        AllStocks['Open'].append(StockDataOpen)
        AllStocks['Close'].append(StockDataClose)

    return AllStocks 


def ask(message):
    chat_log.append({"role":"user","content":f"{message}"})
    
    Assistant_response = ai.ChatCompletion.create( #method to generate a response
        model="gpt-4-0613",
        messages=chat_log,
        temperature=0.5,
        stop=None
    )
    
    chat_log.append({"role":"assistant","content":Assistant_response['choices'][0]['message']['content']})

    return {"message":Assistant_response['choices'][0]['message']['content']}

def CreateGraph(StockData):
    print(StockData)
    StockData = StockData['Time Series (5min)'] #Just some specific symbols have this key 
    AllStocks = {"Dates":[],"Prices":[],"Open":[]} #Empty dictionary

    for i in StockData:
        StockDataOpen = StockData[i]['1. open']
        StockDataClose = StockData[i]['4. close']
        AllStocks['Dates'].append(i)
        AllStocks['Open'].append(StockDataOpen)
        AllStocks['Prices'].append(StockDataClose)
    print(AllStocks)
    return AllStocks


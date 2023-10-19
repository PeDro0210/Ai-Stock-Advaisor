import openai as ai
import os
import json
import load_dotenv as env


# Haha, otra cosa con API o lo puedo trasvasar a JS.
env.load_dotenv()
information_loader = json.load(open('src/Util/Data/initial_information.json','r'))
ai.api_key = os.getenv("AI_API")
initial_info = {"role":"system","content":f"{information_loader['AiPrompt']}"}
chat_log = [initial_info]

def CheckStockData(StockData, StockName):
    # TODO: Separate the StockData in 4 parts

    StockData = StockData['Time Series (5min)']
    AllStocks = {"Open":[],"Close":[]}
    # Just take the Open and close
    for i in StockData:

        StockDataOpen = StockData[i]['1. open']
        StockDataClose = StockData[i]['4. close']
        chat_log.append({"role":"system","content":f"Symbol: {StockName} Open: {StockDataOpen} Close: {StockDataClose}"})
        AllStocks['Open'].append(StockDataOpen)
        AllStocks['Close'].append(StockDataClose)

    return AllStocks 


def ask(message):
    chat_log.append({"role":"user","content":f"{message}"})
    
    Assistant_response = ai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=chat_log,
        temperature=0.5,
        stop=None
    )
    
    chat_log.append({"role":"assistant","content":Assistant_response['choices'][0]['message']['content']})

    return {"message":Assistant_response['choices'][0]['message']['content']}

def CreateGraph(StockData):
    print(StockData)
    StockData = StockData['Time Series (5min)']
    AllStocks = {"Dates":[],"Prices":[],"Open":[]}

    for i in StockData:
        StockDataOpen = StockData[i]['1. open']
        StockDataClose = StockData[i]['4. close']
        AllStocks['Dates'].append(i)
        AllStocks['Open'].append(StockDataOpen)
        AllStocks['Prices'].append(StockDataClose)
    print(AllStocks)
    return AllStocks


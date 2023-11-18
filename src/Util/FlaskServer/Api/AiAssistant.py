import os
import json
import load_dotenv as env
import openai as ai


from Classes.JsonManager import JsonFile
from Classes.CsvManager import CsvFile
# from Interfaces.XmlManager import InterfaceFile



#Global variables

env.load_dotenv("src/Util/Keys.env")
information_loader = json.load(open('src/Util/FlaskServer/Api/Data/Initial_information.json','r')) #TODO: make that the launcher dont need this big ass path
ai.api_key = os.getenv("AI_API")
initial_info = {"role":"system","content":f"{information_loader['AiPrompt']}"}
chat_log = []

#Global Objects

JsonManager = JsonFile('src/Util/FlaskServer/API/Data/DB.json')
CsvManager = CsvFile('src/Util/FlaskServer/API/Data/DB.csv')



def CheckStockData(StockData, StockName): #takes a while to check all the data

    def DeleateOldStockData():
        for prompt in chat_log:
            if (prompt['content'][0:9] == "StockData:"):
                chat_log.remove(prompt)

    #Removes any other StockCalls for the token quantity
    DeleateOldStockData()

    StockData = StockData['Time Series (5min)'] #Just some specific symbols have this key 
    AllStocks = {"Open":[],"Close":[]}
    
    for i in StockData:
        StockDataOpen = StockData[i]['1. open']
        StockDataClose = StockData[i]['4. close']

        chat_log.append({"role":"system","content":
                        f"StockData: Symbol: {StockName} Open: {StockDataOpen} Close: {StockDataClose}"})
        
        AllStocks['Open'].append(StockDataOpen)
        AllStocks['Close'].append(StockDataClose)

    return AllStocks 


def ask(message):
    chat_log.append({"role":"user","content":f"{message}"})
    
    Assistant_response = ai.chat.completions.create( #method to generate a response
        model="gpt-4-0613",
        messages=chat_log,
    )

    # Load for persistence
    JsonManager.SaveInfo(message,Assistant_response.choices[0].message.content)
    CsvManager.SaveInfo(message,Assistant_response.choices[0].message.content)
    
    chat_log.append({"role":"assistant","content":Assistant_response.choices[0].message.content})

    return {"message":Assistant_response.choices[0].message.content}

def CreateGraph(StockData):
    StockData = StockData['Time Series (5min)'] #Just some specific symbols have this key 
    AllStocks = {"Dates":[],"Prices":[],"Open":[]} 

    for i in StockData:
        StockDataOpen = StockData[i]['1. open']
        StockDataClose = StockData[i]['4. close']
        AllStocks['Dates'].append(i)
        AllStocks['Open'].append(StockDataOpen)
        AllStocks['Prices'].append(StockDataClose)
    return AllStocks




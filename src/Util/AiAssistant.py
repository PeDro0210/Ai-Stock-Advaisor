import openai as ai
import os
import json
import load_dotenv as env
import base64



env.load_dotenv()
information_loader = json.load(open('src/Util/Data/initial_information.json','r'))
ai.api_key = os.getenv("AI_API")
initial_info = {"role":"system","content":f"{information_loader['AiPrompt']}"}
chat_log = [initial_info]



def CheckStockData(StockData, StockName): #takes a while to check all the data

    #TODO: optimizenlo HAHA
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

    SaveInfo(message,Assistant_response['choices'][0]['message']['content']) #Info saving for idunno future stuff

    return {"message":Assistant_response['choices'][0]['message']['content']}

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



def SaveInfo(message,AIPrompt):
    message_bytes = message.encode('utf-8')
    padding = len(message_bytes) % 4 #si o si el largo tiene que ser un multiplo de 4
    if padding != 0:
        message_bytes += b'=' * (4 - padding) #agrega el "padding"

    try:
        coded_message = base64.b64decode(message_bytes)
    except Exception as err:
        # Si no cumple con el formato de base64, no lo codifica y pone el mensaje original
        coded_message = message_bytes

    PersistentData = {f"message:{coded_message}":{ #a fancy way to save the data
        "message":message,
        "AIPrompt":AIPrompt
    }}

    with open('src/Util/Data/initial_information.json','r+') as file:
        data = json.load(file)
        data.update(PersistentData)
        file.seek(0)
        json.dump(data,file,indent=4)
        file.truncate()
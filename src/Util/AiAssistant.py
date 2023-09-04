import openai as ai
import os
import json
import load_dotenv as env


# Haha, otra cosa con API o lo puedo trasvasar a JS.
env.load_dotenv()
information_loader = json.load(open('Data/initial_information.json', 'r'))
ai.api_key = os.getenv("AI_API")
initial_info = {"role":"system","content":f"{information_loader['AiPrompt']}"}
chat_log = [initial_info]

def CheckStockData(StockData):
    chat_log.append({"role":"system","content":f"Stock Name:{StockData['Meta Data']['2. Symbol']}. StockData:{StockData['Time Series (5min)']}"})
    return StockData['Time Series (5min)']


def ask(message) -> str:
    chat_log.append({"role":"user","content":f"{message}"})
    
    Assistant_response = ai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=chat_log,
        temperature=0.5,
        stop=None
    )
    
    chat_log.append({"role":"assistant","content":Assistant_response['choices'][0]['message']['content']})

    return Assistant_response

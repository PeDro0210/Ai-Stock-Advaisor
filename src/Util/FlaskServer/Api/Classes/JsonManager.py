from Classes.Interfaces.IFileManager import InterfaceFile
import json

class JsonFile(InterfaceFile):
    def __init__(self, path):
        self.path = path

    def SaveInfo(self, messages, response):
        coded_message = InterfaceFile.Encoding(message=messages)
        PersistentData = {f"message:{coded_message}":{ #a fancy way to save the data
            "message":messages,
            "AIPrompt":response
        }}

        with open('src/Util/FlaskServer/API/Data/DB.json','r+') as file:
            data = json.load(file)
            data.update(PersistentData)
            file.seek(0)
            json.dump(data,file,indent=4)
            file.truncate()

if __name__ == "__main__":
    print("This is a module, not a script!")
from Classes.Interfaces.IFileManager import InterfaceFile


class CsvFile(InterfaceFile):
    def __init__(self, path):
        self.path = path

    def SaveInfo(self, messages, response):
        coded_message = InterfaceFile.Encoding(message=messages)
        PersistentData = {f"message:{coded_message}":{ #a fancy way to save the data
            "message":messages,
            "AIPrompt":response
        }}

        with open('src/Util/FlaskServer/API/Data/DB.csv','r+') as file:
            data = file.readlines()
            data.append(PersistentData)
            file.seek(0)
            # TODO: Formatear a csv :D
            file.writelines(data)
            file.truncate()
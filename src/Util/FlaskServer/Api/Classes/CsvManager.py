from Classes.Interfaces.IFileManager import InterfaceFile
import pandas as pd

class CsvFile(InterfaceFile):
    def __init__(self, path):
        self.path = path

    def SaveInfo(self, messages, response):
        PersistentData = { #a fancy way to save the data
            "MessageHash":InterfaceFile.Encoding(message=messages),
            "message":messages,
            "AIPrompt":response
        }

        data = pd.read_csv(self.path)
        data = data._append(PersistentData, ignore_index=True)
        data.to_csv(self.path, index=False)
from Classes.Interfaces.IFileManager import InterfaceFile
import pandas as pd

from Classes.Interfaces.IFileManager import InterfaceFile
import xml.etree.ElementTree as ET
import os

class XmlFile(InterfaceFile):
    def __init__(self, path):
        self.path = path

    def SaveInfo(self, messages, response):
        coded_message = InterfaceFile.Encoding(message=messages)
        PersistentData = {f"message:{coded_message}": {
            "message": messages,
            "AIPrompt": response
        }}

        File = pd.read_xml(self.path)
        File = File._append(PersistentData, ignore_index=True)
        File.to_xml(self.path)

    # TODO: Implementar el guardado de datos en XML

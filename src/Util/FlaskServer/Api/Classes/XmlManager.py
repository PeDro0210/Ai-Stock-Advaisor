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
        persistent_data = {"message": coded_message, "AIPrompt": response}

        # Si el archivo no existe, crear un nuevo archivo XML
        if not os.path.exists(self.path):
            root = ET.Element("root")
            tree = ET.ElementTree(root)
            tree.write(self.path)

        # Leer el archivo XML existente
        tree = ET.parse(self.path)
        root = tree.getroot()

        # Crear un nuevo elemento 'entry' con la información
        entry = ET.SubElement(root, "entry")
        for key, value in persistent_data.items():
            child = ET.SubElement(entry, key)
            child.text = str(value)

        # Guardar el árbol XML actualizado de vuelta al archivo
        tree.write(self.path)
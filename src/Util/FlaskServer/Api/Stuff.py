from Classes.JsonManager import JsonFile
from Classes.CsvManager import CsvFile
from Classes.XmlManager import XmlFile

Json = JsonFile(path='src/Util/FlaskServer/API/Data/DB.json')
Csv = CsvFile(path='src/Util/FlaskServer/API/Data/DB.csv')
Xml = XmlFile(path='src/Util/FlaskServer/API/Data/DB.xml')


Csv.SaveInfo(messages="Hola", response="Hola")
Json.SaveInfo(messages="Hola", response="Hola")
Xml.SaveInfo(messages="Hola", response="Hola")
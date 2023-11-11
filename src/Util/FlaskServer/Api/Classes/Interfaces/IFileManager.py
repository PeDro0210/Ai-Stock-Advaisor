from abc import ABC, abstractmethod
import base64

class InterfaceFile(ABC):
    @abstractmethod
    def SaveInfo(self, message, response):
        pass
    
    def Encoding(message):
        message_bytes = message.encode('utf-8')
        padding = len(message_bytes) % 4 #si o si el largo tiene que ser un multiplo de 4
        if padding != 0:
            message_bytes += b'=' * (4 - padding) #agrega el "padding"

        try:
            return base64.b64decode(message_bytes)
        except Exception as err:
            # Si no cumple con el formato de base64, no lo codifica y pone el mensaje original
            return message_bytes


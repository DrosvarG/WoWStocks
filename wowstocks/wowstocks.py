import getpass
import httpx

from . import configuration

class ClientCred:
    def __init__(self, id:str = "", secret:str = ""):
        self.client_id = id
        self.client_secret = secret
    
    def __eq__(self, other):
        if not isinstance(other, ClientCred):
            return NotImplemented
        return self.client_id == other.client_id and self.client_secret == other.client_secret
    
class WoWStocks:
    def __init__(self):
        self._config = configuration.Configuration('wowstocks/config.ini')
        self.ResetCredentials()
        self._http_client = httpx.Client()

        return
    
    def ResetCredentials(self):
        self._cred = ClientCred(input("Enter client ID: "), getpass.getpass("Enter client Secret: "))
        return

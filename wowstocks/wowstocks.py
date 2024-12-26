import getpass
import httpx

from . import configuration

class WoWStocks:
    def __init__(self):
        self._config = configuration.Configuration('wowstocks/config.ini')
        self.ResetCredentials()
        self._http_client = httpx.Client()

        return
    
    def ResetCredentials(self):
        self._cred = ClientCred(input("Enter client ID: "), getpass.getpass("Enter client Secret: "))
        return

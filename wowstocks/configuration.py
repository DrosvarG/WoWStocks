import configparser

class Configuration:
    class ClientCred:
        def __init__(self, id:str = "", secret:str = ""):
            self.client_id = id
            self.client_secret = secret

    def __init__(self, path:str):
        parser = configparser.ConfigParser()
        parser.read(path)

        self.client_credentials = self.ClientCred(parser['Blizzard API']['client_id'], parser['Blizzard API']['client_secret'])
        self.auction_db_path = parser['databases']['auctions']
        return

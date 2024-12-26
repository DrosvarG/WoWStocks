import configparser

class Configuration:
    def __init__(self, path:str):
        parser = configparser.ConfigParser()
        parser.read(path)

        self.auction_db_path = parser['databases']['auctions']
        return

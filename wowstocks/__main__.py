from . import wowstocks 
from . import configuration
import sqlite3

def main():
    config = configuration.Configuration('wowstocks/config.ini')
    app = wowstocks.WoWStocks(config)
    app.Run()

# DataFetcher.DataFetcher(get_credentials('config.ini'), db_connect('databases/auctions.db'))

main()
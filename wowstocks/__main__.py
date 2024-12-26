from . import wowstocks

import sqlite3

def show_help(args:list[str]):
    if len(args) == 0:
        print("Type \"help \'command\'\" for more information. List of commands:")
        print("help - Show this help message")
        print("credentials - Reset credentials")
        print("exit - Terminate the program")
        print("servers - Print a list of all WoW servers")

        return
    
    match args[0]:
        case "exit":
            print("Terminate the program. Syntax: exit")
        case "help":
            print("Get help about a command. Syntax: help \'command\'")
        case "credentials":
            print("Reset your credentials. Syntax: credentials (client_id client_secret)")
        case "servers":
            print("List Blizzard servers. Syntax: servers")

def main():
    app = wowstocks.WoWStocks()

    while True:
        user_command = input("WoWStocks> ").split()
        
        match user_command[0]:
            case "exit":
                return
            case "help":
                show_help(user_command[1:])
            case "credentials":
                app.ResetCredentials()
            case _:
                print("Unknown command.")

    return

# DataFetcher.DataFetcher(get_credentials('config.ini'), db_connect('databases/auctions.db'))

main()
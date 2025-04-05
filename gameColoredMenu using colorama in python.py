from colorama import Fore, Back, Style, init

init()


def showMenu(): 
    print(Fore.BLUE + "==== MENU ====")
    print(Fore.YELLOW + "1. Start Game ")
    print(Fore.GREEN + "2. View Score")
    print(Fore.RED + "3. Exit the game")
    
    
    
showMenu()
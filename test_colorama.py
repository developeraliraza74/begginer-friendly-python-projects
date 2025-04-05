from colorama import Fore, Back, Style, init

init()

# available colors : red, green, blue, yellow, magenta, cyan, white, black ===> there are total 8 colors available in coloramba
# Available colors FOR BACK IS ALSO 8
# THERE ARE total three text styles available 1. NORMAL 2. BRIGHT 3. DIM
# to reset it there are RESET command used with . operator like Fore.RESET Back.RESET Style.RESET_ALL


print(Fore.RED + "This is Red")
print(Fore.GREEN + "This is Green")
print(Fore.BLUE + "This is Blue")
print(Fore.YELLOW + "This is Yellow")
print(Fore.MAGENTA + "This is Magenta")
print(Fore.CYAN + "This is Cyan")
print(Fore.WHITE + "This is White")
print(Fore.BLACK + "This is Black")


print(Fore.RED + "The red text is here ")
print(Fore.GREEN + "Green Text is here")
print(Fore.YELLOW + "Yellow text is here")
print(Fore.CYAN + "CYAN text is here")


# print(Back.RED + "Red Background" + Style.RESET_ALL)
# print(Back.GREEN + "Green Background" + Style.RESET_ALL)
# print(Back.BLUE + "Blue Background" + Style.RESET_ALL)


print(Back.RED + "RED BACKGROUND" + Style.RESET_ALL)
print(Back.GREEN + "Green Background" + Style.RESET_ALL)
print(Back.YELLOW + "Yellow background " + Style.RESET_ALL)
print(Back.CYAN + "CYAN background" + Style.RESET_ALL)


print(Style.BRIGHT + "BRIGHT TEXT" + Style.RESET_ALL)
print(Style.DIM + "Dim text" + Style.RESET_ALL)
print(Style.RESET_ALL +  "Back to normal Meri Jaan")


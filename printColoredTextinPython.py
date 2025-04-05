from colorama import init, Fore, Back, Style

# Initialize colorama
init()

# Print text in different colors
print(Fore.RED + "This text is red!")
print(Fore.GREEN + "This text is green!")
print(Fore.BLUE + "This text is blue!")
print(Fore.YELLOW + "This text is yellow!")
print(Fore.MAGENTA + "This text is magenta!")
print(Fore.CYAN + "This text is cyan!")

# Print text with colored background
print(Back.WHITE + Fore.BLACK + "This text has white background and black text!")

# Print text with different styles
print(Style.BRIGHT + "This text is bright!")
print(Style.DIM + "This text is dim!")

# Reset all styles
print(Style.RESET_ALL + "This text is back to normal!")

# Example of combining colors and styles
print(Fore.RED + Style.BRIGHT + "This is bright red text!")
print(Back.GREEN + Fore.WHITE + "This is white text on green background!")

# Example of multiple colors in one line
print(Fore.RED + "Red " + Fore.GREEN + "Green " + Fore.BLUE + "Blue") 
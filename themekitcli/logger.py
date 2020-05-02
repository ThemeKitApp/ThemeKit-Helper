from colorama import Fore, Style

def printc(*strings, color=None, style=None):
    string = ' '.join(strings)
    if color:
        if Fore.__getattribute__(color.upper()) is not None:
            string = Fore.__getattribute__(color.upper()) + string
    if style:
        if Style.__getattribute__(style.upper()) is not None:
            string = Style.__getattribute__(style.upper()) + string
    if color or style:
        string = string + Fore.RESET + Style.RESET_ALL
    print(string)
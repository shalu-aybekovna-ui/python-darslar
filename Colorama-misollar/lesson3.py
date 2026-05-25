from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.YELLOW + "Bu matn")
print(Fore.YELLOW + Style.DIM + "Bu matn")
print(Fore.YELLOW + Style.NORMAL + "Bu matn")
print(Fore.YELLOW + Style.BRIGHT + "Bu matn")

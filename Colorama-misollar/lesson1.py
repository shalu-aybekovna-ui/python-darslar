from colorama import init
from colorama import Fore, Back, Style

init() # Windows да ранглар тўгри чикиши учун инициализация килиш шарт

print(Fore.GREEN + "Bu yashil matn")
print(Back.YELLOW + Fore.WHITE + "Bu sariq fondagi oq matn")
print(Style.RESET_ALL + "Bu esa oddiy matn")

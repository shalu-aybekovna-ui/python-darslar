from colorama import Fore, Back, Style, init
import math
init()
# log(a,10) ni hisoblash dasturi
a = int(input("A="))
b = math.log(a, 10)
print(Fore.YELLOW + Back.GREEN + Style.BRIGHT + "LOG(" + str(a) + ",10)=" + str(f"{b:.2f}"))
# print(Style.RESET_ALL, f"{type(b)}")
print(Style.RESET_ALL, type(b))
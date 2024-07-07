#!/usr/bin/python3
import re # regular expression
import pyfiglet # figlet for banner
from colorama import Fore, Style # colores

# defining colores
red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
reset = Style.RESET_ALL

# defining format as short
format = pyfiglet.figlet_format

# banner
def banner():
    print(green+format("PcC")+reset)

# password checker method
def passwordChecker(password):
    points = 0
    if len(password) < 8:
        print(red+"\t * Password should be 8 chararchters long"+reset)
    else:
        points+=1
        
    if re.search(r"[0-9]", password) is None:
        print(red+"\t * You should at least have a Number"+reset)
    else:
        points+=1
        
    if re.search(r"[A-Z]", password) is None:
        print(red+"\t * Add some capital letter in your password"+reset)
    else:
        points+=1
    
    if re.search(r"[^a-zA-Z0-9]", password) is None:
        print(red+"\t * Add special charachters in your password"+reset)
    else:
        points+=1
    
    if points <= 1:
        print(red+"\tVery weak password"+reset)
    elif points <= 2:
        print(blue+"\tWeak password"+reset)
    elif points <= 3:
        print(cyan+"\tMedium password"+reset)
    elif points <= 4:
        print(green+"\tPassword Okay"+reset)

# main method 
def main():
    banner()
    password = input("Enter your Passowrd : ")
    print("\n Suggestions : ")
    passwordChecker(password)


if __name__ == main():main()
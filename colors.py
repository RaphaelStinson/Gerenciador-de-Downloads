import pyfiglet
from colored import fg, bg, attr
from colorama import init, Fore, Back, Style

def initialize_colors():
    init(autoreset=True)

def print_header():
    color = bg('blue') + fg('black')
    reset = attr('reset')
    print("\n" + color + f"{pyfiglet.figlet_format(' GD ', font='standard')}" + reset)
    print("                                                🐈‍⬛")
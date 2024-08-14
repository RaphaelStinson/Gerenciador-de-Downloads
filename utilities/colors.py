# src/colors.py
import pyfiglet
from colored import fg, bg, attr
from colorama import init

def print_welcome_message():
    init(autoreset=True)
    color = bg('blue') + fg('black')
    reset = attr('reset')
    print("\n" + color + f"{pyfiglet.figlet_format(' GD ', font='standard')}" + reset)
    print("                                                🐈‍⬛")
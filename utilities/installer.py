# src/installer.py
import os

def install_dependencies():
    os.system("pip install colored colorama pyfiglet watchdog")

if __name__ == '__main__':
    install_dependencies()
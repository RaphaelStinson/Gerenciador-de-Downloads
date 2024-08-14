import os

def install_missing_packages():
    packages = ['colored', 'colorama', 'pyfiglet']
    for package in packages:
        try:
            __import__(package)
        except ModuleNotFoundError:
            os.system(f"pip install {package}")
            __import__(package)
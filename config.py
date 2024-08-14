import os
import shutil
from watchdog.events import FileSystemEventHandler

class MeuHandler(FileSystemEventHandler):
    def __init__(self, pasta_origem1, pasta_origem2, pasta_origem3, pasta_origem4, pasta_destino, mapeamento_pastas):
        self.pasta_origem1 = pasta_origem1
        self.pasta_origem2 = pasta_origem2
        self.pasta_origem3 = pasta_origem3
        self.pasta_origem4 = pasta_origem4
        self.pasta_destino = pasta_destino
        self.mapeamento_pastas = mapeamento_pastas

    def on_modified(self, event):
        self.process_files(self.pasta_origem1)
        self.process_files(self.pasta_origem2)
        self.process_files(self.pasta_origem3)
        self.process_files(self.pasta_origem4)

    def process_files(self, pasta_origem):
        for filename in os.listdir(pasta_origem):
            src = os.path.join(pasta_origem, filename)
            if os.path.isfile(src):
                extensao = os.path.splitext(filename)[1]
                if extensao in self.mapeamento_pastas:
                    pasta_destino_tipo = self.mapeamento_pastas[extensao]
                    pasta_destino_completa = os.path.join(self.pasta_destino, pasta_destino_tipo)
                    if not os.path.exists(pasta_destino_completa):
                        os.makedirs(pasta_destino_completa)
                    dst = os.path.join(pasta_destino_completa, filename)
                    shutil.move(src, dst)
                    print(f"Arquivo {filename} movido para {pasta_destino_completa}")import os

def install_missing_packages():
    packages = ['colored', 'colorama', 'pyfiglet']
    for package in packages:
        try:
            __import__(package)
        except ModuleNotFoundError:
            os.system(f"pip install {package}")import pyfiglet
from colored import fg, bg, attr
from colorama import init

def setup_colors():
    init(autoreset=True)
    
def display_header():
    color = bg('blue') + fg('black')
    reset = attr('reset')
    header = pyfiglet.figlet_format(" GD ", font="standard")
    print("\n" + color + header + reset)
    print("""                                                🐈‍⬛""")# Configurações das pastas
PASTA_ORIGEM1 = '/storage/emulated/0/Download'
PASTA_ORIGEM2 = '/storage/emulated/0/Download/Seal'
PASTA_ORIGEM3 = '/storage/emulated/0/Movies/Downloader_for_TikTok'
PASTA_ORIGEM4 = '/storage/emulated/0/Download/Nekogram'
PASTA_DESTINO = '/storage/emulated/0/Download'from config import PASTA_ORIGEM1, PASTA_ORIGEM2, PASTA_ORIGEM3, PASTA_ORIGEM4, PASTA_DESTINO

def obter_mapeamento_pastas():
    return {
        '.txt': 'textos',
        '.jpg': 'imagens',
        '.pdf': 'documentos',
        '.mp4': 'videos',
        '.zip': 'arquivos para descompactar',
        '.rar': 'arquivos para descompactar',
        '.exe': 'arquivos executaveis',
        '.msi': 'arquivos executaveis',
        '.apk': 'arquivos executaveis'
    }
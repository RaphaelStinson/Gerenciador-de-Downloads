import os
try:
    import colored
except ModuleNotFoundError:
    os.system("pip install colored")
    import colored
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
os.system("clear")
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from colored import fg, bg, attr
from colorama import init, Fore, Back, Style
from arquvos_observados import obter_mapeamento_pastas

color = bg('blue') + fg('black')

init(autoreset=True)

reset = attr('reset')

print("\n" + color+(f"""{pyfiglet.figlet_format(" GD ", font="standard")}""")+reset)

print("""                                                🐈‍⬛""")

# Pasta de origem
pasta_origem1 = '/storage/emulated/0/Download'
pasta_origem2 = '/storage/emulated/0/Download/Seal'
pasta_origem3 = '/storage/emulated/0/Movies/Downloader_for_TikTok'

# Pasta de destino
pasta_destino = '/storage/emulated/0/Download'

# Mapeamento de extensões para pastas de destino
mapeamento_pastas = obter_mapeamento_pastas()

class MeuHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(pasta_origem1):
            src = os.path.join(pasta_origem1, filename)
            if os.path.isfile(src):
                extensao = os.path.splitext(filename)[1]
                if extensao in mapeamento_pastas:
                    pasta_destino_tipo = mapeamento_pastas[extensao]
                    pasta_destino_completa = os.path.join(pasta_destino, pasta_destino_tipo)
                    if not os.path.exists(pasta_destino_completa):
                        os.makedirs(pasta_destino_completa)
                    dst = os.path.join(pasta_destino_completa, filename)
                    shutil.move(src, dst)
                    print(f"Arquivo {filename} movido para {pasta_destino_completa}")

        for filename in os.listdir(pasta_origem2):
            src = os.path.join(pasta_origem2, filename)
            if os.path.isfile(src):
                extensao = os.path.splitext(filename)[1]
                if extensao in mapeamento_pastas:
                    pasta_destino_tipo = mapeamento_pastas[extensao]
                    pasta_destino_completa = os.path.join(pasta_destino, pasta_destino_tipo)
                    if not os.path.exists(pasta_destino_completa):
                        os.makedirs(pasta_destino_completa)
                    dst = os.path.join(pasta_destino_completa, filename)
                    shutil.move(src, dst)
                    print(f"Arquivo {filename} movido para {pasta_destino_completa}")

        for filename in os.listdir(pasta_origem3):
            src = os.path.join(pasta_origem3, filename)
            if os.path.isfile(src):
                extensao = os.path.splitext(filename)[1]
                if extensao in mapeamento_pastas:
                    pasta_destino_tipo = mapeamento_pastas[extensao]
                    pasta_destino_completa = os.path.join(pasta_destino, pasta_destino_tipo)
                    if not os.path.exists(pasta_destino_completa):
                        os.makedirs(pasta_destino_completa)
                    dst = os.path.join(pasta_destino_completa, filename)
                    shutil.move(src, dst)
                    print(f"Arquivo {filename} movido para {pasta_destino_completa}")

# Cria o observador
event_handler = MeuHandler()
observer = Observer()
observer.schedule(event_handler, pasta_origem1, recursive=True)
observer.schedule(event_handler, pasta_origem2, recursive=True)
observer.schedule(event_handler, pasta_origem3, recursive=True)

# Inicia o observador
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

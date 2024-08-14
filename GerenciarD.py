# main.py
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utilities.config import pasta_origem1, pasta_origem2, pasta_origem3, pasta_origem4, pasta_destino
from utilities.arquivos_observados import obter_mapeamento_pastas
from utilities.colors import print_welcome_message
from utilities.file_handler import MeuHandler
os.system("clear")

def main():
    print_welcome_message()
    
    mapeamento_pastas = obter_mapeamento_pastas()
    event_handler = MeuHandler(mapeamento_pastas)
    observer = Observer()
    for pasta_origem in [pasta_origem1, pasta_origem2, pasta_origem3, pasta_origem4]:
        observer.schedule(event_handler, pasta_origem, recursive=True)
    
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

if __name__ == '__main__':
    main()
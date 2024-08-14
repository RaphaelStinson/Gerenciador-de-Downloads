import os
import time
from watchdog.observers import Observer
from config import pasta_origem1, pasta_origem2, pasta_origem3, pasta_destino, obter_mapeamento_pastas
from file_handler import MeuHandler
os.system("clear")

# Inicializar o colorama e outras configurações
from colors import initialize_colors, print_header

initialize_colors()
print_header()

# Obter o mapeamento de pastas
mapeamento_pastas = obter_mapeamento_pastas()

# Criar o handler de eventos
event_handler = MeuHandler(pasta_destino, mapeamento_pastas)
observer = Observer()
observer.schedule(event_handler, pasta_origem1, recursive=True)
observer.schedule(event_handler, pasta_origem2, recursive=True)
observer.schedule(event_handler, pasta_origem3, recursive=True)

# Iniciar o observador
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
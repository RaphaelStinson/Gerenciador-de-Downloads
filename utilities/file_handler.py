# utilities/file_handler.py

import os
import shutil
from watchdog.events import FileSystemEventHandler
from utilities.config import pasta_destino

class MeuHandler(FileSystemEventHandler):
    def __init__(self, mapeamento_pastas):
        self.mapeamento_pastas = mapeamento_pastas

    def on_modified(self, event):
        if event.is_directory:
            return

        src = event.src_path
        filename = os.path.basename(src)
        extensao = os.path.splitext(filename)[1]
        if extensao in self.mapeamento_pastas:
            pasta_destino_tipo = self.mapeamento_pastas[extensao]
            pasta_destino_completa = os.path.join(pasta_destino, pasta_destino_tipo)

            # Cria a pasta de destino se não existir
            if not os.path.exists(pasta_destino_completa):
                os.makedirs(pasta_destino_completa)

            dst = os.path.join(pasta_destino_completa, filename)
            shutil.move(src, dst)
            print(f"Arquivo {filename} movido para {pasta_destino_completa}")
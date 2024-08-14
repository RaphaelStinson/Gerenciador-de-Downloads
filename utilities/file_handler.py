# src/file_handler.py
import os
import shutil
from watchdog.events import FileSystemEventHandler
from .config import pasta_origem1, pasta_origem2, pasta_origem3, pasta_origem4, pasta_destino

class MeuHandler(FileSystemEventHandler):
    def __init__(self, mapeamento_pastas):
        self.mapeamento_pastas = mapeamento_pastas

    def on_modified(self, event):
        for pasta_origem in [pasta_origem1, pasta_origem2, pasta_origem3, pasta_origem4]:
            for filename in os.listdir(pasta_origem):
                src = os.path.join(pasta_origem, filename)
                if os.path.isfile(src):
                    extensao = os.path.splitext(filename)[1]
                    if extensao in self.mapeamento_pastas:
                        pasta_destino_tipo = self.mapeamento_pastas[extensao]
                        pasta_destino_completa = os.path.join(pasta_destino, pasta_destino_tipo)
                        if not os.path.exists(pasta_destino_completa):
                            os.makedirs(pasta_destino_completa)
                        dst = os.path.join(pasta_destino_completa, filename)
                        shutil.move(src, dst)
                        print(f"Arquivo {filename} movido para {pasta_destino_completa}")
# GerenciadorD.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utilities.config import carregar_pastas_observadas, salvar_pastas_observadas, pasta_destino
from utilities.arquivos_observados import obter_mapeamento_pastas
from utilities.colors import print_welcome_message
from utilities.file_handler import MeuHandler
os.system("clear")

class GerenciadorD:
    def __init__(self):
        self.pastas_observadas = carregar_pastas_observadas()
        self.mapeamento_pastas = obter_mapeamento_pastas()
        self.event_handler = MeuHandler(self.mapeamento_pastas)
        self.observer = Observer()
        self._configurar_observador()

    def _configurar_observador(self):
        for pasta_origem in self.pastas_observadas:
            if not os.path.exists(pasta_origem):
                os.makedirs(pasta_origem)
            self.observer.schedule(self.event_handler, pasta_origem, recursive=True)
    
    def adicionar_pasta(self, nova_pasta):
        if nova_pasta not in self.pastas_observadas:
            self.pastas_observadas.append(nova_pasta)
            self._configurar_observador()  # Reconfigura o observador
            salvar_pastas_observadas(self.pastas_observadas)
            print(f"Pasta {nova_pasta} adicionada para observação.")

    def iniciar(self):
        print_welcome_message()
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

def executar_gerenciador():
    gerenciador = GerenciadorD()
    gerenciador.iniciar()

if __name__ == "__main__":
    executar_gerenciador()
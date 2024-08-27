# Menu.py

import os
import sys
from utilities.config import criar_pasta
from GerenciadorD import GerenciadorD, executar_gerenciador

def menu_adicionar_pastas(gerenciador):
    while True:
        print("\nMenu:")
        print("1. Adicionar nova pasta")
        print("2. Conectar e executar GerenciadorD")
        print("3. Sair")

        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

        if opcao == '1':
            nova_pasta = input("Digite o caminho da nova pasta: ").strip()
            criar_pasta(nova_pasta)
            if gerenciador:
                gerenciador.adicionar_pasta(nova_pasta)
        elif opcao == '2':
            # Adiciona o diretório atual ao caminho de importação
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            executar_gerenciador()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicializa o script
if __name__ == "__main__":
    # Cria as pastas iniciais
    from utilities.config import criar_pasta, pastas_iniciais
    for pasta in pastas_iniciais:
        criar_pasta(pasta)
    
    # Cria uma instância do gerenciador (inicialmente com pastas carregadas da configuração)
    gerenciador = GerenciadorD()
    
    # Exibe o menu para adicionar novas pastas e outras opções
    menu_adicionar_pastas(gerenciador)
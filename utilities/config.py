import os

# Configuração das pastas
pasta_origem1 = '/storage/emulated/0/Download'
pasta_origem2 = '/storage/emulated/0/Download/Seal'
pasta_origem3 = '/storage/emulated/0/Movies/Downloader_for_TikTok'
pasta_origem4 = '/storage/emulated/0/Download/Nekogram'
pasta_destino = '/storage/emulated/0/Download'

# Lista de todas as pastas para criação
pastas = [pasta_origem1, pasta_origem2, pasta_origem3, pasta_origem4, pasta_destino]

# Cria as pastas se não existirem
for pasta in pastas:
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        print(f'Pasta criada: {pasta}')
    else:
        print(f'Pasta já existe: {pasta}')
# utilities/arquivos_observados.py
def obter_mapeamento_pastas():
    return {
        '.txt': 'textos',
        '.jpg': 'imagens',
        '.jpeg': 'imagens',
        '.gif': 'imagens',
        '.raw': 'imagsns',
        '.png': 'imagens',
        '.pdf': 'pdf',
        '.epub': 'pdf',
        '.mp4': 'videos',
        '.mov': 'videos',
        '.avi': 'videos',
        '.flv': 'videos',
        '.doc': 'documentos',
        '.docx': 'documentos',
        '.mp3': 'audios',
        '.zip': 'arquivos para descompactar',
        '.rar': 'arquivos para descompactar',
        '.exe': 'arquivos executaveis',
        '.msi': 'arquivos executaveis',
        '.apk': 'arquivos executaveis'
    }
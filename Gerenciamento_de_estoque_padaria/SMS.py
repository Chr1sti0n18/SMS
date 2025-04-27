import sys
from pathlib import Path

# Adiciona o caminho da pasta teste/src/app ao sistema
caminho_app = Path(__file__).parent / "src" / "app"
sys.path.append(str(caminho_app))

# Importa o arquivo e usa a função
from login import Login

# Executa a função
Login()
from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Autenticar
api = KaggleApi()
api.authenticate()

# Nome correto do dataset
dataset_name = "faizalkarim/flood-area-segmentation"

# Fazer download e descompactar automaticamente
api.dataset_download_files(
    dataset_name,
    path="avanti-ML-course",
    unzip=True,  # Remove o ZIP após extrair
    force=False  # Não sobrescreve arquivos existentes
)

# Listar arquivos baixados (verificação)
print("Arquivos no diretório:")
print(os.listdir("avanti-ML-course"))
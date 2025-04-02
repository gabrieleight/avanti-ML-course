import os
import hashlib
from PIL import Image

def verify_images(directory, generate_hashes=False):
    corrupted_files = []
    valid_hashes = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                    if generate_hashes:
                        file_hash = hashlib.sha256(content).hexdigest()
                        valid_hashes[file] = file_hash
            except IOError:
                corrupted_files.append(file_path)
                continue
            
            try:
                with Image.open(file_path) as img:
                    img.verify()
                with Image.open(file_path) as img:
                    img.load()
                    img.transpose(Image.FLIP_LEFT_RIGHT)
            except (IOError, OSError, Image.DecompressionBombError) as e:
                corrupted_files.append(file_path)
                print(f"Arquivo corrompido: {file_path} - Erro: {str(e)}")
            
        return {
            'total_files': len(files),
            'corrupted_files': corrupted_files,
            'valid_hashes': valid_hashes if generate_hashes else None
        }

if __name__ == "__main__":
    diretorio_image = "/home/gabriel/Desktop/Gabriel/Codes/avanti-ML-course/Image"
    diretorio_mask = "/home/gabriel/Desktop/Gabriel/Codes/avanti-ML-course/Mask"
 
    print(f"Verificando existência dos diretórios:")
    print(f"Diretório de imagens existe: {"Sim" if os.path.exists(diretorio_image) else "Não"}")
    print(f"Diretório de máscaras existe: {"Sim" if os.path.exists(diretorio_mask) else "Não"}")
    
    report_image = verify_images(diretorio_image, generate_hashes=True)
    report_mask = verify_images(diretorio_mask, generate_hashes=True)
    
    print()
    print("Relatório de Integridade:")
    print(f"Arquivos de imagem: {report_image['total_files']} verificados")
    print(f"Arquivos de máscara: {report_mask['total_files']} verificados")
    print(f"Total geral: {report_image['total_files'] + report_mask['total_files']} arquivos\n")
    
 # Integridade pasta Image   
    if report_image['corrupted_files']:
        print("Lista de arquivos corrompidos:")
        for corrupted in report_image['corrupted_files']:
            print(f" - {corrupted}")
        print()
    else:
        print("Não foram encontrados arquivos da pasta Image corrompidos!\n")
   
    if report_image['valid_hashes']:
        print(f"Hashes válidos gerados para {len(report_image['valid_hashes'])} arquivos da pasta Image\n")
            
# Integridade pasta Mask
    if report_mask['corrupted_files']:
        print("Lista de arquivos corrompidos:")
        for corrupted in report_mask['corrupted_files']:
            print(f" - {corrupted}")
        print()
    else:
        print("Não foram encontrados arquivos da pasta Mask corrompidos!\n")
    
    if report_mask['valid_hashes']:
        print(f"Hashes válidos gerados para {len(report_mask['valid_hashes'])} arquivos da pasta Mask\n")
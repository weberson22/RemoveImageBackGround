import os
from rembg import remove
from PIL import Image

input_folder = 'image'
output_folder = 'image/output'

# Verifica se a pasta de saída existe, senão cria
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lista todos os arquivos da pasta de entrada
input_files = os.listdir(input_folder)

# Variável para contar as imagens processadas com sucesso
imagens_processadas = 0

for filename in input_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

    # Verifica se o arquivo é uma imagem (extensões suportadas podem variar)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        imagens_processadas += 1

print(f"Processamento concluído! {imagens_processadas} imagens foram processadas com sucesso.")

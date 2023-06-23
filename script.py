"""Script que encontra valor especifico dentro de uma pasta com varios PDFs"""
import os
from PyPDF2 import PdfReader


def procurar_texto_em_pdf(caminho_pasta, texto_procurado):
    """
    Procura por um texto específico dentro de todos os arquivos PDF em uma pasta.

    Parâmetros:
        caminho_pasta (str): O caminho completo para a pasta contendo os arquivos PDF.
        texto_procurado (str): O texto que está sendo procurado nos arquivos PDF.

    Retorna:
        Uma lista com os nomes dos arquivos que contêm o texto especificado.
    """

    arquivos_encontrados = []

    # Listar todos os arquivos na pasta
    arquivos_pdf = [
        arquivo
        for arquivo in os.listdir(caminho_pasta)
        if arquivo.lower().endswith(".pdf")
    ]

    # Iterar sobre os arquivos PDF
    for arquivo_pdf in arquivos_pdf:
        caminho_pdf = os.path.join(caminho_pasta, arquivo_pdf)

        # Abrir o arquivo PDF
        with open(caminho_pdf, "rb") as arquivo:
            pdf = PdfReader(arquivo)

            # Iterar sobre as páginas do PDF
            for pagina in pdf.pages:
                texto = pagina.extract_text()

                # Verificar se o texto procurado está presente na página
                if texto_procurado in texto:
                    arquivos_encontrados.append(arquivo_pdf)
                    break

    return arquivos_encontrados


# Caminho para a pasta contendo os arquivos PDF
CAMINHO_DA_PASTA = os.path.join(os.getcwd(), "data")

# Texto a ser procurado nos arquivos PDF
TEXTO_PROCURADO = "Texto que deseja procurar"

# Chamar a função para procurar o texto nos arquivos PDF
ARQUIVOS_ENCONTRADOS = procurar_texto_em_pdf(CAMINHO_DA_PASTA, TEXTO_PROCURADO)

# Exibir os nomes dos arquivos encontrados
if len(ARQUIVOS_ENCONTRADOS) > 0:
    print("Arquivos encontrados:")
    for ARQUIVO in ARQUIVOS_ENCONTRADOS:
        print(ARQUIVO)
else:
    print("Nenhum arquivo encontrado.")

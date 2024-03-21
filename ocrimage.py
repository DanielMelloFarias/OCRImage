import pandas as pd
import google.generativeai as genai


from dotenv import load_dotenv
import os

import PIL

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

genai.configure(api_key = os.environ.get('KeyMaster'))

#img = PIL.Image.open("receita_medica2.png")


# Base do nome do arquivo
nome_base = "imagens/TERMOS DE ADESÃO PEDRO REIS-"

# Loop para ler cada um dos 5 arquivos
for i in range(1, 2):  # O range vai de 1 a 5, incluindo o 5
    # Monta o nome do arquivo
    nome_arquivo = f"{nome_base}{i:03d}.jpg"
    print(f"Lendo arquivo: {nome_arquivo}...")
    # Abre a imagem
    imagem = PIL.Image.open(nome_arquivo)

    # Roda os Modelos 
    modelText = genai.GenerativeModel('gemini-pro')
    modelVision = genai.GenerativeModel('gemini-pro-vision')

    # Mostra as respostas
    responseImage = modelVision.generate_content(['Extraia Informações: - Nome, - CPF, - Unidade Escolar, - Ano/Série, - Turma, - Nome do Responsável e CPF, - Cidade e Data da ASsinatura e qual box foi marcada', imagem])
    #responseImage = modelVision.generate_content(['Extraia Informações relevantes', img])
    response = modelText.generate_content(['Ajuste o texto e me mostre de forma organizada', responseImage.text])
    print (responseImage.text)
    print ("#################")
    print(response.text)
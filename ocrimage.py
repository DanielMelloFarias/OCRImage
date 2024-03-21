import pandas as pd
import google.generativeai as genai


import os

import PIL

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

genai.configure(api_key = os.environ.get('KeyMaster'))

#img = PIL.Image.open("receita_medica2.png")



file = st.file_uploader("Pick a file")
# Abre a imagem
imagem = PIL.Image.open(file)

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
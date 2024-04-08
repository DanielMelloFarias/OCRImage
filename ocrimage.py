import pandas as pd
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
import json

import PIL

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

genai.configure(api_key = os.environ.get('KeyMaster'))

#img = PIL.Image.open("receita_medica2.png")



file = st.file_uploader("Escolha uma imagem...", type=['jpg', 'jpeg', 'png'])

# Verifica se um arquivo foi enviado
if file is not None:
    # Mostra a imagem enviada
    st.image(file, caption='Imagem Enviada', use_column_width=True)

    # Abre a imagem
    imagem = PIL.Image.open(file)

    # Roda os Modelos 
    modelText = genai.GenerativeModel('gemini-pro')
    modelVision = genai.GenerativeModel('gemini-pro-vision')

    json_saida = {
    "nome": "Gabriel Eclisson Ferreira da Silva",
    "cpf": "151.331.347-60",
    "unidade_escolar": "Escola Estadual Prof. Pedro de França Reis",
    "ano_serie": "1º ano",
    "turma": "01",
    "nome_responsavel": "Ana Cleide da Silva Pereira",
    "cpf_responsavel": "014.692.614-93",
    "cidade": "Arapiraca",
    "data_assinatura": "21 de fevereiro de 2024",
    "box_marcada": "Autorizando o transporte do leite até a minha residência semanalmente"
    }

    # Mostra as respostas
    responseImage = modelVision.generate_content(['Extraia Informações: - Nome, - CPF, - Unidade Escolar, - Ano/Série, - Turma, - Nome do Responsável e CPF, - Cidade e Data da ASsinatura e qual box foi marcada. E ponha em um JSON como o padrão. nome: Gabriel Eclisson Ferreira da Silva,"cpf": "151.331.347-60", "unidade_escolar": "Escola Estadual Prof. Pedro de França Reis", "unidade_escolar": "Escola Estadual Prof. Pedro de França Reis", "ano_serie": "1º ano", "turma": "01", "nome_responsavel": "Ana Cleide da Silva Pereira", "cpf_responsavel": "014.692.614-93","cidade": "Arapiraca", "data_assinatura": "21 de fevereiro de 2024", "box_marcada": "Autorizando o transporte do leite até a minha residência semanalmente"',imagem])
    #responseImage = modelVision.generate_content(['Extraia Informações relevantes', img])
    response = modelText.generate_content(['Ajuste o texto e me mostre de forma organizada em formato JSON. MATENHA APENAS O JSON convertido. Pegue o json de ex: nome: Gabriel Eclisson Ferreira da Silva,"cpf": "151.331.347-60", "unidade_escolar": "Escola Estadual Prof. Pedro de França Reis", "unidade_escolar": "Escola Estadual Prof. Pedro de França Reis", "ano_serie": "1º ano", "turma": "01", "nome_responsavel": "Ana Cleide da Silva Pereira", "cpf_responsavel": "014.692.614-93","cidade": "Arapiraca", "data_assinatura": "21 de fevereiro de 2024", "box_marcada": "Autorizando o transporte do leite até a minha residência semanalmente"', responseImage.text])

    print (responseImage.text)
    print ("#################")
    print(response.text)

    # Converte a string JSON em um dicionário
    dados_extraidos = json.loads(response)

    # Adapta o dicionário para o formato esperado pela DataFrame (especialmente para valores booleanos)
    dados_adaptados = {
    "Nome Completo": dados_extraidos["nome"],
    "CPF": dados_extraidos["cpf"],
    "Unidade Escolar": dados_extraidos["unidade_escolar"],
    "Ano/Série": dados_extraidos["ano_serie"],
    "Turma": dados_extraidos["turma"],
    "Nome do Responsável": dados_extraidos["nome_responsavel"],
    "CPF do Responsável": dados_extraidos["cpf_responsavel"],
    "Cidade": dados_extraidos["cidade"],
    "Data da Assinatura": dados_extraidos["data_assinatura"],
    "Box Marcada": dados_extraidos["marcacao"]
    }

    # Converte os dados adaptados para um DataFrame para exibição
    df = pd.DataFrame([dados_adaptados])

    # Exibe o DataFrame como uma tabela na aplicação Streamlit
    st.table(df)


import streamlit as st
import pandas as pd
import requests
import io
import downloadf3
import downloadf6

st.title('Download Bases de Dados Formulário Kobo')

# Lendo dados do Formulário 3
dadosf3 = downloadf3.download_form3()

if st.button('Formulário 3 - Cadastro Anual das Unidades Familiares de Produção'):
    # Convertendo o DataFrame para bytes (formato binário)
    dados_binarios = io.BytesIO()
    dadosf3.to_excel(dados_binarios, index=False, engine='xlsxwriter')
    dados_binarios.seek(0)

    # Botão de download
    st.download_button(label='Clique para Baixar',
                       data=dados_binarios,
                       file_name='Formulário 3 - Cadastro Anual das Unidades Familiares de Produção.xlsx',
                       key='download_button')
    

# Lendo dados do Formulário 6
dadosf6 = downloadf6.download_form6()

if st.button('Formulário 06 - Projetos de Crédito efetivados por Agência e Produtor'):
    # Convertendo o DataFrame para bytes (formato binário)
    dados_binarios = io.BytesIO()
    dadosf6.to_excel(dados_binarios, index=False, engine='xlsxwriter')
    dados_binarios.seek(0)

    # Botão de download
    st.download_button(label='Clique para Baixar',
                       data=dados_binarios,
                       file_name='Formulário 06 - Projetos de Crédito efetivados por Agência e Produtor.xlsx',
                       key='download_button')

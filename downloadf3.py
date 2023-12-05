import pandas as pd
import requests
from io import BytesIO
import os

# FORMULÁRIO 3 KOBO

# Rota para o download do arquivo

def download_form3():
    link = 'https://eu.kobotoolbox.org/api/v2/assets/aKetFYPwuhGSD43m7RtKot/export-settings/esQ8BrbzfxRJqdvJJGX5FRr/data.xlsx?format=api'

    response = requests.get(link)
    file = BytesIO(response.content)

    # lendo as tabelas
    df1 = pd.read_excel(file, sheet_name='Formulário 03 - Cadastro anu...', engine='openpyxl')
    df2 = pd.read_excel(file, sheet_name='Dados_sociais_ufp', engine='openpyxl')
    df3 = pd.read_excel(file, sheet_name='dados_de_producao', engine='openpyxl')

    # convertendo as tabelas para formato "string" para evitar erros na mesclagem dos dados
    df1 = df1.astype(str)
    df2 = df2.astype(str)
    df3 = df3.astype(str)

    # mesclando as tabelas
    df_merged1 = pd.merge(df1, df2, left_on='_index', right_on='_parent_index', how='outer')
    df_merged2 = pd.merge(df_merged1, df3, left_on='_parent_index', right_on='_parent_index', how='outer')

    # função para garantir que apenas valores distintos serão concetenados entre "," nas linhas
    def join_unique(x):
        values = set()
        result = []
        for value in x.dropna():
            if value not in values:
                result.append(value)
                values.add(value)
        return ','.join(result)

    # agrupando os dados que tem linhas a mais pelo "index" e concatenando por ","
    df_merged1 = df_merged2.groupby('_parent_index').agg(join_unique).reset_index()


    return df_merged1
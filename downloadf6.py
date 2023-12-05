import pandas as pd
import requests
from io import BytesIO
import os


def download_form6():
    link = 'https://eu.kobotoolbox.org/api/v2/assets/ah4QnXrsbDCrg7TekPzMHs/export-settings/esJr6AaHsWVbXPpgQtDpUEb/data.xlsx'

    response = requests.get(link)
    file = BytesIO(response.content)

    # lendo a tabela excel
    df1 = pd.read_excel(file, sheet_name='Formulário 06 - Projetos de ...', engine='openpyxl')
    df2 = pd.read_excel(file, sheet_name='culturas_banco_da_amazonia', engine='openpyxl')
    df3 = pd.read_excel(file, sheet_name='culturas_outros_bancos', engine='openpyxl')

    # convertendo as colunas para string
    df1 = df1.astype(str)
    df2 = df2.astype(str)
    df3 = df3.astype(str)

    # mesclando os dados
    df_merged1 = pd.merge(df1, df2, left_on='_uuid', right_on='_submission__uuid', how='left')
    df_merged2 = pd.merge(df_merged1, df3, left_on='_uuid', right_on='_submission__uuid', how='left')

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
    df_merged1 = df_merged2.groupby('_uuid').agg(join_unique).reset_index()

    # Salva o dataframe em um arquivo Excel
    output_path = os.path.abspath('Formulário 06 - Projetos de Crédito efetivados por Agência e Produtor.xlsx')
    df_merged1.to_excel(output_path, index=False)

    return df_merged1
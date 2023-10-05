#pip install pandas requests openpyxl

import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL do site
url = ''

# Fazer o download da página
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas as tabelas na página
tables = soup.find_all('table')

# Iterar sobre as tabelas e criar planilhas do Excel
for i, table in enumerate(tables):
    # Ler a tabela com pandas
    df = pd.read_html(str(table))[0]  # Pode haver várias tabelas na página, escolha a que você deseja

    # Criar uma planilha do Excel
    excel_file = f'tabela_{i + 1}.xlsx'
    df.to_excel(excel_file, index=False)

    print(f'Planilha {excel_file} criada com sucesso.')

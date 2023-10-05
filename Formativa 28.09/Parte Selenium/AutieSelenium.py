from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configurar o WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Acessar o site
navegador.get('')
navegador.implicitly_wait(3)

# Encontrar e exibir conteúdo por ID
elemento_por_id = navegador.find_element(By.ID, '').text
print("Conteúdo por ID:")
print(elemento_por_id)

# Encontrar e exibir conteúdo por TAG_NAME
elementos_por_tags = navegador.find_elements(By.TAG_NAME, 'h1')
print("\nConteúdo por TAG_NAME:")
for elemento in elementos_por_tags:
    print(elemento.text)

# Encontrar e exibir conteúdo por CLASS_NAME
elementos_por_class = navegador.find_elements(By.CLASS_NAME, '')
print("\nConteúdo por CLASS_NAME:")
for elemento in elementos_por_class:
    print(elemento.text)

# Encontrar e exibir conteúdo por NAME 
elemento_por_name = navegador.find_element(By.NAME, '')
elemento_por_name.send_keys('')
print("\nConteúdo por NAME:")
print(elemento_por_name.get_attribute('value'))

# O comando abaixo, INSPECIONA, o conteúdo de um INPUT no site do Google e escreve uma pesquisa
elemento_por_xpath = navegador.find_element(By.XPATH, 'XPATH')
elemento_por_xpath.send_keys('conteúdo que quer pesquisar')
print("\nConteúdo por XPATH:")
print(elemento_por_xpath.get_attribute('value'))

# Fechar o navegador
navegador.quit()

import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Criar contador para fazer múltiplos testes
contador = 0

# Ler arquivo json
arquivo_Json = open('jogadores.json', 'r')

# Armazenar os dados do arquivo json no dicionário dados
dados_Json = json.load(arquivo_Json)

# Lista com todos os dados de cada jogador
jogadores = dados_Json['Jogadores']

# Laço de repetição para gerar a quantidade de testes necessárias
while contador < 5:
    # Criar instância do navegador
    driver = webdriver.Chrome()

    # Abrir a página do cadastro da Liga Vale Tennis Amador
    driver.get('https://ligavaletennis.esp.br/formulario.php')

    # Maximizar o browser
    driver.maximize_window()

    # Pegar o campo nome do tenista
    campo_Nome = driver.find_element_by_name('nome')

    # Pegar o campo sobrenome do tenista
    campo_Sobrenome = driver.find_element_by_name('sobrenome')

    # Pegar o campo apelido do tenista
    campo_Apelido = driver.find_element_by_name('apelido')

    # Pegar o campo e-mail do tenista
    campo_Email = driver.find_element_by_name('email')

    # Pegar o campo telefone do tenista
    campo_Telefone = driver.find_element_by_name('phone')

    # Pegar o select categoria do tenista
    select_Categoria = Select(driver.find_element_by_name('categoria'))

    # Pegar o campo senha do tenista
    campo_Senha = driver.find_element_by_name('senha')

    # Pegar o campo confirmar senha do tenista
    campo_ConfirmarSenha = driver.find_element_by_name('confirmarSenha')

    # Digitar um nome aleatório
    campo_Nome.send_keys(jogadores[contador]["nome"])

    # Digitar um sobrenome aleatório
    campo_Sobrenome.send_keys(jogadores[contador]["sobrenome"])

    # Digitar um apelido aleatório
    campo_Apelido.send_keys(jogadores[contador]["apelido"])

    # Digitar um email aleatório
    campo_Email.send_keys(jogadores[contador]["email"])

    # Digitar um telefone aleatório
    campo_Telefone.send_keys(jogadores[contador]["telefone"])

    # Selecionar uma opção aleatória
    select_Categoria.select_by_visible_text(jogadores[contador]["categoria"])

    # Digitar uma senha aleatória
    campo_Senha.send_keys(jogadores[contador]["senha"])

    # Digitar uma confirmação de senha aleatória
    campo_ConfirmarSenha.send_keys(jogadores[contador]["confirmarSenha"])

    contador = contador + 1


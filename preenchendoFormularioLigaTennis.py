from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
campo_Nome.send_keys('Scott')

# Digitar um sobrenome aleatório
campo_Sobrenome.send_keys('Free')

# Digitar um apelido aleatório
campo_Apelido.send_keys('Sr.Milagre')

# Digitar um email aleatório
campo_Email.send_keys('scottfree@srmilagre.com')

# Digitar um telefone aleatório
campo_Telefone.send_keys('012-34985-3325')

# Selecionar a opção classe A
select_Categoria.select_by_visible_text('Classe A')

# Digitar uma senha aleatória
campo_Senha.send_keys('srmilagre')

# Digitar uma confirmação de senha aleatória
campo_ConfirmarSenha.send_keys('srmilagre')


import json

from selenium import webdriver

# Criar instância do navegador
driver = webdriver.Chrome()

# Abrir a página do Python Club
driver.get('https://www.omelete.com.br/')

# Maximizar o browser
driver.maximize_window()

# Inicializar meu dicionário
myDict = {'posts': []}

# Selecionar todos os elementos que possuem a class post
posts = driver.find_elements_by_class_name('featured__head')

# Imprimir informações para cada post encontrado
for post in posts:
    # Pegar o título do post
    post_Title = post.find_element_by_class_name('mark__title')

    # Pegar o link do post
    post_Link = post.find_element_by_class_name('analytic-featured').get_attribute('href')

    # Imprimir o título do post
    print(u"Título: {titulo}".format(titulo=post_Title.text))

    # Imprimir o link do post
    print(u"Link: {link}".format(link=post_Link))

    # Armazenar as informações em um dicionário
    myDict['posts'].append(({"Título": "{titulo}".format(titulo=post_Title.text),
                            "Link": "{link}".format(link=post_Link)
                             }))

# Salvar os dados do dicionário em um arquivo JSON
with open('dadosOmelete.json', 'w') as json_file:
    json.dump(myDict, json_file, indent=4)

# Fechar o navegador
driver.quit()

from selenium import webdriver

# Criar instância do navegador
driver = webdriver.Chrome()

# Abrir a página do Python Club
driver.get('http://pythonclub.com.br/')

# Maximizar o browser
driver.maximize_window()

# Selecionar todos os elementos que possuem a class post
posts = driver.find_elements_by_class_name('post')

# Imprimir informações para cada post encontrado
for post in posts:
    # Pegar o título do post
    post_Title = post.find_element_by_class_name('post-title')

    # Pegar o link do post
    post_Link = post_Title.get_attribute('href')

    # Pegar o autor do post
    post_Avatar = post.find_element_by_class_name('avatar')
    post_Author = post_Avatar.get_attribute('alt')

    # Imprimir o título do post
    print(u"Título: {titulo}".format(titulo=post_Title.text))

    # Imprimir o link do post
    print(u"Link: {link}".format(link=post_Link))

    # Imprimir o autor do post
    print(u"Autor: {autor}".format(autor=post_Author))

driver.quit()
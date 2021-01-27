import requests
from bs4 import BeautifulSoup
import pandas as pd


# Função que busca as pastas e arquivos encontrado com a página especificada


def get_navegation(obj_soup, page_main):
    # lista para os dicionarios recebidos
    data = []
    # como a classe das subpastas são diferentes é preciso criar uma função para diferenciar
    # a primeira request na página principal das demais
    if page_main:
        # caso a page_main seja True passa o conteudo referente a classe da pagina principal
        grid = 'Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block'
    else:
        # Recebe a classe de subpastas
        grid = 'Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-block'

    # Primeiro pesquisamos a classe reponsavel por armazenar os arquivos que procuramos
    # e extraimos uma lista com apenas os que contem a tag role = 'row', após a priemira linha que nao precisamos

    for row in obj_soup.find(class_=grid).find_all(role="row")[1:]:
        try:
            # Pega o tipo de arquivo (Pasta, Arquivo, Symlink File)
            type_file = row.svg['aria-label']

            if type_file != 'Directory':
                type_file = 'File'
        except:
            type_file = 'File'
        # a url armazenada no href
        url = row.find('a').attrs['href']

        # Nome do arquivo
        try:
            name = row.find('a').attrs['title']
        except KeyError:
            name = 'others'

        extension = 'Directory'

        if type_file != 'Directory':
            extension = name.split('.')[-1]

            # junta os dados em um dicionario e adiciona dentro de uma lista
        data.append({'type_file': type_file, 'url': url, 'name': name, 'extension': extension})

    return data





def gera_dados_repositorio(url):
    # esta pasta contera todas as pastas que for preciso verificar, iniciando com o diretorio principal
    urls_directories = [url]
    print('lista de diretorios para pesquisar:', urls_directories)
    # conterá todos os dados da raspagem
    data_full = []
    # Passa a informação de que é a pagina principal do projeto
    page_main = True

    # Verifica se a quantidade de diretorios é menor que 0
    while len(urls_directories) > 0:
        # lista que armazena os subdiretorios
        subdirectories = []
        # Por cada diretorio encontrado
        for url_directory in urls_directories:
            # armazenando os dados coletados do repositório indicado com a função que busca os itens
            collected_data = get_navegation(html_convert_python('https://github.com/' + url_directory), page_main)

            # percorre todos os dados coletados
            for data in collected_data:
                # adiciona cada item coletado dentro do
                data_full.append(data)
                # se o tipo do arquivo for
                if data['type_file'] == 'Directory':
                    #  Armazena os subsdiretorios para as novas buscas
                    subdirectories.append(data['url'])

        # Quando a primeira busca for feita é passado o valor false,
        # para o sistema reconhecer que vem apenas subpastas
        page_main = False
        # A lista principal herda os subdiretorios
        urls_directories = subdirectories

    for dados in data_full:
        print(dados)


repos = ['Erickson-lopes-dev/Python_BeautifulSoup_V4.9.2',
         # 'Erickson-lopes-dev/Python_BeautifulSoup_V4.9.2',
         # 'frontpressorg/frontpress',
         # 'SambitAcharya/Mini-Projects',
         # 'jenkinsci/docker',
         # 'docker/compose'
         ]

for repo in repos:
    # print(url_repo)
    gera_dados_repositorio(repo)
    print()
    # get_navegation(html_convert_python(url_repo), True)
    # break
import requests
from bs4 import BeautifulSoup


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
        # Pega o tipo de arquivo (Pasta, Arquivo, Symlink File)
        type_file = row.svg['aria-label']
        # a url armazenada no href
        url = row.find('a').attrs['href']
        # Nome do arquivo
        name = row.find('a').attrs['title']
        print(name)
        print()


# Função converte uma o html de uma url para obj python do bs4
def html_convert_python(url):
    # Faz uma requisição trasendo o html
    req_get = requests.get(url)
    # A Beautiful Soup analisa o documento usando o melhor analisador disponível.
    # Ele usará um analisador HTML
    return BeautifulSoup(req_get.content, 'html.parser')  # retornando o obj


repos = ['Erickson-lopes-dev/Python_BeautifulSoup_V4.9.2',
         'frontpressorg/frontpress',
         'SambitAcharya/Mini-Projects', 'jenkinsci/docker', 'docker/compose']
for repo in repos:
    url_repo = 'https://github.com/' + repo
    obj_repo = html_convert_python(url_repo)

    get_navegation(obj_repo, True)
    break

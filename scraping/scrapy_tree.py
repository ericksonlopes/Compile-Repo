# Função que busca as pastas e arquivos encontrado com a página especificada
from scraping.funtion import html_convert_python


def get_data_page(url_page, page_main):
    """
        Captura as informações especificada dentro do arquivo convertido de HTML para python
    :param url_page:
    :param page_main:
    :return:
    """
    obj_soup = html_convert_python(url_page)
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

            # se caso nao seja diretorio todos os outros sao arquivos
            if type_file != 'Directory':
                type_file = 'File'
        except:
            type_file = 'File'
        # a url armazenada no href
        url = row.find('a').attrs['href']

        # Nome do arquivo
        try:
            name = row.find('a').attrs['title']
        except:
            # quando nao encontrar o nome do arquivo
            name = 'others'

        extension = 'Directory'

        # se caso o tipo do arquvio nao for diretorio, cria a extension
        if type_file != 'Directory':
            extension = name.split('.')[-1]

            # junta os dados em um dicionario e adiciona dentro de uma lista
        data.append({'type_file': type_file, 'url': url, 'name': name, 'extension': extension})

    return data

# Função que busca as pastas e arquivos encontrado com a página especificada
def get_data_page(obj_soup, page_main):
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

        type_file = row.svg['aria-label']

        # a url armazenada no href
        url = row.find('a').attrs['href']
        # Nome do arquivo
        name = row.find('a').attrs['title']

        # Por padrão a str é um directory
        extension = 'Directory'

        # Se o tipo de arquivo não for
        if type_file != 'Directory':
            # Apartir do nome faz um split para remover a virgula e retira o ultimo item ['extension', 'html'] -> html
            extension = name.split('.')[-1]

        # junta os dados em um dicionario e adiciona dentro de uma lista
        data.append({'type_file': type_file, 'url': url, 'name': name, 'extension': extension})

    # retorna os dados coletados do scraping
    return data

from scraping.scrapy_tree import get_data_page
from tqdm import tqdm


def get_data_repository_full(url, self):
    """
        Retorna Todos as informações especificadas
    :param self:
    :param url:
    :return:
    """
    print('\n')
    print(f"Buscando dados do repositório '{url.split('/')[1]}' do usuário '{url.split('/')[0]}'")
    # esta pasta contera todas as pastas que for preciso verificar, iniciando com o diretorio principal
    urls_directories = [url]
    # print('lista de diretorios para pesquisar:', urls_directories)
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
            collected_data = get_data_page(self.url_git + '/' + url_directory, page_main)

            # percorre todos os dados coletados
            for data in tqdm(collected_data, desc='Encontrado Arquivos'):

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

    # remtorna todos os dados
    return data_full

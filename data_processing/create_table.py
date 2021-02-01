from prettytable import PrettyTable
from scraping.scrapy_lines_bytes import get_lines_bytes
from tqdm import tqdm


def create_pettyTable(repo, data_full, self):
    """
        Função que constrói e retorna a tabela
    :param repo:
    :param data_full:
    :param self:
    :return:
    """
    # cria a tabela e passa as respectivas colunas
    table = PrettyTable(['Type File', 'URL', 'Name', 'Extension', 'Lines', 'Size'])

    for file in tqdm(data_full, desc='Construindo Tabela'):
        # Verifica se a chave 'type_file' é 'File', se for e tiver a chave 'extension' como 'Go to parent directory'
        if file['type_file'] == 'File' and file['extension'] != 'Go to parent directory':
            try:
                # Tenta buscar as informações de linhas e bytes do arquivo pela sua url
                lb = get_lines_bytes(self.url_git + file['url'])

                # Adiciona uma linha na tabela
                table.add_row([
                    file['type_file'],
                    file['url'].replace(f'/{repo}/blob/master', ''),
                    file['name'],
                    file['extension'],
                    lb[0],
                    lb[1]
                ])

            except:
                # Caso gere algum erro por arquivos solicitados que na verdade são links
                pass

    # alinha todos os itens das colunas
    table.align = 'l'
    # retorna a tabela ordenada pela coluna size

    print(table.get_string(sortby='Lines'))

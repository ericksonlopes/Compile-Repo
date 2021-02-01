from data_processing.create_table import create_pettyTable
from scraping.scrapy_data_full import get_data_repository_full
from tqdm import tqdm


class CompileRepo:
    def __init__(self):
        self.url_git = 'https://github.com'

        # Abre o arquivo e processa todos os dados
        with open('repositories.txt', 'r') as file:
            # Fatiando em linhas para lista
            self.repos = file.read().split()

        # percorre cara repositorio
        for repo in self.repos:
            # Realiza a
            data = get_data_repository_full(repo, self)
            # Concoca a função que cria a tabela e exibe a mesma
            create_pettyTable(repo, data, self)


if __name__ == '__main__':
    CompileRepo()

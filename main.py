from data_processing.create_table import create_pettyTable
from scraping.scrapy_data_full import get_data_repository_full


class CompileRepo:
    def __init__(self):
        self.url_git = 'https://github.com'

        with open('repositories.txt', 'r') as file:
            self.repos = file.read().split()

        for repo in self.repos:
            try:
                print(f"Buscando dados do repositório '{repo.split('/')[1]}' de {repo.split('/')[0]}")
                data = get_data_repository_full(repo)

                create_pettyTable(repo, data, self)

            except Exception as error:
                print(error)


if __name__ == '__main__':
    CompileRepo()

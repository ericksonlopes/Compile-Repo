from scraping.scrapy_data_full import get_data_repository_full


class CompileRepo:
    def __init__(self):
        self.url_git = 'https://github.com'

        with open('repositories.txt', 'r') as file:
            self.repos = file.read().split()

        for repo in self.repos:
            print(get_data_repository_full(repo))


if __name__ == '__main__':
    CompileRepo()

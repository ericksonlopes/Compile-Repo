from scraping.scrapy_data_full import get_data_repository_full
from scraping.scrapy_lines_bytes import get_lines_bytes


class CompileRepo:
    def __init__(self):
        self.url_git = 'https://github.com'

        with open('repositories.txt', 'r') as file:
            self.repos = file.read().split()

        for repo in self.repos:
            print(f"Pesuisando o repositório '{repo.split('/')[1]}' de {repo.split('/')[0]}")
            for item in get_data_repository_full(repo):

                if item['type_file'] == 'File':
                    if f'/{repo}/tree/' in item['url'] or item['url'] == f'/{repo}':
                        pass
                    else:
                        print(get_lines_bytes(self.url_git + item['url']), item['url'], item['extension'])
                        # print(x, '\n')
        print('#' * 100, '\n')



if __name__ == '__main__':
    CompileRepo()

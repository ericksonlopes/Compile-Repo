from data_processing.cute_lines_bytes import lines_bytes
from scraping.scrapy_data_full import get_data_repository_full
import treelib
import pandas as pd
from prettytable import PrettyTable


class CompileRepo:
    def __init__(self):
        self.url_git = 'https://github.com'

        with open('repositories.txt', 'r') as file:
            self.repos = file.read().split()

        for repo in self.repos:
            try:
                print(f"Pesuisando o repositório '{repo.split('/')[1]}' de {repo.split('/')[0]}")

                data = get_data_repository_full(repo)
                keys = data[0].keys()

                table = PrettyTable(keys)

                for item in data:
                    table.add_row([item[0], item[1], item[2], item[3]])

                print(table)
                # print(data)

                # for item in data:
                #     for x in item.keys():
                #         print(x)

                # instancia o obj Tree

                # tree = treelib.Tree()
                # tree.create_node(f"[{repo}]", '/')
                # for item in get_data_repository_full(repo):
                #     if item['type_file'] == 'Directory':
                #         print(item)
                #         name = f"[{item['name']}]"
                #
                #         parent = item['url'].replace(f'/{repo}/tree/master', '') \
                #             .replace(item['name'].replace(' ', '%20'), '')
                #
                #         path_name = item['url'].replace(f'/{repo}/tree/master', '')
                #
                #         # Verifica se não é o path base '/'
                #         if len(parent) > 1:
                #             # remove o ultimo elemento que é a barra
                #             parent = parent[:-1]
                #
                #         try:
                #             tree.create_node(name, path_name, parent=parent)
                #         except Exception as error:
                #             pass
                #
                #         # print()
                #     # se o item coletado for do tipo File
                #
                # for item in get_data_repository_full(repo):
                #     if item['type_file'] == 'File':
                #         # busca os itens
                #         lb = lines_bytes(item, repo, self)
                #         if lb:
                #             print(lb)
                #             parent = f"{lb['url'].replace(f'/{repo}/blob/master', '').replace(item['name'], '')}"
                #             formated_nome = f"{lb['name']} ({lb['lb']['lines']} linhas)"
                #
                #             if len(parent) > 1:
                #                 # remove o ultimo elemento que é a barra
                #                 parent = parent[:-1]
                #
                #             # print(parent)
                #             # print(formated_nome)
                #             # print(lb)
                #
                #             try:
                #                 tree.create_node(formated_nome, formated_nome, parent=parent)
                #             except Exception as error:
                #                 pass
                #                 # print(error)
                #             # print()
                # tree.show()
                # # analisar -> Fazer Tree partindo  dos caminhos dos arquivos, pois o git-hub não sobe pastas vazias

                print('#' * 100, '\n')
            except Exception as error:
                print(error)


if __name__ == '__main__':
    CompileRepo()

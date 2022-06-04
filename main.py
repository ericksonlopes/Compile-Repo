from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests


@dataclass
class RepoData:
    name: str
    type: str
    link: str


class CompileRepo:
    def __init__(self, repository: str):
        self.__repository = repository
        self.__files_list = []
        self.__directory_list = []

    @property
    def repository(self):
        return self.__repository

    @property
    def files_list(self):
        return self.__files_list

    @property
    def directory_list(self):
        return self.__directory_list

    @classmethod
    def html_convert_bs4(cls, url) -> BeautifulSoup:
        """
            Função Converte o conteudo HTML recebido pela requisição em objetos python, Retornando esse obj
        :param url: -> url completa
        :return:
        """
        # Faz uma requisição trazendo o html
        req_get = requests.get(url)
        # beautifulSoup transforma um documento HTML complexo em uma árvore complexa de objetos Python.
        return BeautifulSoup(req_get.content, 'html.parser')  # retornando o obj

    def get_files(self) -> None:
        """

        busca
        :return:
        """
        directorys = [self.__repository]
        while len(directorys) > 0:
            for link in directorys:
                sub_directorys = []
                req = self.html_convert_bs4(link)

                grid_itens = req.find(class_='js-details-container Details')

                list_itens = grid_itens.find_all(role='row')[1:]

                for row in list_itens:

                    try:
                        name_ = row.a['title']

                        if name_ != "Go to parent directory":
                            type_ = row.svg['aria-label']
                            link_ = 'https://github.com' + str(row.span.a['href'])

                            if 'Directory' == type_:
                                sub_directorys.append(link_)
                                self.__directory_list.append(RepoData(type=type_, link=link_, name=name_))
                            else:
                                self.__files_list.append(RepoData(type=type_, link=link_, name=name_))
                    except Exception as error:
                        print(error)

                directorys = sub_directorys


if __name__ == '__main__':
    cr = CompileRepo('https://github.com/Erickson-lopes-dev/Alexa_Skills')
    cr.get_files()

    for file in cr.files_list:
        print(file)

    print()
    for directory in cr.directory_list:
        print(directory)

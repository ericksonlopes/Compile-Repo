from typing import List

import requests
from bs4 import BeautifulSoup

from utils import DirectoryModel, FileModel


class CompileRepo:
    def __init__(self, repository: str):
        self.__repository = 'https://github.com/' + repository
        self.__files_list = []
        self.__directory_list = []

    @property
    def repository(self) -> str:
        return self.__repository

    @property
    def files_list(self) -> List[FileModel]:
        return self.__files_list

    @property
    def directory_list(self) -> List[DirectoryModel]:
        return self.__directory_list

    @classmethod
    def html_convert_bs4(cls, url) -> BeautifulSoup:
        """
        Função Converte o conteudo HTML recebido pela requisição em objetos python, Retornando esse obj
        :param url: url completa
        :return: BeautifulSoup
        """
        # Faz uma requisição trazendo o html
        req_get = requests.get(url)
        # beautifulSoup transforma um documento HTML complexo em uma árvore complexa de objetos Python.
        return BeautifulSoup(req_get.content, 'html.parser')  # retornando o obj

    def get_diretories_and_files(self) -> None:
        """
        Captura todos os dados necessarios (diretorios e arquivos)
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

                    name_ = row.a['title']

                    if name_ != "Go to parent directory":
                        type_ = row.svg['aria-label']
                        link_ = 'https://github.com' + str(row.span.a['href'])

                        if 'Directory' == type_:
                            sub_directorys.append(link_)
                            self.__directory_list.append(DirectoryModel(link=link_, name=name_))
                        else:
                            file_model = FileModel(type=type_, link=link_, name=name_)
                            self.get_info_files(file_model)
                            self.__files_list.append(file_model)

                directorys = sub_directorys

    def get_info_files(self, file: FileModel):
        req_file = self.html_convert_bs4(file.link.replace('blob', 'blame'))
        file_info = req_file.find(class_='file-info').text

        print(''.join(file_info.strip().split('\n')))

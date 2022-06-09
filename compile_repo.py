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

                            try:
                                new_file_model = self.get_info_file(file_model)
                                file_model = new_file_model
                            except Exception:
                                pass

                            self.__files_list.append(file_model)

                directorys = sub_directorys

    def get_info_file(self, file: FileModel):
        # Para acessar outra rota com as informações
        replace_link: str = file.link.replace('blob', 'blame')

        # Recebe o objeto bs4 para scraping
        req_file: BeautifulSoup = self.html_convert_bs4(replace_link)

        # Recebe o texto
        file_info: str = req_file.find(class_='file-info').text

        # limpa os dados
        file_cute: List[str] = file_info.strip().replace('\n', '').split()

        lines = file_cute[1]
        size = f"{file_cute[-2]} {file_cute[-1]}"

        file.lines = lines
        file.size = size

        # Adiciona a extensão
        if '.' in file.name:
            file.extension = file.name.split('.')[-1]
        else:
            file.extension = file.name

        return file

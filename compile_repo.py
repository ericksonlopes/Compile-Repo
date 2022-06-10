from typing import List

import requests
from bs4 import BeautifulSoup

from utils import DirectoryModel, FileModel, FullDataRepo


class CompileRepo:
    def __init__(self, repository: str):
        self.__repository: str = 'https://github.com/' + repository
        self.__files_list: List[FileModel] = []
        self.__directory_list: List[DirectoryModel] = []
        self.__branch: str = ''

        # Executa funções que traz os dados
        self.__get_diretories_and_files()

    @property
    def repository(self) -> str:
        return self.__repository

    @property
    def files_list(self) -> List[FileModel]:
        return self.__files_list

    @property
    def directory_list(self) -> List[DirectoryModel]:
        return self.__directory_list

    @property
    def branch(self):
        return self.__branch

    @classmethod
    def __html_convert_bs4(cls, url) -> BeautifulSoup:
        """
        Função Converte o conteudo HTML recebido pela requisição em objetos python, Retornando esse obj
        :param url: url completa
        :return: BeautifulSoup
        """
        # Faz uma requisição trazendo o html
        req_get = requests.get(url)
        # beautifulSoup transforma um documento HTML complexo em uma árvore complexa de objetos Python.
        return BeautifulSoup(req_get.content, 'html.parser')  # retornando o obj

    def __get_diretories_and_files(self) -> None:
        """
        Captura todos os dados necessarios (diretorios e arquivos)
        :return:
        """
        directorys = [self.__repository]

        while len(directorys) > 0:
            for link in directorys:
                sub_directorys = []
                req = self.__html_convert_bs4(link)

                # Captura o nome da branch
                self.__branch = req.find(class_='btn css-truncate').text.strip('\n')

                # Frid que localiza todos os arquivos
                grid_itens = req.find(class_='js-details-container Details')

                # Separa todas as linhas
                list_itens = grid_itens.find_all(role='row')[1:]

                for row in list_itens:

                    name_ = row.a['title']

                    if name_ != "Go to parent directory":
                        type_ = row.svg['aria-label']
                        link_ = 'https://github.com' + str(row.span.a['href'])

                        if 'Directory' == type_:  # diretório
                            path_dire = link_.split(f'/tree/{self.__branch}')[-1].replace(name_, '')
                            self.__directory_list.append(DirectoryModel(link=link_, name=name_, path=path_dire))

                            # Adiciona um subdiretório na lista
                            sub_directorys.append(link_)

                        else:  # arquivo
                            path_file = link_.split(f'/blob/{self.__branch}')[-1].replace(name_, '')
                            file_model = FileModel(type=type_, link=link_, name=name_, path=path_file)

                            try:
                                new_file_model = self.__get_size_lines_on_file(file_model)
                                file_model = new_file_model
                            except AttributeError:
                                pass
                            except ValueError:
                                pass

                            else:
                                # Adiciona a extensão
                                if '.' in file_model.name:
                                    file_model.extension = file_model.name.split('.')[-1]
                                else:
                                    file_model.extension = file_model.name

                            self.__files_list.append(file_model)

                # Transforma os sub_diretórios em diretórios para serem explorados
                directorys = sub_directorys

    def __get_size_lines_on_file(self, file: FileModel) -> FileModel:
        """
        Extrai os dados da url presente no objeto
        :param file: FileModel
        :return:
        """
        # Para acessar outra rota com as informações
        replace_link: str = file.link.replace('blob', 'blame')

        # Recebe o objeto bs4 para scraping
        req_file: BeautifulSoup = self.__html_convert_bs4(replace_link)

        # Recebe o texto
        file_info: str = req_file.find(class_='file-info').text

        # Limpa os dados
        file_cute: List[str] = file_info.strip().replace('\n', '').split()

        # Atribui os valores
        file.lines = int(file_cute[1])
        file.size = f"{file_cute[-2]} {file_cute[-1]}"

        return file

    def return_full_data_repo(self) -> FullDataRepo:
        """
        Retorna todos os dados coletados em um objeto
        :return: FullDataRepo
        """
        return FullDataRepo(
            repository=self.__repository,
            files=self.__files_list,
            directories=self.__directory_list,
            branch=self.__branch
        )

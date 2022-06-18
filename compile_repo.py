from datetime import datetime

import requests
from bs4 import BeautifulSoup

from utils import *


class CompileBase:
    def __init__(self, repository: str):
        self.__repository: str = 'https://github.com/' + repository

    @property
    def repository(self) -> str:
        return self.__repository

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


class CompileRepo(CompileBase):
    def __init__(self, repository: str):
        super().__init__(repository)
        self.__files_list: List[FileModel] = []
        self.__directory_list: List[DirectoryModel] = []
        self.__branch: str = ''

    @property
    def files_list(self) -> List[FileModel]:
        return self.__files_list

    @property
    def directory_list(self) -> List[DirectoryModel]:
        return self.__directory_list

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, branch):
        self.__branch = branch

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

                # Captura o nome da branch
                if self.__branch == '':
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
        req_file: BeautifulSoup = self.html_convert_bs4(replace_link)

        # Recebe o texto
        file_info: str = req_file.find(class_='file-info').text

        # Limpa os dados
        file_cute: List[str] = file_info.strip().replace('\n', '').split()

        # Atribui os valores
        file.lines = int(file_cute[1])
        file.size = f"{file_cute[-2]} {file_cute[-1]}"

        return file

    def return_full_data_repo(self) -> FullDataModel:
        """
        Retorna todos os dados coletados em um objeto
        :return: FullDataRepo
        """
        return FullDataModel(
            repository=self.__repository,
            files=self.__files_list,
            directories=self.__directory_list,
            branch=self.__branch
        )


class BranchsRepo(CompileBase):
    def __init__(self, repository: str):
        super().__init__(repository)
        self.__branches_all_url = self.repository + '/branches/all'
        self.__branchs = []

    @property
    def branchs(self):
        return self.__branchs

    def get_all_branchs(self) -> List[BranchModel]:
        num = 1

        while num:
            soup_html = self.html_convert_bs4(self.__branches_all_url + f'?page={num}')

            # Pega todas as classes de cada linha com a branch
            li_list: List[BeautifulSoup] = soup_html.find_all(class_='Box-row position-relative')

            # se não tiver nenhum item, cancela o loop
            if not li_list:
                break

            for li in li_list:
                # linha da branch
                branch_filter_item = li.find('branch-filter-item')
                # Pega o nome da branch
                name = branch_filter_item.attrs['branch']
                # pega o caminho da branch
                path = branch_filter_item.attrs['dialog-body-path']

                # Captura as divs da linha da branch
                updated = branch_filter_item.findAll('div')
                # Pera o primeiro item que contém a data e quem commitou
                updated = updated[0].text
                # Retira os espaços e o nome da branch
                updated = updated.replace(name, '')
                # Separa as letras pelos espaços
                updated = updated.split()

                # Pega o nome de quem fez o commit
                updated_by = updated[-1]
                # Pega a data da atualização
                updated_date = datetime.strptime(' '.join(updated[1:4]), '%b %d, %Y').date()

                self.__branchs.append(BranchModel(name=name, path=path, update_by=updated_by, update_date=updated_date))

            num += 1

        return self.__branchs

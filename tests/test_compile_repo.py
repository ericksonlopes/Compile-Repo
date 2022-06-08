from compile_repo import CompileRepo
import pytest


@pytest.mark.parametrize('url', [
    'Erickson-lopes-dev/Alexa_Skills',
    'Erickson-lopes-dev/Words-In-Songs'
])
def test_get_infos(url):
    cr = CompileRepo(url)

    # Executa o código de busca
    cr.get_infos()

    list_files = cr.files_list
    print(list_files, '\n')

    list_directories = cr.directory_list
    print(list_directories, '\n')

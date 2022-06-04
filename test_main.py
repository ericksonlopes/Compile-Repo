from main import CompileRepo
import pytest


@pytest.mark.parametrize('url', [
    'https://github.com/Erickson-lopes-dev/Alexa_Skills',
    'https://github.com/Erickson-lopes-dev/Words-In-Songs'
])
def test_get_infos(url):
    cr = CompileRepo(url)

    # Executa o código de busca
    cr.get_infos()

    print(cr.files_list, '\n')
    print(cr.directory_list, '\n')

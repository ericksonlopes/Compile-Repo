import pytest

from compile_repo import CompileRepo


@pytest.mark.parametrize('url', [
    # "angular/angular"
    # 'Erickson-lopes-dev/Alexa_Skills',
    # 'Erickson-lopes-dev/Words-In-Songs',
    "Erickson-lopes-dev/Compile-Repo"
])
def test_get_infos(url):
    cr = CompileRepo(url)

    # Executa o código de busca
    cr.get_diretories_and_files()

    assert isinstance(cr.repository, str)
    assert isinstance(cr.files_list, list)
    assert isinstance(cr.directory_list, list)

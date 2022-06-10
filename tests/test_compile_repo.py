import pytest

from compile_repo import CompileRepo
from utils import FullDataRepo


@pytest.mark.parametrize('url', [
    # "angular/angular"
    'Erickson-lopes-dev/Alexa_Skills',
    'Erickson-lopes-dev/Words-In-Songs',
    "Erickson-lopes-dev/Compile-Repo"
])
def test_class_compile_repo(url):
    cr = CompileRepo(url)

    assert isinstance(cr.repository, str)
    assert isinstance(cr.files_list, list)
    assert isinstance(cr.directory_list, list)
    assert isinstance(cr.branch, str)
    assert isinstance(cr.return_full_data_repo(), FullDataRepo)
    print(cr.return_full_data_repo(), '\n')

from typing import List

import pytest

from compile_repo import CompileRepo, BranchsRepo
from utils import FullDataModel


@pytest.mark.parametrize('url', [
    # "angular/angular"
    'Erickson-lopes-dev/Alexa_Skills',
    'Erickson-lopes-dev/Words-In-Songs',
    "Erickson-lopes-dev/Compile-Repo"
])
def test_class_compile_repo(url):
    cr = CompileRepo(url)
    cr.get_diretories_and_files()

    assert isinstance(cr.repository, str)
    assert isinstance(cr.files_list, list)
    assert isinstance(cr.directory_list, list)
    assert isinstance(cr.branch, str)
    assert isinstance(cr.return_full_data_repo(), FullDataModel)
    print(cr.return_full_data_repo(), '\n')


@pytest.mark.parametrize('url', [
    # "angular/angular"
    'Erickson-lopes-dev/Alexa_Skills',
    'Erickson-lopes-dev/Words-In-Songs',
    "Erickson-lopes-dev/Compile-Repo"
])
def test_class_branchs(url):
    bc = BranchsRepo(url)
    bc.get_all_branchs()

    assert isinstance(bc.branchs, List)
    print(bc.branchs)

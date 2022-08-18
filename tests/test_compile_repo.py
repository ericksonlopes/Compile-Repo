from typing import List

import pytest

from src.compile_repo import CompileRepo, BranchsRepo
from src.models import *


@pytest.mark.parametrize('url', [
    # "angular/angular"
    'Erickson-lopes-dev/Alexa_Skills',
    'Erickson-lopes-dev/Words-In-Songs',
    "Erickson-lopes-dev/Compile-Repo"
])
def test_class_compile_repo(url):
    cr = CompileRepo(url)

    assert isinstance(cr.get_diretories_and_files(), FullDataModel)
    assert isinstance(cr.branch, str)


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

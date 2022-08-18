from dataclasses import dataclass
from typing import List

from src.models.DirectoryModel import DirectoryModel
from src.models.FileModel import FileModel


@dataclass
class FullDataModel:
    repository: str
    branch: str
    files: List[FileModel]
    directories: List[DirectoryModel]

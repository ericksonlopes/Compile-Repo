from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class FileModel:
    name: str
    link: str
    type: str


@dataclass(frozen=True)
class DirectoryModel:
    name: str
    link: str
    type: str = "Directory"


@dataclass
class ReturnModel:
    repository: str
    files: List[FileModel]
    directories: List[DirectoryModel]

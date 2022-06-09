from dataclasses import dataclass
from typing import List


@dataclass
class FileModel:
    name: str
    link: str
    type: str
    size: str = None
    lines: int = None
    extension: str = None


@dataclass(frozen=True)
class DirectoryModel:
    name: str
    link: str
    type: str = "Directory"


@dataclass(frozen=True)
class FullDataRepo:
    repository: str
    files: List[FileModel]
    directories: List[DirectoryModel]

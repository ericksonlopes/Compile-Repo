from dataclasses import dataclass
from typing import List


@dataclass
class FileModel:
    name: str
    link: str
    type: str
    extension: str = None
    lines: int = None
    size: str = None


@dataclass(frozen=True)
class DirectoryModel:
    name: str
    link: str
    type: str = "Directory"


@dataclass(frozen=True)
class ReturnModel:
    repository: str
    files: List[FileModel]
    directories: List[DirectoryModel]

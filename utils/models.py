from dataclasses import dataclass
from typing import List


@dataclass
class PropertyModel:
    path: str
    name: str
    link: str
    type: str


@dataclass
class FileModel(PropertyModel):
    size: str = None
    lines: int = None
    extension: str = None


@dataclass
class DirectoryModel(PropertyModel):
    type: str = "Directory"


@dataclass
class FullDataRepo:
    repository: str
    files: List[FileModel]
    directories: List[DirectoryModel]

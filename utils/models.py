from dataclasses import dataclass
from datetime import date
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
class FullDataModel:
    repository: str
    branch: str
    files: List[FileModel]
    directories: List[DirectoryModel]


@dataclass
class BranchModel:
    name: str
    path: str
    update_by: str
    update_date: date

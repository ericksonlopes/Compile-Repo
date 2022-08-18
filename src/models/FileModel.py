from dataclasses import dataclass

from src.models.PropertyModel import PropertyModel


@dataclass
class FileModel(PropertyModel):
    size: str = None
    lines: int = None
    extension: str = None

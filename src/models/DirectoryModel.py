from dataclasses import dataclass

from src.models.PropertyModel import PropertyModel


@dataclass
class DirectoryModel(PropertyModel):
    type: str = "Directory"

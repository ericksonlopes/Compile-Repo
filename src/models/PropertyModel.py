from dataclasses import dataclass


@dataclass
class PropertyModel:
    path: str
    name: str
    link: str
    type: str

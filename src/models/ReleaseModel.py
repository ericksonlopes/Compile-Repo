from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReleaseModel:
    name: str
    date: datetime
    user: str

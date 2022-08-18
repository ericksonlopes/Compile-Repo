from dataclasses import dataclass
from datetime import date


@dataclass
class BranchModel:
    name: str
    path: str
    update_by: str
    update_date: date

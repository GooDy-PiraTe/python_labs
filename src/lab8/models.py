from dataclasses import dataclass
from datetime import *


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")
        if not (0.0 <= float(self.gpa) <= 5.0):
            raise ValueError("gpa must be between 0 and 5")

    def __str__(self):
        return f"{self.fio}, {self.group}, {self.gpa}"

    def age(self) -> int:
        today = date.today()
        bd_year = int(self.birthdate.split("-")[0])
        return today.year - bd_year

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

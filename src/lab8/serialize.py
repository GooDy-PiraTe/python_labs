import json
from models import Student
from pathlib import Path


def students_to_json(students: list, path: str) -> None:
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=True, indent=2)


def students_from_json(path: str) -> list["Student"]:
    try:
        with (Path(path)).open("r", encoding="utf-8") as f:
            dict_data = json.load(f)
        if len(dict_data) == 0:
            raise ValueError("Пустой JSON")
        data = []
        for student in dict_data:
            data.append(Student.from_dict(student))
        return data
    except FileNotFoundError:
        raise FileNotFoundError("Файл не был найден")


path_to_json = Path("data/lab8/students_input.json")
npath = "data/lab8/students_output.json"

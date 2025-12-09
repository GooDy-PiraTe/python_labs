import csv
from pathlib import Path
from src.lab8.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8")

    def _read_all(self, header=False):
        with open(self.path, "r", encoding="utf-8") as csv_file:
            rdr = csv.DictReader(csv_file)
            head = rdr.fieldnames
            if header:
                return head
            lrdr = list(rdr)
            sorted_data = []
            for elem in lrdr:
                sorted_elem = {key: elem.get(key) for key in head}
                sorted_data.append(sorted_elem)
        return sorted_data

    def list(self):
        in_data, out_data = self._read_all(), []
        for item in in_data:
            out_data.append(Student(**item))
        return out_data

    def add(self, student: Student):
        head = self._read_all(header=True)
        item = student.to_dict()
        sorted_data = []
        sorted_item = {key: item.get(key, None) for key in head}
        sorted_data.append(sorted_item)
        with open(self.path, "a", encoding="utf-8", newline="") as file:
            wrt = csv.DictWriter(file, fieldnames=head)
            wrt.writerows(sorted_data)

    def find(self, substr: str):
        rows = self._read_all()
        return [r for r in rows if substr in r["fio"]]

    def remove(self, fio: str):
        head = self._read_all(header=True)
        rows = self._read_all()
        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                break
        with open(self.path, "w", encoding="utf-8", newline="") as file:
            wrt = csv.DictWriter(file, fieldnames=head)
            wrt.writeheader()
            wrt.writerows(rows)

    def update(self, fio: str, **fields):
        head = self._read_all(header=True)
        rows = self._read_all()
        for item in rows:
            if item["fio"] == fio:
                for field in fields:
                    item[field] = fields[field]
                    fl = 1
                break
        with open(self.path, "w", encoding="utf-8", newline="") as file:
            wrt = csv.DictWriter(file, fieldnames=head)
            wrt.writeheader()
            wrt.writerows(rows)


if __name__ == "__main__":
    test_group = Group("./data/lab9/students.csv")

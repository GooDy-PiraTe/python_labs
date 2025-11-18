from openpyxl import Workbook
import csv
from pathlib import Path

path_to_csv = Path("data/lab5/carcosa.csv")
path_new_xl = "data/lab5/newxl.xlsx"


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            rdr = csv.DictReader(csv_file)
            head = rdr.fieldnames
            lrdr = list(rdr)
            if len(lrdr) == 0:
                raise ValueError("Пустой csv")
            sorted_data = []
            for elem in lrdr:
                sorted_elem = {key: elem.get(key) for key in head}
                sorted_data.append(sorted_elem)
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        ws.append(head)
        for elem in sorted_data:
            row = [elem.get(key, "") for key in head]
            ws.append(row)
        for col in ws.columns:
            mxl = max(len(str(cell.value or "")) for cell in col)
            ws.column_dimensions[col[0].column_letter].width = max(mxl + 2, 8)
        wb.save(xlsx_path)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не был найден")


csv_to_xlsx(path_to_csv, path_new_xl)

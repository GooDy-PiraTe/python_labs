from re import findall
from pathlib import Path
import json, csv
from openpyxl import Workbook


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold: text = text.casefold()
    if yo2e: text = (text.replace('ё', 'е')).replace('Ё', 'Е')
    text = ' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    tokens = findall(r'\w+(?:-\w+)*', text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freq_sorted = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    ans = []
    for i in range(n):
        try: ans.append(freq_sorted[i])
        except: break 
    return ans

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try: text = p.read_text(encoding=encoding)
    except FileNotFoundError: raise FileNotFoundError('Файл не найден')  
    except UnicodeDecodeError: raise UnicodeDecodeError('unicode=[другая кодировка]') 
    return ' '.join(text.split())

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if len(rows): eq = len(rows[0])
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            if len(r) != eq: raise ValueError('строки разного размера')
            w.writerow(r)
        
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            rdr = csv.DictReader(csv_file)
            head = rdr.fieldnames
            lrdr = list(rdr)
            if len(lrdr) == 0: raise ValueError('Пустой csv')
            sorted_data = []
            for elem in lrdr:
                sorted_elem = {key: elem.get(key) for key in head}
                sorted_data.append(sorted_elem)
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        ws.append(head)
        for elem in sorted_data:
            row = [elem.get(key, '') for key in head]
            ws.append(row)
        for col in ws.columns:
            mxl = max( len(str(cell.value or '')) for cell in col )
            ws.column_dimensions[col[0].column_letter].width = max(mxl+2, 8)
        wb.save(xlsx_path)
    except FileNotFoundError: raise FileNotFoundError('Файл не был найден')

def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        with Path(json_path).open('r', encoding="utf-8") as json_file:
            data = json.load(json_file)
        if len(data) == 0: raise ValueError('Пустой JSON')
        try: head = list(data[0].keys())
        except AttributeError: raise ValueError('Внутри находятся не словари') 
        sorted_data = []
        for item in data:
            if not isinstance(item, dict): raise ValueError('Внутри находятся не словари')
            sorted_item = {key: item.get(key, None) for key in head}
            sorted_data.append(sorted_item)
        with open(csv_path, 'w', encoding='utf-8') as file:
            wrt = csv.DictWriter(file, fieldnames=head)
            wrt.writeheader()
            wrt.writerows(sorted_data)
    except FileNotFoundError: raise FileNotFoundError('Файл не был найден')
    except json.decoder.JSONDecodeError: raise ValueError("Неверный формат")


def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        with open(Path(csv_path), "r", encoding="utf-8") as csv_file:
            rdr = csv.DictReader(csv_file)
            head = rdr.fieldnames
            lrdr = list(rdr)
            sorted_data = []
            for elem in lrdr:
                sorted_elem = {key: elem.get(key) for key in head}
                sorted_data.append(sorted_elem)
        if len(sorted_data) == 0: raise ValueError('Пустой файл')
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(sorted_data, json_file, indent=4, ensure_ascii=True, sort_keys=True)
    except FileNotFoundError: raise FileNotFoundError('Файл не был найден')



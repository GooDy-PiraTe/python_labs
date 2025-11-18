import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try:
        text = p.read_text(encoding=encoding)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("unicode=[другая кодировка]")
    return " ".join(text.split())


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    rows = list(rows)
    if len(rows):
        eq = len(rows[0])
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            if len(r) != eq:
                raise ValueError("строки разного размера")
            w.writerow(r)


print(read_text("./data/samples/text.txt"))

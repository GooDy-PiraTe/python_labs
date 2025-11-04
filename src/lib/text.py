from re import findall
from pathlib import Path

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

# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]


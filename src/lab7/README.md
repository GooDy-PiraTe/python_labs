
# GooDy-PiraTe (Саргаева Анна БИВТ-25-1)

## Лабораторная работа 7

### Задание A
pytest, test_text.py
```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# normalize по умолчанию
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт МИР", "привет мир"),
        ("Hello WORLD", "hello world"),
        ("один пробел", "один пробел"),
        ("", ""),
        ("      ", ""),
        ("\t \t \r \n   \r   ", ""),
        ("монолит", "монолит"),
        ("  много   пробелов     ", "много пробелов"),
        ("новая\nстрока", "новая строка"),
        ("ёжик ЁЖИК ёлка", "ежик ежик елка"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


# normalize с примочками
@pytest.mark.parametrize(
    "source, casefold, yo2e, expected",
    [
        ("Hello WORLD", True, True, "hello world"),
        ("Hello WORLD", False, True, "Hello WORLD"),
        ("ПрИвЕт", True, True, "привет"),
        ("ПрИвЕт", False, True, "ПрИвЕт"),
        ("ёжик ЁЖ", True, True, "ежик еж"),
        ("ёжик ЁЖ", True, False, "ёжик ёж"),
        ("ПРИЁМ", False, True, "ПРИЕМ"),
        ("ПРИЁМ", False, False, "ПРИЁМ"),
        ("Ёлка World", True, True, "елка world"),
        ("Ёлка World", True, False, "ёлка world"),
        ("Ёлка World", False, True, "Елка World"),
        ("Ёлка World", False, False, "Ёлка World"),
        ("", True, True, ""),
        ("      ", False, False, ""),
    ],
)
def test_normalize_basic(source, casefold, yo2e, expected):
    assert normalize(source, casefold=casefold, yo2e=yo2e) == expected


# tokenize
@pytest.mark.parametrize(
    "source, expected",
    [
        ("один два три", ["один", "два", "три"]),
        ("", []),
        (" !@#$%^&*()", []),
        ("монолит", ["монолит"]),
        ("какой-то текст", ["какой-то", "текст"]),
        ("привет, мир!", ["привет", "мир"]),
        ("один.два.три", ["один", "два", "три"]),
        (
            "очень много слов подряд! дефис-дефис",
            ["очень", "много", "слов", "подряд", "дефис-дефис"],
        ),
        ("same same", ["same", "same"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


# count_freq n top_n (частота)
@pytest.mark.parametrize(
    "source, expected",
    [
        (["два", "два", "один"], {"два": 2, "один": 1}),
        (
            ["первый", "первый", "а-второй", "б-третий"],
            {"первый": 2, "а-второй": 1, "б-третий": 1},
        ),
        ([], {}),
        (["монолит"], {"монолит": 1}),
        (["test-case", "test", "case"], {"test-case": 1, "test": 1, "case": 1}),
        (["123", "321", "123"], {"123": 2, "321": 1}),
        (["1", "2", "3", "2", "1"], {"1": 2, "2": 2, "3": 1}),
    ],
)
def test_count_freq_and_top_n(source, expected):
    assert count_freq(source) == expected


# top_n
@pytest.mark.parametrize(
    "source, n, expected",
    [
        ({"apple": 5, "banana": 3, "cherry": 7}, 2, [("cherry", 7), ("apple", 5)]),
        ({"a": 10, "b": 8, "c": 6, "d": 4}, 3, [("a", 10), ("b", 8), ("c", 6)]),
        ({}, 5, []),
        ({"word": 1}, 5, [("word", 1)]),
        ({"a": 1, "b": 2}, 0, []),
        ({"single": 5}, 1, [("single", 5)]),
        ({"a": 1, "b": 2}, -1, []),
    ],
)
def test_top_n_tie_breaker(source, n, expected):
    assert top_n(source, n) == expected


```
### Задание B
pytest, test_json_csv
```python
import pytest
import json, csv
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path):
    sor = tmp_path / "people.json"
    res = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    sor.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(sor), str(res))

    with res.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path):
    sor = tmp_path / "people.csv"
    res = tmp_path / "people.json"

    csv_content = "name,age\nAlice,22\nBob,25"
    sor.write_text(csv_content, encoding="utf-8")
    csv_to_json(str(sor), str(res))

    with res.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert {"name", "age"} <= set(data[0].keys())
    assert data[0]["name"] == "Alice"
    assert data[0]["age"] == "22"


def test_json_to_csv_empty_file(tmp_path):
    # Пустой JSON файл
    sor = tmp_path / "empty.json"
    res = tmp_path / "output.csv"
    sor.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(sor), str(res))


def test_csv_to_json_empty_file(tmp_path):
    # Пустой CSV файл
    sor = tmp_path / "empty.csv"
    res = tmp_path / "output.json"
    sor.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(sor), str(res))


def test_json_to_csv_file_not_found(tmp_path):
    # non-ex
    sor = tmp_path / "nonex.json"
    res = tmp_path / "output.csv"

    with pytest.raises(FileNotFoundError):
        json_to_csv(str(sor), str(res))


def test_csv_to_json_file_not_found(tmp_path):
    # non-ex
    sor = tmp_path / "nonex.csv"
    res = tmp_path / "output.json"

    with pytest.raises(FileNotFoundError):
        csv_to_json(str(sor), str(res))


def test_json_to_csv_different_columns(tmp_path):
    sor = tmp_path / "diff.json"
    res = tmp_path / "diff.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25, "city": "SPb"},
        {"name": "Charlie", "city": "Moscow"},
    ]
    sor.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    json_to_csv(str(sor), str(res))

    with res.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 3
    assert {"name", "age"} == set(rows[0].keys())
    assert rows[0]["name"] == "Alice"
    assert rows[0]["age"] == "22"
    assert rows[1]["name"] == "Bob"
    assert rows[1]["age"] == "25"
    assert rows[2]["name"] == "Charlie"
    assert rows[2]["age"] == ""


def test_json_to_csv_not_dicts(tmp_path):
    sor = tmp_path / "not_dicts.json"
    res = tmp_path / "output.csv"
    data = ["not", "a", "dict"]
    sor.write_text(json.dumps(data), encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(sor), str(res))


def test_json_to_csv_mixed_types(tmp_path):
    sor = tmp_path / "mixed.json"
    res = tmp_path / "output.csv"
    data = [{"name": "Alice"}, "not_a_dict", {"name": "Bob"}]
    sor.write_text(json.dumps(data), encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(sor), str(res))


def test_csv_to_json_only_headers(tmp_path):
    sor = tmp_path / "headers.csv"
    res = tmp_path / "headers.json"

    csv_content = "name,age,city"
    sor.write_text(csv_content, encoding="utf-8")
    with pytest.raises(ValueError, match="Пустой файл"):
        csv_to_json(str(sor), str(res))


def test_csv_to_json_monolith(tmp_path):
    sor = tmp_path / "monolith.csv"
    res = tmp_path / "monolith.json"

    csv_content = "name,age\nMonolith,30"
    sor.write_text(csv_content, encoding="utf-8")
    csv_to_json(str(sor), str(res))

    with res.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["name"] == "Monolith"
    assert data[0]["age"] == "30"


```
общий прогон pytest на python_labs 
```
pytest -q
```
![Картинка 1](./screenshots/pytest_gotit.png)
### Задание C
black
```
black .
```
![Картинка 2](./screenshots/black_check.png)

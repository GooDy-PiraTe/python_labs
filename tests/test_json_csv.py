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

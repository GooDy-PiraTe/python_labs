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

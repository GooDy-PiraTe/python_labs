import argparse
from src.lib.text import json_to_csv, csv_to_json, csv_to_xlsx
import sys, os
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Анализ частот слов в тексте")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Адрес входного файла")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Адрес входного файла")
    stats_parser.add_argument("--top", type=int, default=5, help='Топ слов по частоте')

    args = parser.parse_args()

    if args.command == "cat":
        #  python src/lab6/cli_text.py cat --input data/samples/text.txt -n
        f = open(Path(args.input)).readlines()
        if args.n:
            for i in range(len(f)):
                print(f"{i+1}. {f[i][:-1]}")
        else:
            for line in f: print(line[:-1])
    elif args.command == "stats":
        #  python src/lab6/cli_text.py stats --input data/samples/text.txt --top 5
        with open(args.input, 'r') as f:
            tf = f.read()
        cf = tokenize(normalize(tf))
        tnf = top_n(count_freq(cf), args.top)
        for elem in tnf: print(f'{elem[0]}:{elem[1]}') 


if __name__ == "__main__":
    main()
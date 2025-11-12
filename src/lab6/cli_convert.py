import argparse
from src.lib.text import json_to_csv, csv_to_json, csv_to_xlsx
import sys, os

def main():
    try: 
        parser = argparse.ArgumentParser(description="Конвертеры данных")
        sub = parser.add_subparsers(dest="cmd")

        jc = sub.add_parser("json2csv", help='Конвертирует json в csv')
        jc.add_argument("--in", dest="input", required=True, help="Адрес входного файла")
        jc.add_argument("--out", dest="output", required=True, help="Адрес для итогового файла")

        cj = sub.add_parser("csv2json", help='Конвертирует csv в json')
        cj.add_argument("--in", dest="input", required=True, help="Адрес входного файла")
        cj.add_argument("--out", dest="output", required=True, help="Адрес для итогового файла")

        cx = sub.add_parser("csv2xlsx", help='Конвертирует csv в xlsx')
        cx.add_argument("--in", dest="input", required=True, help="Адрес входного файла")
        cx.add_argument("--out", dest="output", required=True, help="Адрес для итогового файла")

        args = parser.parse_args()
        a = args.cmd
        match a:
            case "json2csv":
                if not args.input.exists(): raise FileNotFoundError(f"Файл не найден")
                json_to_csv(args.input, args.output)
            case "csv2json": 
                if not args.input.exists(): raise FileNotFoundError(f"Файл не найден")
                try: csv_to_json(args.input, args.output)
                except: pass
            case "csv2xlsx": 
                if not args.input.exists(): raise FileNotFoundError(f"Файл не найден")
                try: csv_to_xlsx(args.input, args.output)
                except: pass
    except: parser.error('Некорректные аргументы')

if __name__ == "__main__": 
    main()


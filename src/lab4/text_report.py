import sys
import os
from pathlib import Path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
from text import *
from io_txt_csv import *

data_path = './data/lab4/input.txt'
report_path = './data/lab4/report.csv'

text = read_text(data_path)

norm = normalize(text)
tok = tokenize(norm)
cnt_frq = count_freq(tok)
top_5 = top_n(cnt_frq)
top_all = top_n(cnt_frq, len(cnt_frq))
write_csv(rows=top_all, path=report_path, header=['word', 'count'])
#краткий отчет
print(f"Всего слов: {len(tok)}")
print(f"Уникальных слов: {len(cnt_frq)}")
print(f'Топ-5: {top_5}')

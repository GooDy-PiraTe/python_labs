line = input("in: ")
word_started = False
origin = []
step = 0
f_i = 0
s_i = 0
for i in range(len(line)):
    symb = line[i]
    if symb.isupper() and not word_started:
        word_started = True
        f_i = i
        origin.append(symb)
    if word_started and symb.isdigit() and not s_i:
        s_i = i + 1
        step = s_i - f_i
    if word_started and step and (i - f_i) % step == 0:
        origin.append(symb)
    if word_started and symb == ".":
        break
print(f"out: {''.join(origin)}")


"""
Ht1eadljjl12ojh.
H t1 e ad l jj l 12 o jh .
0 12 3 45 6 78 9

hfh H t1e a dl
012 3 456 7 89

H t1e a dld r
0 123 4 567 8 
"""
